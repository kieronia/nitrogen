#if yo a complete skid with no clue on whats going on because you just want free discord nitro realise this has like a super small chance of working but anyways heres some setup help - download the latest version of python
import os
os.system("pip install --upgrade pip aiohttp aiofiles requests colorama") # dep install
os.system("cls")
import requests
import time
import string 
from colorama import init, Fore, Back, Style
from random import *
init(convert=True)
import threading # added harvey298 21/9/2020
import asyncio # added harvey298 21/9/2020
from datetime import datetime # added harvey298 21/9/2020

os.system("title Kieronia's Nitro Gen - Changing my name does not make you a programmer - Adding proxy support if this gets any attention lol - Added multithreading (Harvey298)")

characters = string.ascii_letters +  string.digits 
 

print(f"""
{Fore.BLUE}        ___  __   __   __   ___                    __      __           __   ___  {Fore.CYAN}     
 |\ | |  |  |__) /  \ / _` |__  |\ |     /\  |\ | |  \    /  \ \_/ \ / / _` |__  |\ | 
{Fore.BLUE} | \| |  |  |  \ \__/ \__> |___ | \|    /~~\ | \| |__/    \__/ / \  |  \__> |___ | \| 
                                                                                     
""")         



# File writing

async def filewrite(gift):
        try:
            with open('Vailds.txt','a+') as txt:              
                 txt.write("\nhttps://discord.gift/" + gift)
        except ValueError:
            print(f"{Fore.RED}[-] Failed to Write to Vailds.txt")

async def invalidfilewrite(gift):
        try:
            with open('invailds.txt','a+') as txt:              
                 txt.write("\nhttps://discord.gift/" + gift)
        except ValueError:
            print(f"{Fore.RED}[-] Failed to Write to invailds.txt")

async def failedcheckfilewrite(gift):
        try:
            with open('FailedToCheck.txt','a+') as txt:              
                 txt.write("\n" + gift)
        except ValueError:
            print(f"{Fore.RED}[-] Failed to Write to FailedToCheck.txt")

# Nitro Code gen

# Rechecker

async def recheck(gift):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{Fore.CYAN}[?] Retesting discord.gift/{gift.upper()} | {current_time}")
    r = requests.get(f"https://ptb.discordapp.com/api/v6/entitlements/gift-codes/{gift}")
    if r.status_code == 404:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{Fore.RED}[-] discord.gift/{gift.upper()} - Invalid (Rechecked) | {current_time}")
        await invalidfilewrite(gift) # comment this out to remove invalid logging
    elif r.status_code == 429:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{Fore.RED}[-] discord.gift/{gift.upper()} - Ratelimited - Skipping and Waiting 10 seconds | {current_time}")
        await failedcheckfilewrite(gift)
        time.sleep(10)
    elif r.status_code == 200: 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{Fore.GREEN}[-] discord.gift/{gift.upper()} -Valid Code - Saved to valid.txt | {current_time}")
        await filewrite(gift)


# Main code checker

async def gen():
    gift = "".join(choice(characters) for x in range(randint(16, 16))) #change 24 , 24 16, 16 if it's 16 idk
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"{Fore.CYAN}[?] Testing discord.gift/{gift.upper()} | {current_time}")
    r = requests.get(f"https://ptb.discordapp.com/api/v6/entitlements/gift-codes/{gift}")
    if r.status_code == 404:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{Fore.RED}[-] discord.gift/{gift.upper()} - Invalid | {current_time}")
        await invalidfilewrite(gift) # comment this out to remove invalid logging
    elif r.status_code == 429:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{Fore.RED}[-] discord.gift/{gift.upper()} - Ratelimited - Rechecking in 10 seconds | {current_time}")
        time.sleep(10)
        await recheck(gift)
    elif r.status_code == 200: 
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"{Fore.GREEN}[-] discord.gift/{gift.upper()} -Valid Code - Saved to valid.txt | {current_time}")
        # harvey298's code:
        await filewrite(gift)


# Loop that keeps it going

while True:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gen())
    time.sleep(6)
