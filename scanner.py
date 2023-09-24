from pyfiglet import figlet_format
import os
import time
from tqdm import tqdm
import sys

print("\n")

for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    time.sleep(0.2)

os.system("figlet 'Scanner HQ' | lolcat")
print("\n\n[.] Boot succseful!")


target = input("[*] TARGET IP ADDRESS: ")

def nmap(target):
    type = input("[1] Basic scan | [2] Detailed scan: ")
    if type == '1':
        print("[.] Doing a basic scan on "+ target +" with 'Nmap\n'")
        print("==============================================\n")
        os.system("nmap "+ target + " -Pn -p-")
    elif type == '2':
        print("[.] Doing an advanced scan on ", target, " with 'Nmap'\n")
        print("==============================================\n")
        os.system("nmap "+ target + " -sV -sC -p-")
    else:
        print("Wrong input")

nmap(target)
