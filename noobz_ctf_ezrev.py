array = [130, 37, 70, 115, 64, 106, 143, 34, 54, 134, 96, 98, 125, 98, 138, 104, 25, 3, 66, 78, 24, 69, 91, 80, 87, 67, 95, 8, 25, 22, 115]

z=[]*len(array)


for i in range(len(array)//2):
    if i%2!=0:

       array[i]=array[i]-30
    else:
       

       temp1 = array[len(array)-1-i]
       temp2= array[i]
       array[i] = temp1+10
       array[len(array)-1-i] = temp2 - 20



print(array)

for x in range(len(array)):
   
   if x%2==0:
      array[x]=(array[x]^19)
   else:
      array[x]=(array[x]^55)
      


print("".join([chr(i) for i in array]))