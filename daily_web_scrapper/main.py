# This file runs if you run it locally since env variables are set. To run it in docker, one needs to set ARGs in Dockerfile and send arguments on command (or send .env file).
# NOTE Original source: https://towardsdev.com/easily-use-selenium-with-aws-lambda-2cc49ca43b93

# Python packages (in alphabetical order)
from datetime import datetime
from dateutil.relativedelta import relativedelta
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import os
import smtplib
import sys
from tempfile import mkdtemp

# Third party packages (in alphabetical order)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from yahoo_fin import stock_info as si

# TODO add a symbol duplicate check

# Path to file where info will be saved
LOGS_FILE_PATH = "/tmp/text.txt"

def send_email(path_to_attachment):
    # Initialize Email and Server Variables
    gmail_user = os.environ['GMAIL_APP_USER']
    gmail_app_password = os.environ['GMAIL_APP_PSW']
    email_body = 'Find attached a file with today\'s stocks\' analysis.'
    email_from = gmail_user
    email_to = os.environ['EMAIL_TO']

    message = MIMEMultipart()
    message['Subject'] = 'Stocks Analysis'
    body_part = MIMEText(email_body)
    message.attach(body_part)
    
    #Attach file
    with open(path_to_attachment,'rb') as file:
        message.attach(MIMEApplication(file.read(), Name="stocks.txt"))
    
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(email_from, email_to.split(','), message.as_string())
        server.close()
        print('Email sent!\n')
    except Exception as exception:
        print(f"Error when sending email: {exception}\n")

def init_log_file(path_to_file):
    orig_stdout = sys.stdout
    logs_file_instance = open(path_to_file, "w")
    sys.stdout = logs_file_instance
    print(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n")
    logs_file_instance.close()
    sys.stdout = orig_stdout

def init_webdriver():
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-tools")
        chrome_options.add_argument("--no-zygote")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
        chrome_options.add_argument(f"--data-path={mkdtemp()}")
        chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
        chrome_options.add_argument("--remote-debugging-pipe")
        chrome_options.add_argument("--verbose")
        chrome_options.add_argument("--log-path=/tmp")
        chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

        service = Service(
            executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver",
            service_log_path="/tmp/chromedriver.log"
        )

        return webdriver.Chrome(
            service=service,
            options=chrome_options
        )
    except Exception as exception:
        print(f"Error when initializing webdriver: {exception}\n")

def init_symbols_list(quantity=1000):
    symbols_list = None
    with open("./stocks_list.txt",'r') as file:
        symbols_list = file.read()

    return symbols_list.split('\n')[:quantity]

# Fetch curr price of symbol using webdriver
def fetch_symbol_curr_price(driver, symbol):
    try:
        # We try Google first
        driver.get(f"https://www.google.com/search?client=ubuntu-sn&channel=fs&q={symbol}+stock+price")
        # This is for after hours price (when market is closed): ".qFiidc > span:nth-child(3)"
        elem = driver.find_element(By.CSS_SELECTOR , ".qFiidc > span:nth-child(3)") #after hours price
        return float(elem.text.replace(',', ''))
    except:
        try:
            # If it fails on Google, try Yahoo finance
            driver.get(f"https://finance.yahoo.com/quote/{symbol}/")
            # This is for curr price (or closed price when market is closed): ".livePrice > span:nth-child(1)"
            # This is for after hours price (when market is closed): "fin-streamer.price > span:nth-child(1)"
            elem = driver.find_element(By.CSS_SELECTOR , "fin-streamer.price > span:nth-child(1)")
            return float(elem.text.replace(',', ''))
        except:
            try:
                # If it fails on Yahoo, try CNBC
                driver.get(f"https://www.cnbc.com/quotes/{symbol}")
                # This is for after hours price (when market is closed): ".QuoteStrip-extendedDataContainer > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)"
                elem = driver.find_element(By.CSS_SELECTOR , ".QuoteStrip-extendedDataContainer > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)")
                return float(elem.text.replace(',', ''))
            except:
                return None
        
def fetch_symbol_last_price(symbol, start_date, end_date):
    try:
        hData = si.get_data(symbol, start_date=start_date, end_date=end_date, index_as_date = False, interval="1d")
        return round(float(hData['close'].iloc[-1]), 2)
    except: 
        return None

def process_symbols(driver, symbols, log_file_path):
    curr_prices_failed = []
    last_prices_failed = []
    curr_vs_last_perc = {}

    todayDt = datetime.now()
    fiveDaysAgoDt = todayDt - relativedelta(days=5)
    today = todayDt.strftime('%m/%d/%Y')
    fiveDaysAgo = fiveDaysAgoDt.strftime('%m/%d/%Y')

    # Iterate through each symbol and calculate percentage drops/gains
    # Currently, only implementing the last closed value vs curr after hours value.
    for symbol in symbols:
        curr_price = fetch_symbol_curr_price(driver, symbol)
        last_price = fetch_symbol_last_price(symbol, fiveDaysAgo, today)
        if curr_price == None:
            curr_prices_failed.append(symbol)
        elif last_price == None:
            last_prices_failed.append(symbol)
        else:
            curr_vs_last_perc[symbol] = round(((curr_price / last_price) - 1) * 100, 2)

    # If we couldn't gather a price from a symbol, log it        
    orig_stdout = sys.stdout
    logs_file_instance = open(log_file_path, "a")
    sys.stdout = logs_file_instance

    if len(curr_prices_failed) > 0:
        print("Symbols whose current price couldn't be fetched:")
        print(f"{', '.join(curr_prices_failed)}\n")

    if len(last_prices_failed) > 0:
        print("Symbols whose last price couldn't be fetched:")
        print(f"{', '.join(last_prices_failed)}\n")

    logs_file_instance.close()
    sys.stdout = orig_stdout

    return curr_vs_last_perc

def log_symbols_results(results, results_file_path):
    sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))

    orig_stdout = sys.stdout
    logs_file_instance = open(results_file_path, "a")
    sys.stdout = logs_file_instance

    for symbol in sorted_results:
        print(f"{symbol}\t\t{sorted_results[symbol]}%")

    logs_file_instance.close()
    sys.stdout = orig_stdout

def run_program():    
    init_log_file(LOGS_FILE_PATH)
    driver = init_webdriver()
    symbols_list = init_symbols_list()
    results = process_symbols(driver, symbols_list, LOGS_FILE_PATH)
    log_symbols_results(results, LOGS_FILE_PATH)
    driver.quit()
    send_email(LOGS_FILE_PATH)


def lambda_handler(event, context):
    try: 
        run_program()
    except Exception as exception:
        print(f"Overall Error in lambda_handler: {exception}\n")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__ == "__main__":
    lambda_handler(None, None)