from bs4 import BeautifulSoup
from termcolor import colored
import httpx
import trio
import os
from argparse import ArgumentParser
from datetime import datetime
import time
import importlib
import pkgutil
import hashlib
import re
import sys
import string
import random
import json
from uuid import uuid4


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from otpbomber.instruments import TrioProgress

__version__ = "1"


def import_submodules(package, recursive=True):
    """Get all the submodules"""
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


def get_functions(modules,args=None):
    """Transform the modules objects to functions"""
    websites = []

    for module in modules:
        if len(module.split(".")) > 3 :
            modu = modules[module]
            site = module.split(".")[-1]
            websites.append(modu.__dict__[site])
    return websites


def credit():
    """Print Credit"""
    print('Twitter : @asharbinkhalil')
    print('Github : https://github.com/asharbinkhalil/otpbomber')
    print('Repositry Structure Inspired by https://github.com/megadose/holehe')


def print_result(data,phone,start_time,websites,clear_screen):
    def print_color(text,color):
        return(colored(text,color))

    description = print_color("[+] OTP Sent","green") + ","  + "," + print_color(" [x] Rate limit","yellow") + "," + print_color(" [!] Error","red")

    print("*" * (len(phone) + 6))
    print("   " + phone)
    print("*" * (len(phone) + 6))
    if clear_screen:
        print("\033[H\033[J")
    credit()

    for results in data:
        if results["rateLimit"]==True:
            websiteprint = print_color("[x] " + results["domain"], "yellow")
            print(websiteprint)
        elif results["sent"] == False and results["error"] == False:
            websiteprint = print_color("[-] " + results["domain"], "magenta")
            print(websiteprint)
        elif results["sent"] == True and results["error"] == False:
            websiteprint = print_color("[+] " + results["domain"], "green")
            print(websiteprint)
        elif results["error"] == True:
            websiteprint = print_color("[!] " + results["domain"], "red")
            print(websiteprint)

    print("\n" + description)
    print(str(len(websites)) + " websites checked in " +
          str(round(time.time() - start_time, 2)) + " seconds")


async def launch_module(module,phone, client, out):
    try:
        await module(phone, client, out)
    except Exception:
        name=str(module).split('<function ')[1].split(' ')[0]
        out.append({"name": name,"domain":name,"frequent_rate_limit":False, "rateLimit": False, "sent": False,'error':True})


async def maincore():
    parser = ArgumentParser(description=f"wtf v{__version__}")
    parser.add_argument("phone", nargs='+', metavar='PHONE', help="Target phone number")
    parser.add_argument("--no-clear", default=False, required=False,action="store_true",dest="noclear",help="Do not clear the terminal to display the results")
    parser.add_argument("--site", default=None, required=False,action="store",dest="site",help="Check only one site")



    args = parser.parse_args()
    credit()

    phone = args.phone[0]
    clear_screen = not args.noclear
    onlysite=args.site



    # Import Modules
    modules = import_submodules("otpbomber.modules")

    websites = get_functions(modules, args)

    if onlysite:
        onlysite=[onlysite]
        websites = [site for site in websites if site.__name__  in onlysite]
    else:
        websites = [site for site in websites if site.__name__ not in []]

    # Start time
    start_time = time.time()

    client = httpx.AsyncClient(timeout=10)

    out = []
    instrument = TrioProgress(len(websites))

    trio.lowlevel.add_instrument(instrument)  # Add instrument once here

    async with trio.open_nursery() as nursery:
        for website in websites:
            nursery.start_soon(launch_module, website, phone, client, out)

    # Remove instrument after all tasks are done
    trio.lowlevel.remove_instrument(instrument)
    await client.aclose()
    
    print_result(out, phone, start_time, websites,clear_screen)

def main():
    trio.run(maincore)

if __name__ == "__main__":
    main()
