# Known: 0xF3 0x0F 0x1E 0xFA 0x55 0x48 0x89 0xE5
# start of function: 0x13A9

def array_xor(array1, array2):
	if len(array1) != len(array2):
		raise ValueError("Arrays have different lenght")

	ret_array = bytearray(len(array1))

	for i in range(0, len(array1)):
		ret_array[i] = array1[i]^array2[i]

	return ret_array

fd = open("dump", "rb")

full_file = fd.read()

fd.close()

file = full_file[:0x5b6d7]
section = bytearray(full_file[0x13A9:0x172A])
enc_function_start = full_file[0x13A9:0x13A9+8]
known_fuction_start = [0xF3, 0x0F, 0x1E, 0xFA, 0x55, 0x48, 0x89, 0xE5]

known_bytes = array_xor(enc_function_start, known_fuction_start)

print("Known bytes are: ", known_bytes)

array_indexes = [(i, i+len(known_bytes)) for i in range(len(file)) if file[i:i+len(known_bytes)] == known_bytes]

print("xor_array is at: ", hex(array_indexes[0][0]))

xor_array = file[array_indexes[0][0]:array_indexes[0][0]+32]

print("Full array is: ", xor_array)

for j in range(0, 896):
	section[j] ^= xor_array[j%32]

new_file = full_file[:0x13A9] + section + full_file[0x172A:]

fd = open("dec_dump", "wb")

fd.write(new_file)

fd.close()

print("Decrypted dump created!")