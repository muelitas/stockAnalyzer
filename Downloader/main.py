# #Python packages (in alphabetical order)
import argparse
# from collections import deque
from configparser import ConfigParser
# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# import os
# import sys

# #Third party packages (in alphabetical order)
# import pandas as pd
# from yahoo_fin.stock_info import get_data

parser = argparse.ArgumentParser(description="Serves as a stocks' historical data downloader")
parser.add_argument("--config", dest = "config_path", default = "", help="Path to config (.ini) file")
args = parser.parse_args()

# configExtension = ".ini"

# if args.config_path == "":
#   print(f"Please provide the path to your configuration '{configExtension}' file")
#   sys.exit()

# if not os.path.exists(args.config_path):
#   print(f"Provided config file does not exist")
#   sys.exit()

# if not os.path.isfile(args.config_path):
#   print("The provided configuration path does not lead to a file")
#   sys.exit()

# if not args.config_path.endswith(configExtension):
#   print(f"Provided config file must have '{configExtension}' extension")
#   sys.exit()

# Get configuration attributes
config = ConfigParser()
config.read(args.config_path)
numOfYearsRaw = config.get('main', 'years')
symbolsRaw = config.get('main', 'symbols')
downloadDir = config.get('main', 'download_dir')

print(numOfYearsRaw, symbolsRaw, downloadDir)

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
