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

def numv(phone_number):
    try:
        number = phone_number[1:]
        url = "https://lookify.io/api/v2/lookup"
        data = {"number": number}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=data, headers=headers, verify=False)
        if response.status_code == 200:
            result = response.json()
            details = result.get("response", {}).get("details", {})
            carrier = details.get("carrier")
            number_type = details.get("number_type")
            print(f"{y}Number : {o}|{number}| {g}Carrier : {carrier} {o}| {c}Type : {number_type} {o}")
            
            if 'T-MOBILE' in carrier.upper() or 'VERIZON' in carrier.upper():
                with open('VALID.txt', 'a') as f:
                    f.write(f"{number}|{carrier}|{number_type}\n")
            else:
                with open('others.txt', 'a') as f:
                    f.write(f"{number}|{carrier}|{number_type}\n")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    try:
        # Clear console screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{y} Carrier - Lookup  | {c}https://github.com/idhin\n")
        
        # Read phone numbers from file
        with open(input(f'{y}List:~# {o}'), 'r') as file:
            phone_numbers = file.read().splitlines()
        
        # Create a thread pool with a reasonable number of threads (adjust as needed)
        num_threads = min(16, len(phone_numbers))
        pool = ThreadPool(num_threads)
        pool.map(numv, phone_numbers)
        pool.close()
        pool.join()
        
        time.sleep(5)
    except Exception as e:
        print(f"Error: {e}")
