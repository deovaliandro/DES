from Crypto.Cipher import DES

mode = DES.MODE_ECB
cipher = DES.new("HELLODEO", mode)
result = cipher.encrypt("DEOVALIA")
inhex = result.hex()
# print(bin(int(inhex, 16))[2:])
print(inhex)