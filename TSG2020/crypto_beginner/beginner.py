#from Crypto.Util.Number import ling_to_bytes
from string import printable
import sys
sys.setrecursionlimit(1500)

tot_len = 3131
def printAllKLength(set, k): 
  
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
  
# The main recursive method 
# to print all possible  
# strings of length k 
def printAllKLengthRec(set, prefix, n, k): 
      
    # Base case: k is 0, 
    # print prefix 
    if (k == 0):
        if str(int.from_bytes(("TSG{"+prefix+"}").encode("utf-8"), byteorder='big') << 10000).endswith('1002773875431658367671665822006771085816631054109509173556585546508965236428620487083647585179992085437922318783218149808537210712780660412301729655917441546549321914516504576'):
            print(prefix)   
            exit()
        return
  
    # One by one add all characters  
    # from set and recursively  
    # call for k equals to k-1 
    for i in range(n): 
  
        # Next character of input added 
        newPrefix = prefix + set[i] 
          
        # k is decreased, because  
        # we have added a new character 
        printAllKLengthRec(set, newPrefix, n, k - 1) 

from z3 import *

x = Int()



exit()




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

		print(orig, len(stringa))
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
numero = int(stringa)

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


