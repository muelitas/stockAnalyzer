from datetime import datetime
import os

from _color_print import ColorPrint
from _path_validator import PathValidator
pathToAppend = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils')

class Logger:
  """Logs logs logs"""
  def __init__(self) -> None:
    self.logFilePath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs', 'logs.txt')
    self.path_validator = PathValidator()
    self.printer = ColorPrint()
    self.validateLogFilePath()

  def validateLogFilePath(self) -> None:
    """Validate path where logs will be saved"""
    fileLabel = "logs file"
    self.path_validator.pathIsSet(self.logFilePath, fileLabel)
    self.path_validator.pathExists(self.logFilePath, fileLabel)
    self.path_validator.pathIsFile(self.logFilePath, fileLabel)
    self.path_validator.pathHasValidExtension(self.logFilePath, fileLabel, ['txt'])

  def logMsg(self, textToLog: str, excludeLog: None | bool, colorOfPrint: None | str ) -> None:
    """Handle log and/or print"""
    if excludeLog == True or excludeLog == None:
      self.printMsg(textToLog, colorOfPrint)

    if excludeLog == False or excludeLog == None:
      self.saveLog(textToLog)

  def saveLog(self, textToLog: str) -> None:
    """Save given text/prompt to log file"""
    with open(self.logFilePath, "a") as logFile:
        dtNow = datetime.now()
        now = dtNow.strftime('%B %d, %Y; %I:%M:%S %p')
        logFile.write(f"[{now}] {textToLog}\n")

  def printMsg(self, msgToPrint: str, colorOfPrint: None | str) -> None:
    """Use printer class to display message in terminal"""
    self.printer.simplePrint(msgToPrint, colorOfPrint)

  
    
