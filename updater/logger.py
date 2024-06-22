import os, sys

pathToAppend = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils')
sys.path.append(pathToAppend)

# Custom packages, modules, files, etc. (in alphabetical order)
from _logger import Logger as _Logger

class Logger(_Logger):
  def __init__(self) -> None:
    super().__init__()
    pass

sys.path.remove(pathToAppend)
