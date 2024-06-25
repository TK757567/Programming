Matrix = [[0x81ccd1ca, 0x81cce1cb, 0xa7dfe1c6], [0xbbc9d2d9, 0xffc5d7da, 0x81c3cece], [0x81cacdf0, 0xbaf2d9cd, 0x9cc2da89]] 


for i in range(3):
    for x in range(3):
        Matrix[i][x]= hex(Matrix[i][x]^0xdeadbeaf )


keys = [3,2,2,2,2,0,1,1,1,2,2,1,2,0,2,3,0,0,2,0,0,1,1,0,1,0,2,2,1,1,2,2,2,0,0,1,3,0,1,1,0,1,2,1,2,0,2,2,0,0,2,3,1,2,0,2,0,1,1,2,3,1,0,0,1,1,1,2,1,3,0,2,0,2,1,1,2,0,0,1,0,0,0,0,2,1,0,0,1,0,3,2,1,0,1,2,1,0,0,1,2,2,3,2,0,3,1,1]

def split_list_into_chunks(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]



keys=split_list_into_chunks(keys,3)



for i in keys: 
    x = i[::-1] 

    r,c,s = x[0],x[1],x[2]

    v = Matrix[r][c]
    x=((((int(v, base=16) >> (8 * s))) & 0xFF))
    print(chr(x),end="")


# Dead{Bring_a_shovel_&_dig_up_a_dead_body!}