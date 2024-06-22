#Python packages (in alphabetical order)
import argparse
from collections import deque
from configparser import ConfigParser
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os

#Third party packages (in alphabetical order)
import pickle
from yahoo_fin.stock_info import get_data

# Custom modules / packages
from validator import Validator
from color_print import ColorPrint

# TODO maybe add check: if not 4pm ET yet, recommend user to wait until after to run this program

configExtension = ".ini"
downloadFileName = "stocksHistoricalData.pickle"

printer = ColorPrint()

parser = argparse.ArgumentParser(description="Serves as a stocks' historical data downloader")
parser.add_argument("--config", dest = "config_path", default = None, help=f"Path to config ({configExtension}) file")
args = parser.parse_args()

#Validate given configuration file
validator = Validator()
validator.validateConfigPath(args.config_path, [configExtension])

# Get configuration attributes
config = ConfigParser()
config.read(args.config_path)
numOfYearsRaw = config.get('main', 'years')
symbolsRaw = config.get('main', 'symbols')
downloadDir = config.get('main', 'download_dir')

# Validate and format config-provided values
validator.validateDownloadDir(downloadDir)
numOfYears = int(numOfYearsRaw)
symbols = symbolsRaw.replace(" ", "").replace("\"", "").lower().split(",")

# Get start and end dates (today and x year(s) ago)
dtEndDate = datetime.now()
dtStartDate = dtEndDate - relativedelta(years=numOfYears)
endDate = dtEndDate.strftime('%m/%d/%Y')
startDate = dtStartDate.strftime('%m/%d/%Y')

# Iterate through each symbol
symbolsHash = {}
for symbol in symbols:
  # Get stock's historical data
  # NOTE: get_data is not end_date inclusive
  stockData = get_data(symbol, start_date=startDate, end_date=endDate, index_as_date = True, interval="1d")

  q = deque()
  for idx in stockData.index:
    q.append((stockData['high'][idx] + stockData['low'][idx]) / 2)

  symbolsHash[symbol] = q

#Save historical data in pickle file
downloadFilePath = os.path.join(downloadDir, downloadFileName)
fileInstance = open(downloadFilePath, 'wb')
pickle.dump(symbolsHash, fileInstance)
fileInstance.close()
printer.simplePrint(f"Historical data successfully downloaded and saved in {downloadFilePath}", 'green')

