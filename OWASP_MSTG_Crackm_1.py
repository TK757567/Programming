import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


key = "8d127684cbc37c17616d806cf50473cc"

length = len(key)

any = bytearray(length//2)
for i in range(0,length,2):
    any[i//2] = (int(key[i],16)<<4)+ int(key[i+1],16)

enc=base64.b64decode("5UJiFctbmgbDoLXmpL12mkno8HT4Lv8dlat8FxR2GOc=")

cipher = AES.new(any,AES.MODE_ECB)
plaintext = unpad(cipher.decrypt(enc),AES.block_size)
plaintext = plaintext.decode()
print(plaintext)