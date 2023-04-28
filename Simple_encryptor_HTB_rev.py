enc=[0,245,62,18,192,189,141,22,240,253,117,153,250,239,57,154,75,150,33,161,67,22,35,113,101,251,39,75]


xor=[72,68,251,245,179,253,114,217,70,194,41,207,79,230,73,64,176,190,238,4,167,55,22,222,17,9,187,52,187,54,21,3,122,16,248,45,13,106,7,83,45,48,34,124,22,107,188,198,41,170,203,208,225,225,175,242]



def first(xor):
    first=[]
    for i in range(len(xor)):
        if i==0:
          first.append(xor[i+1]&7)
        elif i%2==0:
            first.append(xor[(i+1)%len(xor)]&7)

    return first



def second(xor):
    second=[]
    for i in range(len(xor)):
       if i == 0:
            second.append(xor[i])
       elif i%2!=0:
            second.append(xor[(i+1)%len(xor)])
    return second



first_rand=first(xor)

second_rand=second(xor)

print(first_rand)

print(second_rand)

for i in range(len(enc)):

    idk=enc[i]
    
    lol=(idk >> first_rand[i%len(first_rand)])   | (idk << 8 - first_rand[i%len(first_rand)])
    any=(lol%256)^second_rand[i%len(second_rand)]
    
    
    
    
    print(chr(any),end="")
