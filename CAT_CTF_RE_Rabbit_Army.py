enc=[0xea,0x64,0xc4,0x63,0x9a,0x7c,0xc,0x70,0xd2,0x72,0xbe,0x14,0xe,0x7a,0xa8,0x40,0xd2,0x64,0x8a,0x4a,0xe,0x41,0xbe,0x40,0x88,0x7a,0x8a,0x15,0xc,0x4b,0x96,0x1f]

flag=[""]*32


for i in range(len(enc)):
    if i &1 == 0:
        any = enc[i] ^0x6c
        flag[i] = any//2

    else:
        flag[i] = enc[i] ^ 0x25

print("".join(chr(z)for z in flag)) 