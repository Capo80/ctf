#from Crypto.Util.Number import ling_to_bytes
from string import digits
import sys
from z3 import *

x = Int('x')
y = Int('y')

print(solve(x > 0, y > 0, x * (2**10000) == y*(10**175) + 1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576))


sys.setrecursionlimit(1500)

tot_len = 3131

def recover(stringa):

	lista = [stringa]
	
	while(True):

		stringa = lista[0]
		lista = lista[1:]

		#print(len(stringa))
		#print(int(stringa).to_bytes((int(stringa).bit_length() + 7) // 8, byteorder='big'))
		if (len(stringa) == 3131):
			print(stringa)
			print(int(stringa).to_bytes((int(stringa).bit_length() + 7) // 8, byteorder='big'))
			break

		orig = 0
		numero = int(stringa)
		while (numero % 2 == 0):
			numero = numero // 2
			orig+= 1

		print(orig, len(stringa), stringa[:50])
		for i in digits:
			temp = i + stringa
			numero = int(temp)
			c = 0
			while (numero % 2 == 0):
				numero = numero // 2
				c+= 1
			if c > orig:
				lista= [temp] + lista

#assert(str(int.from_bytes(open('flag.txt', 'rb').read(), byteorder='big') << 10000).endswith('1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576'))
stringa = '1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576'
stringa = str(int(123 << 1000))[-175:]
print(str(int(123 << 1000))[-180:], stringa)
numero = int("0" + stringa)

c= 0
while (numero % 2 == 0):
	numero = numero // 2
	c+= 1

print(c)
exit()
recover(stringa)
max_i=''
while (True):
	max_c = 0
	stringa = max_i + stringa
	print(stringa)
	if (len(str(int(stringa) >> 10000)) == 50):
		print(int(stringa).to_bytes((int(stringa).bit_length() + 7) // 8, byteorder='big'))
		break
	for i in digits:
		temp = i + stringa
		c = 0
		numero = int(temp)
		while(numero % 2 == 0):
			numero = numero // 2
			c+= 1
			if max_c < c:
				max_c = c
				max_i = i
		#print(i, c)	
#print(long_to_bytes(numero))
#print(numero.to_bytes((numero.bit_length() + 7) // 8, byteorder='little'))

#value = numero.to_bytes((numero.bit_length() + 7) // 8, byteorder='big')


#print(value)


#print(bin(1 << 10000))
#print(bin(numero))
#assert(str(int.from_bytes(value, byteorder='big') << 10000).endswith('1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576'))


