# ZipBreaker

## Zip file Password Cracking Script

Expected outcome: Discover the encrypted password of Zip file and it's extracted content

Intended only for educational and testing in corporate environments.

Script was tested on Python 3.8.6

This Script should work successfully on most of the Linux based Zip files used on CTF's.

### Usage

```shell
coldfx@Shockwave:~/zipBreaker$ ./zipBreaker.py -h
usage: zipBreaker.py [-h] [-z ZIP] [-w WORDLIST] [-d DIRECTORY]

Zip file Password Cracking Script by ColdFusionX

optional arguments:
  -h, --help            show this help message and exit
  -z ZIP, --zip ZIP     Encrypted Zip file
  -w WORDLIST, --wordlist WORDLIST
                        Password Dictionary
  -d DIRECTORY, --directory DIRECTORY
                        Destination Folder to extract content

Script Usage : 
./zipBreaker.py -z secrets.zip -w wordlist.txt -d myfolder
./zipBreaker.py -z secrets.zip -w wordlist.txt -d ~/Documents/myfolder
```

### Additional required Python modules :
- pwn

Installation:
```shell
pip3 install pwn
```

### Proof of Concept :

This script expects three user inputs :
- **Zip** - Encrypted Zip file
- **Wordlist** - Password Wordlist dictionary for Bruteforce (ex. rockyou.txt)
- **Directory** - Destination folder to extract Zip file content, Just specify the destination folder, the script will automatically create the folder as specified.

#### Expected Output :

```shell
coldfx@Shockwave:~/zipBreaker$ ./zipBreaker.py -z arks.zip -w dictionary.txt -d secretfolder
[*] Zip file Password Cracking Script by ColdFusionX

[◐] Hunting: Trying with Password secretkeeper

[+] SUCCESS !!
[+] Password found: secretk33per
[+] Files Extracted inside -> secretfolder directory!
```

### Reference

https://docs.python.org/3/library/zipfile.html



