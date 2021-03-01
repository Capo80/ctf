## xor_array is at:  0x4ba74
## heap block starts at: 0x5060

## times the heap is allocated
## 128 + 64*rand + 32 + 64*rand + 16 + 64*rand + 192 + 64*rand 

from ctypes import CDLL
libc = CDLL("libc.so.6")

latest_time = 1614211200

while True:
	
	libc.srand(latest_time)

	block_pos = 0x5060 + 128

	for i in range(0, 64):
		block_pos += libc.rand()%2047

	key_pos = block_pos
	block_pos += 32

	for i in range(0, 64):
		block_pos += libc.rand()%2047

	iv_pos = block_pos
	block_pos += 16

	for i in range(0, 64):
		block_pos += libc.rand()%2047

	block_pos += 192

	for i in range(0, 64):
		block_pos += libc.rand()%2047

	if block_pos == 0x4ba74:
		print("Found seed candidate: ", latest_time)
		print("Key is at: ", hex(key_pos))
		print("Iv is at: ", hex(iv_pos))
		exit()

	if (latest_time%1000 == 0):
		print(latest_time)
	latest_time += 1