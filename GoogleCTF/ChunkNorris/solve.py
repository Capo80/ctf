from z3 import *
from random import *
from Crypto.Util.number import *

a = 0xe64a5f84e2762be5

n = 0xab802dca026b18251449baece42ba2162bf1f8f5dda60da5f8baef3e5dd49d155c1701a21c2bd5dfee142fd3a240f429878c8d4402f5c4c7f4bc630c74a4d263db3674669a18c9a7f5018c2f32cb4732acf448c95de86fcd6f312287cebff378125f12458932722ca2f1a891f319ec672da65ea03d0e74e7b601a04435598e2994423362ec605ef5968456970cb367f6b6e55f9d713d82f89aca0b633e7643ddb0ec263dc29f0946cfc28ccbf8e65c2da1b67b18a3fbc8cee3305a25841dfa31990f9aab219c85a2149e51dff2ab7e0989a50d988ca9ccdce34892eb27686fa985f96061620e6902e42bdd00d2768b14a9eb39b3feee51e80273d3d4255f6b19


for i in range(0, 100):
	a = randint(0, 100000)
	b = randint(0, 100000)
	print( a % 5 * b % 5 == a*b % 10)

s1 = Int('x')
s2 = Int('y')

s = Solver()

chunks = [ n & ((2**128-1) << i*128) for i in range(0, 16)]

a_chunk = [ a**i % 2**64 for i in range(0, 16)]
#chunks.reverse()
#print(chunks)
for i in range(0, len(chunks)):
	print( chunks[i] * inverse(a**(i*2), 2**128) // (2**(128*i)))
	print( GCD( n, chunks[i] * inverse(a_chunk[i]*a_chunk[i], 2**128) // (2**(128*i))))
	s.add( ( ( a_chunk[i] * s1 * a_chunk[i] * s2 ) ) % 2**128 == chunks[i] % 2**128)

print(s.check())