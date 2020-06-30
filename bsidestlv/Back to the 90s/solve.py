
## Numbers obtained by the snake bot
numb = [ 66, 83, 105, 100, 101, 115, 85, 149, 209, 57, 13, 9, 81, 196, 37, 54, 150, 70, 87, 53, 89, 93, 19, 144, 208, 149, 28, 66, 83, 105, 100, 101, 115, 85, 149, 209, 57, 13, 9, 81, 196, 37, 54, 150, 70, 87, 53, 89, 93, 19, 144, 208, 149, 28, 66, 83, 100, 101, 115 ]

## xor vector found in wasm
xor_values = [49, 17, 58, 13, 1, 22, 39, 24, 26, 100, 2, 2, 2, 75, 44, 102, 66, 23, 11, 2, 50, 54, 92, 106, 48, 1, 2, 21, 38, 47, 63, 60, 70, 80, 22, 0, 64, 87, 59, 61, 27, 38, 43, 28, 91, 108, 51, 95, 7, 70, 28, 11, 1, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 1, 48, 0, 0, 0, 0, 0, 19, 0, 0, 0]

## Values given by the program
xor_numb = [66, 83, 105, 100, 101, 115, 84, 101, 116, 78, 67, 66, 84, 115, 66, 83, 105, 100, 101, 115, 84, 101, 116, 78, 67, 66, 84, 115, 66, 83, 105, 100, 101, 115, 84, 101, 116, 78, 67, 66, 84, 115, 66, 83, 105, 100, 101, 115, 84, 101, 116, 78, 67, 66]

## Some useful functions
def string_to_bin(stringa):
	res = ""
	for i in stringa:
		res += pad(bin(ord(i))[2:], 8)
	return res

def pad(binary, size):
	while(len(binary) != size):
		binary = "0" + binary
	return binary


## Start value of the number generator found in game_init function
start = 115

flag = ""

for i in range(0, len(numb)-5):
	start = start^xor_values[i]
	flag += chr(start)

print(flag)
