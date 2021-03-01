from binascii import *
from string import printable
import string
from Crypto.Util.number import *
import random

shuffle_mask = "0D0C0A08040F030E090B0501070602"
add_mask = "6763746613371337FEE1DEADDEADBEEF"
xor_mask = "AAF986EB34F823D4385F1A8D49B45876"


def string_to_ints(stringa):
	res = []
	for i in range(0, len(stringa), 8):
		res.append(int(stringa[i:i+8], 16))
	return res


def pad(hex_n, n):
	while len(hex_n) < n:
		hex_n = "0" + hex_n
	return hex_n

def ints_2_to_string(array):
	temp = [pad(hex(i)[2:], 2) for i in array]
	res = []
	for i in range(0, len(array), 4):
		for j in range(3, -1, -1):
			res.append(temp[i+j])
	return ''.join(res)

def ints_4_to_string(array):
	temp = [pad(hex(i)[2:],8) for i in array]
	temp.reverse()
	return ''.join(temp)

def print_hex(array):
	hex_array = [hex(i) for i in array]
	print(hex_array)


## shuffle prep
shuffle_array = []
add_array = []

for i in range(0, len(shuffle_mask), 2):
	numb = int(shuffle_mask[i:i+2],16)
	shuffle_array.append(numb)
	#print(shuffle_mask[i:i+2], int(shuffle_mask[i:i+2],16))
	
shuffle_array.reverse()
shuffle_array.append(0)

print(shuffle_array)
## add prep
add_array = string_to_ints(add_mask)

add_array.reverse()

## xor prep
xor_array = string_to_ints(xor_mask)


xor_array.reverse()
stringa = "CTF{S1MDf0rM3!}"

for i in range(0, len(stringa)):
	print(i, stringa[i], shuffle_array[i])
#exit()
# F
#for c in printable:
for a in printable:
	for b in printable:
		#stringa = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
		start = [ord(i) for i in stringa]
		start.append(0)

		#start[8] = ord(c)
		start[4] = ord(b)
		start[5] = ord(a)

		temp = [ord(i) for i in stringa]
		temp.append(0)
		
		#temp[9] = ord(c)
		temp[4] = ord(b)
		temp[5] = ord(a)

		#print(stringa)
		#print_hex(start)

		for i in range(0, len(shuffle_array)):
			start[i] = temp[shuffle_array[i]]

		#print("before add:")
		#print_hex(start)

		start = string_to_ints(ints_2_to_string(start))

		for i in range(0, len(add_array)):
			start[i] = (start[i]+add_array[i]) % 4294967296
											   
		#print("after add:")
		#print_hex(start)
		#print(ints_4_to_string(start))


		#xor_mask = xor_mask[::-1]
		#print(hex(int(ints_4_to_string(start), 16) ^ int(xor_mask, 16)))


		#print("xor_array")
		#print_hex(xor_array)
		#print_hex(start)

		for i in range(0, len(start)):
			start[i] = start[i]^xor_array[i]
		#xor_mask = xor_mask[::-1]

		#print(start)
		#print(ints_4_to_string(start))
		start = ints_4_to_string(start)

		final_array = []
		for i in range(0, len(start), 2):
			numb = int(start[i:i+2],16)
			final_array.append(numb)
			#print(shuffle_mask[i:i+2], int(shuffle_mask[i:i+2],16))
			
		final_array.reverse()
		#final = ints_4_to_string(start)
		#print(ints_4_to_string(start))
		
		#print("".join([chr(i) for i in temp]))
		#print_hex(final_array)
		final = "".join([chr(i) for i in final_array])
		
		#print(final_array[-4:])
		# if final.isprintable():
		# 	print("".join([chr(i) for i in temp]))
		# 	print(final)
		# 	print(start)
		# 	print_hex(final_array)
		# 	exit()

		#print(final)
		#exit()
		if final[:6] == "".join([chr(i) for i in temp])[:6]:
			print("acceptable ", a, ", ", b)
			#print("found 1")
			print(final, "".join([chr(i) for i in temp]))
			if final[-4:-1].isprintable():
				print(final)
				print("".join([chr(i) for i in temp]))
			#print(final_array)
			#exit()
