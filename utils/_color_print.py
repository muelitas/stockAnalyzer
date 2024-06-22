class ColorPrint:
  """To handle and display messages in terminal in different colors/states"""
  def __init__(self) -> None:
    self.endc = '\033[0m'
    self.hashmap = {
      'red': {
        'color': '\033[91m',
        'label': '[ERROR]'
      },
      'green': {
        'color': '\033[92m',
        'label': '[SUCCESS]'
      },
      'yellow': {
        'color': '\033[93m',
        'label': '[WARNING]'
      },
      'cyan': {
        'color': '\033[96m',
        'label': '[INFO]'
      },
    }

  def simplePrint(self, msgToPrint: str, colorOfPrint: None | str) -> None:
    """Print message in the given color"""
    # TODO make sure we colorOfPrint; if we don't default to none and let user know; if None, print with default
    color, label = self.hashmap[colorOfPrint]['color'], self.hashmap[colorOfPrint]['label']
    print(f"{color}{label}: {msgToPrint}{self.endc}")
