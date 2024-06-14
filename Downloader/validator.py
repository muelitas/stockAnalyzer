import os, sys

pathToAppend = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils')
sys.path.append(pathToAppend)

# Custom packages, modules, files, etc. (in alphabetical order)
from path_validator import PathValidator

class Validator(PathValidator):
  def __init__(self) -> None:
    super().__init__()
    pass

  def validateConfigPath(self, configPath: str | None, validExtensions: list) -> None:
    """Validate path where downloader configuration lives"""
    self.pathIsSet(configPath, "configuration file")
    self.pathExists(configPath, "configuration file")
    self.pathIsFile(configPath, "configuration file")
    self.pathHasValidExtension(configPath, "configuration file", validExtensions)

  def validateDownloadDir(self, downloadDir: str) -> None:
    """Validate folder where data will be downloaded to"""
    # For now, make sure dowload directory is created beforehand
    self.pathExists(downloadDir, "download directory")
    self.pathIsDir(downloadDir, "download directory")
    self.dirIsEmptyWithWarn(downloadDir, "download directory")

sys.path.remove(pathToAppend)
