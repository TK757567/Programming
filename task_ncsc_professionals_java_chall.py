passwordToIntArray = [1429423210,1734759271,1666856046,812738891,1635010379]

flag=[]

for i in range(len(passwordToIntArray)):
    flag.insert(i * 4,(passwordToIntArray[i] >> 24)%256)
    flag.insert(i * 4 + 1, (passwordToIntArray[i] >> 16)%256)
    flag.insert(i * 4 + 2, (passwordToIntArray[i] >> 8)%256)
    flag.insert(i * 4 + 3, (passwordToIntArray[i])%256)


any="".join(chr(f) for f in flag)
print("flag{"+any+"}")
