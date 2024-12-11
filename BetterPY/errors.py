import inspect
import sys

ER_BLUE =   "\033[38;2;0;0;255m"
ER_YELLOW = "\033[38;2;255;255;0m"
ER_ORANGE = "\033[38;2;255;165;0m"
ER_RED =    "\033[38;2;255;0;0m"
ER_WHITE =  "\033[38;2;255;255;255m"

# inspect dosent work omg
def infoWarning(text):  print(f"{ER_BLUE}@{inspect.stack()[-2].function} | Warning: {text}{ER_WHITE}")
def ErrorWarning(text): print(f"{ER_YELLOW}@{inspect.stack()[-2].function} | Error: {text}{ER_WHITE}")
def CritcalWarning(text): print(f"{ER_ORANGE}@{inspect.stack()[-2].function} | Critcal: {text}{ER_WHITE}")
def FatileWarning(text): print(f"{ER_RED}@{inspect.stack()[-2].function} | Fatile: {text}{ER_WHITE}"); sys.exit()