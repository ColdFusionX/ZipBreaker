#!/usr/bin/python3

## Title: Zip file Password Cracking Script
## Author: Mayank Deshmukh (ColdFusionX)
## Author website: https://coldfusionx.github.io
## Date: 2020-11-08

import sys
import zipfile
import argparse, textwrap
from pwn import *

#Expected Arguments
parser = argparse.ArgumentParser(description="Zip file Password Cracking Script by ColdFusionX", formatter_class=argparse.RawTextHelpFormatter, 
epilog=textwrap.dedent(''' 
Script Usage : 
./zipBreaker.py -z secrets.zip -w wordlist.txt -d myfolder
./zipBreaker.py -z secrets.zip -w wordlist.txt -d ~/Documents/myfolder
'''))

parser.add_argument("-z","--zip", help="Encrypted Zip file") 
parser.add_argument("-w","--wordlist", help="Password Dictionary") 
parser.add_argument("-d","--directory", help="Destination Folder to extract content")
args = parser.parse_args()

if  len(sys.argv) < 2:
    log.failure(f"Script Usage: ./zipBreaker.py -h [help] -z [secrets.zip] -w [wordlist.txt] -d [directory]")          
    sys.exit(1)


zip = args.zip
directory = args.directory
wordlist = args.wordlist
zip = zipfile.ZipFile(zip)

banner = log.info(f"Zip file Password Cracking Script by ColdFusionX")
print()
stats = log.progress(f"Hunting")
time.sleep(2)
print() 

wl = open(wordlist, "rb")
for password in wl:
    password = password.strip()
    stats.status("Trying with Password " f"{password.decode(errors='ignore')}")
    try:
        zip.extractall(path=f"{directory}", pwd=password)
    except: 
            continue
    else:
        log.success("SUCCESS !!")
        log.success("Password found: " f"{password.decode()}")
        log.success(f"Files Extracted inside -> {directory} directory!")
        sys.exit(0)
log.failure(f"Oops! Password not found, try different wordlist")


