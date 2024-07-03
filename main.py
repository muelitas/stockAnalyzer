#Python packages (in alphabetical order)
import argparse
from datetime import datetime
import sys

#Third party packages (in alphabetical order)
from yahoo_fin.stock_info import get_data

# Custom modules / packages (in alphabetical order)
import _config
from stock import Stock
from utils._logger import Logger
from utils._path_validator import PathValidator
from utils._printer import Printer

printer = Printer()
generalLog = Logger(_config.LOGS_FILE_PATH, ['txt'])
dailyStocksLog = Logger(_config.DAILY_STOCKS_LOG_FILE_PATH, ['txt'])
pathValidator = PathValidator()

parser = argparse.ArgumentParser(description="Serves as a stocks' historical data downloader")
parser.add_argument("-s", "--stocks", dest = "stock_list", default = None, help="List of stocks to process (as a string)")
parser.add_argument("-d", "--delimiter", dest = "delimiter", default = None, help="Delimiter separating stocks in 'stringed' list")
args = parser.parse_args()

#TODO how to deal with invalid stocks / typos?
# region Validate Terminal Args
if (not args.stock_list):
  printer.simplePrint("A list of stocks must be provided (i.e. -s 'META,PANW,UNH').", "red")
  sys.exit()

#TODO using regex, determine if there is a character in stocks that is not a alphabetical, if there is one, require delimiter.
if (not args.delimiter):
  printer.simplePrint("The delimiter separating the stocks must be provided (i.e. -d ',', '|', etc.)", "red")
  sys.exit()

# endregion

# region Ensure Market Is Open
weekDayNum = datetime.today().weekday()

if (weekDayNum == 5):
  printer.simplePrint("Today is Saturday! Cheers!!", 'cyan')
  sys.exit()

if (weekDayNum == 6):
  printer.simplePrint("Today is Sunday! Cheers!!", 'cyan')
  sys.exit()

# Try to get data to determine if market is closed due to holiday
try:
  dtTodayDate = datetime.now()
  todayDate = dtTodayDate.strftime('%m/%d/%Y')
  symbolData = get_data('AAPL', start_date=todayDate, end_date=todayDate, index_as_date = False, interval="1d")
except Exception as e:
  #After a few runs, this error seems to be returned when there is not data in the stock market (i.e. stock market is closed)
  if e == 'timestamp':
    msg = 'Stock market seems to be closed today due to a holiday. Stopping program...'
    generalLog.logMsg(msg, False, 'cyan')
    sys.exit()

# endregion

stocksDir = _config.STOCKS_DOWNLOAD_DIR
pathValidator.pathExists(stocksDir, "Stocks Download Directory")
pathValidator.pathIsDir(stocksDir, "Stocks Download Directory")

stocks = args.stock_list.lower().replace(" ", "").split(args.delimiter)
# TODO add today's stocks to 'daily stocks' log file
for stockSymbol in stocks:
  stock = Stock(stockSymbol, stocksDir)
  
  checkVerdictMsg = stock.checkDir()
  if checkVerdictMsg:
    generalLog.logMsg(checkVerdictMsg, False, 'red')
    continue

  stock.processHistoricalData()
  #TODO process and save metrics

#TODO we need to run this program at 5 am or 6 am so that get_data returns the last stock info

msg = "Historical Data has been downloaded and/or updated"
generalLog.logMsg(msg, None, 'green')