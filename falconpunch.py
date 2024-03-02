import os
import sys

os.system("figlet FalconPunch")

def main():
    domain = sys.argv[1]
    print("[*] Finding sub-domains of " + domain + "\n")
    os.system("subfinder -d " + domain + " >> temp.txt -v")
    os.system("assetfinder -subs-only " + domain + " >> temp.txt")
    print("\n[*] Filtering out...\n")
    os.system("cat temp.txt | sort | uniq > "+ domain + ".txt && rm temp.txt")
    print("[*] Created sub-domain list in" + domain " ".txt")
main()
