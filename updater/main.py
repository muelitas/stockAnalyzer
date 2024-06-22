#Python packages (in alphabetical order)
import argparse
from configparser import ConfigParser
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import sys

#Third party packages (in alphabetical order)
import pickle
from yahoo_fin.stock_info import get_data

# Custom modules / packages
from color_print import ColorPrint
from logger import Logger
from validator import Validator

# TODO maybe add check: if not 4pm ET yet, recommend user to wait until after to run this program
try:
  configExtension = ".ini"

  printer = ColorPrint()
  log = Logger()

  parser = argparse.ArgumentParser(description="Update already downloaded historical data")
  parser.add_argument("--config", dest = "config_path", default = "", help=f"Path to config ({configExtension}) file")
  args = parser.parse_args()

  #Validate given configuration file
  validator = Validator()
  validator.validateConfigPath(args.config_path, [configExtension])

  # Get configuration attributes
  config = ConfigParser()
  config.read(args.config_path)
  pathToHistoricalData = config.get('main', 'downloaded_data_file')

  validator.validateHistoricalDataFilePath(pathToHistoricalData, ['pickle'])

  # Get stocks' symbols
  file = open(pathToHistoricalData, 'rb')
  hData = pickle.load(file) # short for Historical Data
  file.close()
  stocksSymbols = list(hData.keys())

  # Get start and end dates (today and tomorrow)
  dtStartDate = datetime.now()
  dtEndDate = dtStartDate + relativedelta(days=1)
  startDate = dtStartDate.strftime('%m/%d/%Y')
  endDate = dtEndDate.strftime('%m/%d/%Y')
  dummyDateDt = dtStartDate - relativedelta(days=1)
  dummyDate = dummyDateDt.strftime('%m/%d/%Y')
  # Get each symbol today's info
  symbolsCurrPrices = {}
  for symbol in stocksSymbols:
    # NOTE: get_data is not end_date inclusive
    symbolData = get_data(symbol, start_date=startDate, end_date=endDate, index_as_date = False, interval="1d")

    if len(symbolData) > 1:
      #TODO create exception for this scenario as well
      printer.simplePrint(f"More than one result returned for stock: {symbol}", 'red')
      sys.exit()
    
    todayAvgVal = (symbolData['high'][0] + symbolData['low'][0]) / 2
    
    # Update symbol's average-values-queue
    q = hData[symbol]
    q.popleft()
    q.append(todayAvgVal)
    hData[symbol] = q

  # # Save updated historical data in pickle file
  downloadFilePath = os.path.join(pathToHistoricalData)
  fileInstance = open(downloadFilePath, 'wb')
  pickle.dump(hData, fileInstance)
  fileInstance.close()
  log.logMsg(f"[Updater] Historical data successfully updated and saved in {downloadFilePath}", None, 'green')

except Exception as e:
  # TODO create symbolNonWorkday Exception and handle it here accordingly
  log.logMsg(f"[Updater] An exception occurred. Msg: {e}", None, 'red')