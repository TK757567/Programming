from z3 import *

# Create an array of 30 BitVecs with 30 bits each
v5 = [BitVec('v5_%d' % i, 30) for i in range(30)]
sol = Solver()

for i in range(30):
    sol.add(v5[i]>40)
    sol.add(v5[i]<127)

# Initialize the solver

# Add the constraints
sol.add(v5[0] == 110)
sol.add(v5[1] == 0x30)
sol.add(v5[2] == 48)
sol.add(v5[3] == 98)
sol.add(v5[4] == 122)
sol.add(v5[5] == 0x7b)
sol.add(v5[29] == 0x7d)
sol.add(v5[1] == v5[2])
sol.add(v5[6] | v5[3] == 0x7a)
sol.add(v5[6] & v5[3] == 0x42)
sol.add(v5[28] == v5[4])
sol.add(v5[29] * v5[5] == 0x3c0f)
sol.add(v5[8] + v5[6] + v5[7] == 0x12e)
sol.add(v5[7] * v5[6] - v5[8] == 0x2a8a)
sol.add(v5[9] - v5[8] == 5)
sol.add(v5[10] - v5[9] == 0x1b)
sol.add(v5[10] ^ v5[11] == 0x20)
sol.add(v5[12] == v5[15])
sol.add(v5[11] + v5[12] == 0xb4)
sol.add(v5[12] + v5[13] == 0xb9)
sol.add(v5[13] + v5[14] - v5[16] == v5[13])
sol.add(v5[17] + v5[16] == 0xd9)
sol.add(v5[17] == v5[13])
sol.add(v5[14] + v5[16] == v5[14] * 2)
sol.add(v5[18] == 0x5a)
sol.add(v5[18] == v5[19])
sol.add(v5[21] ^ v5[19] ^ v5[20] == 0x7f)
sol.add(v5[20] ^ v5[21] ^ v5[22] == v5[21])
sol.add(v5[21] == 0x5f)
sol.add(v5[6] + v5[24] == 0xb4)
sol.add(v5[24] - v5[23] == -0x21)
sol.add(v5[25] == v5[9])
sol.add(v5[27] + v5[26] == 0xd4)
sol.add(v5[27] == v5[28])


if sol.check() == sat:
    m = sol.model()
    values = [m[v5[i]].as_long() for i in range(30)]
    print("".join([chr(i % 256) for i in values]))
else:
    print('unsat')

# n00bz{ZzZ_zZZ_zZz_ZZz_zzZ_Zzz}