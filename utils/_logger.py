from datetime import datetime

from utils._path_validator import PathValidator
from utils._printer import Printer

class Logger():
  """Logs logs logs"""
  def __init__(self, logFilePath: str, validFileExtensions: list) -> None:
    self.logFilePath = logFilePath
    self.path_validator = PathValidator()
    self.printer = Printer()
    self.__validateLogFilePath(validFileExtensions)

  def __validateLogFilePath(self, validFileExtensions: list) -> None:
    """Validate path where logs will be saved"""
    fileLabel = "logs file"
    self.path_validator.pathIsSet(self.logFilePath, fileLabel)
    self.path_validator.pathExists(self.logFilePath, fileLabel)
    self.path_validator.pathIsFile(self.logFilePath, fileLabel)
    self.path_validator.pathHasValidExtension(self.logFilePath, fileLabel, validFileExtensions)

  def logMsg(self, textToLog: str, excludeLog: None | bool, colorOfPrint: None | str ) -> None:
    """Handle log and/or print"""
    if excludeLog == True or excludeLog == None:
      self.__printMsg(textToLog, colorOfPrint)

    if excludeLog == False or excludeLog == None:
      self.__saveLog(textToLog)

  def __saveLog(self, textToLog: str) -> None:
    """Save given text/prompt to log file"""
    with open(self.logFilePath, "a") as logFile:
        dtNow = datetime.now()
        now = dtNow.strftime('%B %d, %Y; %I:%M:%S %p')
        logFile.write(f"[{now}] {textToLog}\n")

  def __printMsg(self, msgToPrint: str, colorOfPrint: None | str) -> None:
    """Use printer class to display message in terminal"""
    self.printer.simplePrint(msgToPrint, colorOfPrint)

  
    
