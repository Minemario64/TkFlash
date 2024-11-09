from colorama import init, Fore, Back, Style

init()

class TkFlashError(Exception):
    colors = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    bgs = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
    brightnesses = [Style.DIM, Style.NORMAL, Style.BRIGHT]
    prefixes = {"error" : Fore.RED, "warning" : Fore.YELLOW, "question error" : Fore.CYAN, "timer error" : Fore.MAGENTA}
    def __init__(self, type, message):
        type = type.lower()
        prefix = self.prefixes[type]
        ending = Style.RESET_ALL
        self.message = f"{prefix}{message}{ending}"
        super().__init__(self.message)