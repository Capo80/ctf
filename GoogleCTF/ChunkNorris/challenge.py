#!/usr/bin/python3 -u

import random
from Crypto.Util.number import *


a = 0xe64a5f84e2762be5
chunk_size = 64

## bits // chunk size === 16

def gen_prime(bits):
  s = random.getrandbits(chunk_size)

  while True:
    s |= 0xc000000000000001
    
    p = 0
    for _ in range(bits // chunk_size):
      p = (p << chunk_size) + s
      print(bin(p))
      s = a * s % 2**chunk_size
    if isPrime(p):
      return p

n = gen_prime(1024) * gen_prime(1024)
e = 65537
flag = open("flag.txt", "rb").read()
print('n =', hex(n))
print('e =', hex(e))
print('c =', hex(pow(bytes_to_long(flag), e, n)))
