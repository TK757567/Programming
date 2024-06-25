from pwn import *

# nc static-01.heroctf.fr 8000
io = remote('static-01.heroctf.fr', 8000)
io.recvline()
io.recvline()
while True:
    eq = io.recvline().decode().strip()
    if eq !="exec(\"import platform,os;os.system('shutdown -h now')if platform.system()in'Linux'else os.system('shutdown -s')\")":
        io.sendline(str(eval(eq)).encode())
        print(eq)
        print(io.recvline())
    else:
        
        print(io.recvall())
        break

#  Hero{E4sy_ch4ll3ng3_bu7_tr4pp3d}