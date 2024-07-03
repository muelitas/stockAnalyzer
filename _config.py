import os

# Default values
__logsFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'general_logs.txt')
__dailyStocksLogFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'daily_stocks_log.txt')
__sotcksDownloadDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads', 'stocks')
__hDataYears = 5 # Specify the number of years of historical data to download

try:
  import _my_config

  # region If a different value is provided for any variable in '_my_config.py' file, use it
  if hasattr(_my_config, 'LOGS_FILE_PATH'):
    __logsFilePath = _my_config.LOGS_FILE_PATH

  if hasattr(_my_config, 'DAILY_STOCKS_LOG_FILE_PATH'):
    __dailyStocksLogFilePath = _my_config.DAILY_STOCKS_LOG_FILE_PATH

  if hasattr(_my_config, 'STOCKS_DOWNLOAD_DIR'):
    __sotcksDownloadDir = _my_config.STOCKS_DOWNLOAD_DIR

  if hasattr(_my_config, 'H_DATA_YEARS'):
    __hDataYears = _my_config.H_DATA_YEARS

  # endregion
except ImportError as e:
  pass

LOGS_FILE_PATH = __logsFilePath
DAILY_STOCKS_LOG_FILE_PATH = __dailyStocksLogFilePath
STOCKS_DOWNLOAD_DIR = __sotcksDownloadDir
H_DATA_YEARS = __hDataYears

STOCK_H_DATA_FILE_NAME = 'hData.csv' # H stands for historical
STOCK_METRICS_FILE_NAME = 'metrics.pickle'
