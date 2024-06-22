import os, sys

pathToAppend = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils')
sys.path.append(pathToAppend)

# Custom packages, modules, files, etc. (in alphabetical order)
from _path_validator import PathValidator

class Validator(PathValidator):
  def __init__(self) -> None:
    super().__init__()
    pass

  def validateConfigPath(self, configPath: str | None, validExtensions: list) -> None:
    """Validate path where updater configuration lives"""
    self.pathIsSet(configPath, "configuration file")
    self.pathExists(configPath, "configuration file")
    self.pathIsFile(configPath, "configuration file")
    self.pathHasValidExtension(configPath, "configuration file", validExtensions)

  def validateHistoricalDataFilePath(self, configPath: str | None, validExtensions: list) -> None:
    """Validate path to file where historical data is stored"""
    fileLabel = "historical data file"
    self.pathIsSet(configPath, fileLabel)
    self.pathExists(configPath, fileLabel)
    self.pathIsFile(configPath, fileLabel)
    self.pathHasValidExtension(configPath, fileLabel, validExtensions)

  #TODO move this to analyzer
  def validateChromeExecutablePath(self, configPath: str | None, validExtensions: list) -> None:
    """Validate path to chrome for testing executable path"""
    fileLabel = "chrome for testing executable file"
    self.pathIsSet(configPath, fileLabel)
    self.pathExists(configPath, fileLabel)
    self.pathIsFile(configPath, fileLabel)
    self.pathHasValidExtension(configPath, fileLabel, validExtensions)

  #TODO move this to analyzer
  def validateChromeDriverPath(self, configPath: str | None, validExtensions: list) -> None:
    """Validate path to chrome driver path"""
    fileLabel = "chrome driver file"
    self.pathIsSet(configPath, fileLabel)
    self.pathExists(configPath, fileLabel)
    self.pathIsFile(configPath, fileLabel)
    self.pathHasValidExtension(configPath, fileLabel, validExtensions)

sys.path.remove(pathToAppend)
