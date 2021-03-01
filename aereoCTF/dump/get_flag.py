# Found seed candidate:  1614289910
# Key is at:  0x18a53
# Iv is at:  0x2ade3
#from Crypto.Cipher import AES

from Crypto.Cipher import AES

fd = open("dump", "rb")

full_file = fd.read()

fd.close()

enc_flag = full_file[0x5060:0x5060+128]
key = full_file[0x18a53:0x18a53+16]
iv = full_file[0x2ade3:0x2ade3+16]

print(key)
print(iv)
print(enc_flag)
c = AES.new(key, AES.MODE_CBC, iv)

print(c.decrypt(enc_flag))

