#if yo a complete skid with no clue on whats going on because you just want free discord nitro realise this has like a super small chance of working but anyways heres some setup help - download the latest version of python - tick anything to do with path n pip installs, and for the imports - open cmd and type "pip install requests" , "pip install ___" - These are modules and this will download them and allow you to use my program :)
import requests
import time
import string 
from colorama import init, Fore, Back, Style
import os
from random import *
init(convert=True)
os.system("title Kieronia's Nitro Gen - Changing my name does not make you a programmer - Adding proxy support and multithreading if this gets any attention lol")

characters = string.ascii_letters +  string.digits
gift = ""

print(f"""
{Fore.BLUE}        ___  __   __   __   ___                    __      __           __   ___  {Fore.CYAN}     
 |\ | |  |  |__) /  \ / _` |__  |\ |     /\  |\ | |  \    /  \ \_/ \ / / _` |__  |\ | 
{Fore.BLUE} | \| |  |  |  \ \__/ \__> |___ | \|    /~~\ | \| |__/    \__/ / \  |  \__> |___ | \| 
                                                                                     
""")

while True:
    if gift == "":
        gift = "".join(choice(characters) for x in range(randint(24, 24))) #change 24,24 to 16,16 if the code changes idk gift code things
    print(f"{Fore.CYAN}[?] Testing discord.gift/{gift.upper()}")
    r = requests.get(f"https://ptb.discordapp.com/api/v6/entitlements/gift-codes/{gift}")
    if r.status_code == 404:
        print(f"{Fore.RED}[-] discord.gift/{gift.upper()} - Invalid")
        gift = ""
    elif r.status_code == 429:
        print(f"{Fore.RED}[-] discord.gift/{gift.upper()} - Ratelimited - Waiting 10 seconds")
        time.sleep(9) #9 as theres a 1 sec delay anyway
    elif r.status_code == 200: 
        print(f"{Fore.GREEN}[-] discord.gift/{gift.upper()} -Valid Code - Saved to valid.txt")
        f = open("valids.txt", "a")
        f.write("https://discord.gift/"+gift)
        f.close()
        gift = ""
    time.sleep(1) #change this to whatever but you'll probably get ratelimited if you go any faster
