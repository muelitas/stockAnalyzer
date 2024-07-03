class Printer():
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
      'blue': {
        'color': '\033[43m',
        'label': '[TODO]'
      },
    }

  def simplePrint(self, msgToPrint: str, colorOfPrint: None | str) -> None:
    """Print message in the given color"""
    # TODO make sure we check colorOfPrint value; if we don't default to none and let user know; if None, print with default
    colorOfPrint = colorOfPrint.lower()
    color, label = self.hashmap[colorOfPrint]['color'], self.hashmap[colorOfPrint]['label']
    print(f"{color}{label}: {msgToPrint}{self.endc}")
