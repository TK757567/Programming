import hashlib
import string

char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \n"


f = open("root_flag_hash.txt","r").readlines()

any=""

for i in f:
    for z in char:
        flag=any+z
        result = hashlib.md5(flag.encode())
        hash= result.hexdigest()
        if hash == i.strip():
            any=any+z
            print(z,end="")

