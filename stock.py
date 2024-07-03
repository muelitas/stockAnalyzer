#Python packages (in alphabetical order)
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os

#Third party packages (in alphabetical order)
import pandas as pd
from yahoo_fin.stock_info import get_data

# Custom modules / packages
import _config

class Stock():
  def __init__(self, symbol: str, parentDir: str ) -> None:
    self.symbol = symbol
    self.dir = os.path.join(parentDir, symbol)
    # h stands for historical
    self.hDataPath = os.path.join(self.dir, _config.STOCK_H_DATA_FILE_NAME)
    self.metricsPath = os.path.join(self.dir, _config.STOCK_METRICS_FILE_NAME)

  def checkDir(self) -> str | None:
    if not os.path.exists(self.dir):
      os.mkdir(self.dir)
      return None
    
    if not os.path.isdir(self.dir):
      msg = f"The path '{self.dir}' is not a directory but the path exists. "
      msg += "Please make sure to investigate. Skipping stock."
      return msg

  def __downloadHistoricalData(self):
    # Get start and end dates (today and x year(s) ago)
    numOfYears = _config.H_DATA_YEARS
    todayDt = datetime.now()
    xYearsAgoDt = todayDt - relativedelta(years=numOfYears)
    today = todayDt.strftime('%m/%d/%Y')
    xYearsAgo = xYearsAgoDt.strftime('%m/%d/%Y')

    # NOTE: get_data is not end_date inclusive
    hData = get_data(self.symbol, start_date=xYearsAgo, end_date=today, index_as_date = False, interval="1d")
    hData['date'] = hData['date'].astype(str)
    # Column headers are: open, high, low, close, adjclose, volume and ticker
    hData['highLowAvg'] = (hData['high'] + hData['low']) / 2
    hData.to_csv(self.hDataPath, index=False)

  def __updateHistoricalData(self):
    hData = pd.read_csv(self.hDataPath)
    
    hDataLastDateRaw = hData['date'].loc[hData.index[-1]]
    hDataLastDateDt = datetime.strptime(hDataLastDateRaw, '%Y-%m-%d')
    hDataLastDate = hDataLastDateDt.strftime('%m/%d/%Y')
    todayDt = datetime.now()
    today = todayDt.strftime('%m/%d/%Y')

    hDataToAppend = get_data(self.symbol, start_date=hDataLastDate, end_date=today, index_as_date = False, interval="1d")
    hDataToAppend['date'] = hDataToAppend['date'].astype(str)
    hDataToAppend['highLowAvg'] = (hDataToAppend['high'] + hDataToAppend['low']) / 2

    hDataUpdated = hData
    hDataUpdated[0:len(hData)-len(hDataToAppend)] = hData[len(hDataToAppend):]
    hDataUpdated[len(hData)-len(hDataToAppend):] = hDataToAppend[0:]
    hDataUpdated.to_csv(self.hDataPath, index=False)

  def processHistoricalData(self):
    if not os.path.exists(self.hDataPath):
      self.__downloadHistoricalData()
    else:
      self.__updateHistoricalData()