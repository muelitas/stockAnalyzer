# Python packages (in alphabetical order)
import os
import sys

# Custom packages, modules, files, etc. (in alphabetical order)
from utils._printer import Printer

class PathValidator():
  """Serve as a validator for a given file path"""

  def __init__(self) -> None:
    self.colorPrint = Printer()

  def pathIsSet(self, pathToCheck: str | None, pathLabel: str) -> None:
    """Ensure given path is set (not a falsy value)"""
    if not pathToCheck:
      self.colorPrint.simplePrint(f"Please provide path of '{pathLabel}'", 'red')
      sys.exit()
    
  def pathExists(self, pathToCheck: str, pathLabel: str) -> None:
    """Ensure given path exists"""
    if not os.path.exists(pathToCheck):
      self.colorPrint.simplePrint(f"Provided '{pathLabel}' does not exist", 'red')
      sys.exit()

  def pathIsFile(self, pathToCheck: str, pathLabel: str) -> None:
    """Ensure given path is a file"""
    if not os.path.isfile(pathToCheck):
      self.colorPrint.simplePrint(f"Path to the '{pathLabel}' does not lead to a file", 'red')
      sys.exit()

  def pathIsDir(self, pathToCheck: str, pathLabel: str) -> None:
    """Ensure given path is a directory"""
    if not os.path.isdir(pathToCheck):
      self.colorPrint.simplePrint(f"Path to the '{pathLabel}' does not lead to a directory", 'red')
      sys.exit()

  def pathHasValidExtension(self, pathToCheck: str, pathLabel: str, validExtensions: list) -> None:
    """Ensure extension of given path is present in the given valid extensions"""
    # Set valid extensions to lowercase
    extensionsInLower = [x.lower() for x in validExtensions]
    pathInLower = pathToCheck.lower()
    
    for extension in extensionsInLower:
      if pathInLower.endswith(extension):
        return
    
    self.colorPrint.simplePrint(f"Provided '{pathLabel}' must have one one of the following extensions: {validExtensions}", 'red')
    sys.exit()

  def dirIsEmptyWithWarn(self, pathToCheck: str, pathLabel: str):
    """Ensure given path to directory is empty"""
    userStopped = False
    if not len(os.listdir(pathToCheck)) == 0:
      self.colorPrint.simplePrint(f"The given '{pathLabel}' is not empty; files might get overwritten.\n", 'yellow')
      userInput = input("Would you like to continue? [Y/n]")
      userStopped = userInput.lower() == 'n'
    
    if userStopped:
      print("Ceasing to live...")
      sys.exit()

    return
