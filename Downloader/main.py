# #Python packages (in alphabetical order)
import argparse
# from collections import deque
from configparser import ConfigParser
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# import os

# #Third party packages (in alphabetical order)
# import pandas as pd
# from yahoo_fin.stock_info import get_data

# Custom modules / packages
from validator import Validator

configExtension = ".ini"

parser = argparse.ArgumentParser(description="Serves as a stocks' historical data downloader")
parser.add_argument("--config", dest = "config_path", default = "", help=f"Path to config ({configExtension}) file")
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

validator.validateDownloadDir(downloadDir)

# print(numOfYearsRaw, symbolsRaw, downloadDir)
# print(sys.path)

# # Parse number of years from string to integer
# numOfYears = int(numOfYearsRaw)
# # Remove white spaces and double quotes; set all to lower case; transform string to list
# symbols = symbolsRaw.replace(" ", "").replace("\"", "").lower().split(",")

# # Get start and end dates (today and x year(s) ago)
# dtEndDate = datetime.now()
# dtStartDate = dtEndDate - relativedelta(years=numOfYears)
# endDate = dtEndDate.strftime('%m/%d/%Y')
# startDate = dtStartDate.strftime('%m/%d/%Y')

# symbolsHash = {}

# # Iterate through each symbol
# for symbol in symbols:
#   # Get stock's historical data
#   stockData = get_data(symbol, start_date="6/1/2024", end_date=endDate, index_as_date = True, interval="1d")
#   print(stockData)

#   q = deque()
#   for idx in stockData.index:
#     q.append((stockData['high'][idx] + stockData['low'][idx]) / 2)

#   print(q)
#   symbolsHash[symbol] = q
  
# print(symbolsHash)
# # df = pd.DataFrame()
# # df[symbol.lower()] = stockData['average']
# # print(df.head(5))
# #   print(symbol)
# print("\033[93m Try programiz.pro \033[0m")
