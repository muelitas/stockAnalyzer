class ColorPrint:
  """To handle and display messages in terminal in different colors/states"""
  def __init__(self) -> None:
    self.yellow = '\033[93m'
    self.cyan = '\033[96m'
    self.red = '\033[91m'
    self.endc = '\033[0m'

  def errPrint(self, msgToPrint: str) -> None:
    """Print message in red (error)"""
    print(f"{self.red}[ERROR]: {msgToPrint}{self.endc}")

  def warnPrint(self, msgToPrint: str) -> None:
    """Print message in yellow (warning)"""
    print(f"{self.yellow}[WARNING]: {msgToPrint}{self.endc}")

  def infoPrint(self, msgToPrint: str) -> None:
    """Print informational (cyan) message"""
    print(f"{self.cyan}[INFO]: {msgToPrint}{self.endc}")