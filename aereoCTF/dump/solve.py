fd = open("dump", "rb")

full_file = fd.read()

def count_pair(buffer, dword):
	c = 0
	for i in range(0, len(buffer)-1):
		if (buffer[i] == dword[0] and buffer[i+1] == dword[1] ):
			c +=1
	return c

# THRESHOLD = 100
# zeros = 0
# print("seciton start: 0")
# for i in range(0, len(full_file)):
# 	if full_file[i] != 0:
# 		if (zeros > THRESHOLD):
# 			print("section start:", hex(i))
# 		zeros = 0

# 	if full_file[i] == 0:
# 		zeros += 1

# 	if (zeros == THRESHOLD):
# 		print("section end:", hex(i-THRESHOLD))


# seciton start: 0
# section end: 0xa4c
# section start: 0x1000
# section end: 0x379c
# section start: 0x3d20
# section end: 0x479c
# section start: 0x4d20
# section end: 0x5b6d7
# section start: 0x805060

# Known: 0xF3 0x0F 0x1E 0xFA 0x55 0x48 0x89 0xE5
# start of function: 0x13A9
i = 0
while True:
	
	section = full_file[0x13A9:0x172A]
	section = bytearray(section)

	vector = full_file[0x3000+i:0x3000+i+32]

	for j in range(0, 896):
		section[j] ^= vector[j%32]

	if (section.count(0x48) > 15):
		print(section.count(0x48))
		print("vec:", hex(i))
		print(section)
	if (b"Aereo" in section):
		print(section)
		exit()
	if (b"urandom" in section):
			print(section)
			exit()


	if (i%0x100 == 0):
		print(hex(i))
		#print(vector)
	i += 1