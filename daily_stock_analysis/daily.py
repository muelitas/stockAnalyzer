# Python packages (in alphabetical order)
from datetime import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import pytz
import os
import smtplib
import sys

# Third party packages (in alphabetical order)
from yahooquery import Ticker

# TODO make an Emailer class so you can send email on lambda_handler exception with the error
# TODO add a symbol duplicate check
# TODO Add descriptions to all functions
# TODO use selenium for those that fail with yahoo query!
# TODO add variable that keeps track of errors; this way they can be displayed in the emailed file; log main exception and send email!
# TODO instead of a specific key, consider returning a string: 'pre', 'post' and 'regular' in determine_yahooquery_key()

class Stock:
    def __init__(self, path_to_stocks_file, path_to_log) -> None:
        # Path to file with list of stocks
        self.path_to_stocks_file = path_to_stocks_file
        # Path to file where info will be saved
        self.path_to_log = path_to_log
        # List to store errors
        self.errs = []
        # Number of tickers to fetch at a time from yahooquery
        self.yq_tickers_num_to_fetch = 10

    def send_email(self) -> None:
        """Send an email with an attachment"""
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
        with open(self.path_to_log,'rb') as file:
            message.attach(MIMEApplication(file.read(), Name="stocks.txt"))
        
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_app_password)
            server.sendmail(email_from, email_to.split(','), message.as_string())
            server.close()
            print('Email sent!\n')
        except Exception as e:
            raise Exception(f"Error when sending email: {repr(e)}")

    def init_log_file(self) -> None:
        """Ensure log file is ready to be used (overwrite/clean it if it already exists)"""
        orig_stdout = sys.stdout
        logs_file_instance = open(self.path_to_log, "w")
        sys.stdout = logs_file_instance
        print(f"{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n")
        logs_file_instance.close()
        sys.stdout = orig_stdout

    def init_symbols_list(self, quantity: int = 1000) -> None:
        """Display histogram of given data

        Parameters
        ----------
        quantity : int
            number of stocks to grab from the list (defaults to 1000)
        """
        symbols_list = None
        with open(self.path_to_stocks_file, 'r') as file:
            symbols_list = file.read()

        return symbols_list.split('\n')[:quantity]

    def determine_yahooquery_key(self) -> None:
        """Determine which percentage key to use for yahooquery API given the time of the day"""
        try:
            eastern = pytz.timezone('US/Eastern')
            x = datetime.now(eastern)

            # Post market (after 4pm and before 1am)
            if (x.hour >= 16 and x.hour < 24) or (x.hour >= 0 and x.hour < 1):
                return 'postMarketChangePercent'
            # Pre martket (before 9:30am and after 1am)
            elif (x.hour >= 1) and (x.hour < 9):
                return 'preMarketChangePercent'
            elif (x.hour == 9 and x.minute < 30):
                return 'preMarketChangePercent'
            # Anythin else, regular market hours
            else:
                return 'regularMarketChangePercent'
        except Exception as E:
            msg = f"An error occured when fetching yahooquery key: {repr(E)}"
            self.errs.append(msg)
            print(msg)

    def process_symbols(self, symbols: list) -> list:
        """Get symbol(s) percentage change since the last close; keep track of any failed fetches.

        Parameters
        ----------
            symbols : str
                tickers from which to get after-close percentages for

        Returns
        -------
            list
                it incorporates a dictionary of fetched percentages and a list of failures
        """
        failed = []
        processed = {} # Stores closed price vs after hours price difference in percentage
        i = 0

        while i < len(symbols):
            tickers = symbols[i : i + self.yq_tickers_num_to_fetch]
            i += self.yq_tickers_num_to_fetch
            percentage_key = self.determine_yahooquery_key()
            tickers_data = Ticker(tickers)
            for ticker in tickers:
                try:
                    percentage = round(tickers_data.price[ticker][percentage_key] * 100, 2)
                    processed[ticker] = percentage
                except:
                    failed.append(ticker)

        return [processed, failed]

    def log_failed_symbols(self, symbols: list) -> None:
        """Document those symbols that failed in the log file

        Parameters
        ----------
        symbols : list
            list of those symbols which data fetch failed
        """
        if len(symbols) == 0:
            return
        
        # If we couldn't gather a market percentage change for a symbol, log it        
        orig_stdout = sys.stdout
        logs_file_instance = open(self.path_to_log, "a")
        sys.stdout = logs_file_instance

        print("Symbols whose market percentage change fetch failed:")
        print(f"{', '.join(symbols)}\n")

        logs_file_instance.close()
        sys.stdout = orig_stdout

    def log_processed_symbols(self, symbols: dict) -> None:
        """Document symbols' percentage changes in the log file

        Parameters
        ----------
        symbols : dict
            symbols' tickers and their percentage change
        """
        sorted_symbols = dict(sorted(symbols.items(), key=lambda item: item[1]))

        orig_stdout = sys.stdout
        logs_file_instance = open(self.path_to_log, "a")
        sys.stdout = logs_file_instance

        for symbol in sorted_symbols:
            print(f"{symbol}\t{sorted_symbols[symbol]}%")

        logs_file_instance.close()
        sys.stdout = orig_stdout

    def log_errors(self) -> None:
        """Document all errors found during runtime"""
        orig_stdout = sys.stdout
        logs_file_instance = open(self.path_to_log, "a")
        sys.stdout = logs_file_instance

        print("Additional errors found on runtime:")
        for err in self.errs:
            print(f"- {err}")

        logs_file_instance.close()
        sys.stdout = orig_stdout

    def run_program(self) -> None:
        """Merely a handler to place the flow of commands"""
        self.init_log_file()
        symbols_list = self.init_symbols_list()
        [first_processed, failed] = self.process_symbols(symbols_list)
        self.log_failed_symbols(failed)
        processed = {**first_processed}
        self.log_processed_symbols(processed)
        self.log_errors()
        self.send_email()

def lambda_handler(event, context):
    try: 
        stock = Stock("./stocks_list.txt", "/tmp/text.txt")
        stock.run_program()
    except Exception as e:
        print(f"Overall Error in lambda_handler: {repr(e)}\n")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

if __name__ == "__main__":
    lambda_handler(None, None)