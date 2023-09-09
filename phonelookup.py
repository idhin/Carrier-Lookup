import requests
import time
import random
import json
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Style, init
import urllib3
import os

# Suppress SSL-related warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize colorama for colored output
init(autoreset=True)
r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL
