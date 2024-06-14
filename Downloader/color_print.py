import os, sys

pathToAppend = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils')
sys.path.append(pathToAppend)

# Custom packages, modules, files, etc. (in alphabetical order)
from _color_print import ColorPrint as _ColorPrint

class ColorPrint(_ColorPrint):
  def __init__(self) -> None:
    super().__init__()
    pass

sys.path.remove(pathToAppend)
