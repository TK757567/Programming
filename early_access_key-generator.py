import random
from re import match
ALPHABET1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM = "0123456789"
magic = 178
for x in ALPHABET1:
    for y in ALPHABET1:
        for z in NUM:
            res = int(ord(x))+int(ord(y))+int(ord(z))
            if res >= magic:
                g3 = "XP"+x+y+z
                key="KEY12-0F1O4-"+g3+"-GAMD2"
                gs = key.split('-')
                lastgrp = [sum(bytearray(g.encode())) for g in gs]
                print("KEY12-0F1O4-"+g3+"-GAMD2-"+str(sum(lastgrp)))
                magic = magic+1
