Matrix = [[0x5F6E5F6F,0x53657254,0x73655F74],[0x69647321,0x63726169,0x5F544975],[0x6F217966,0x21736E5F,0x68745F21]]

keys = [2,2,1,3,2,2,2,1, 0, 3 , 0 , 0 , 3 , 1 , 0 , 1 , 0 , 0 , 3 , 0 , 1 , 2 , 0 , 0 , 3 , 2 , 1 , 1 , 2 , 1 , 0 , 0 , 0 , 2 , 2 , 1 , 1 , 2 , 0 , 2 , 1 , 2 , 2 , 2 , 2 , 1 , 1 , 1 , 1 , 1 , 2 ,2 , 0 , 1 , 1 , 0 , 1 , 0 , 1 , 2 , 0 , 0 , 2 , 3 , 0 , 2 , 2 , 1 , 1 , 1 , 2 , 2 , 3 , 2 , 0 , 2 , 2 , 0 , 3 , 1 , 1 , 0 , 2 , 1 , 1 , 1 , 0 , 0 , 1 , 1 , 0 , 2 , 0 , 1 , 0 , 2 , 0 , 2 , 2 , 3 , 1 , 2 , 2 , 0 , 2 , 0 , 0 , 1 , 0 , 0,0]

def split_list_into_chunks(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]



keys=split_list_into_chunks(keys,3)



for i in keys: 
    x = i[::-1] 

    r,c,s = x[0],x[1],x[2]

    v = Matrix[r][c]
    x=((v >> (8 * s)) & 0xFF)
    print(chr(x),end="")

# Dead{The_S_in_IoT_stands_for_security!!!!}    