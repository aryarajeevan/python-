
#perfect number
num=int(input("enter the number"))
sum=0
for i in range(1,num):
  if (num%i==0):
    sum=sum+i
if sum==num:
    print("is aperfect number")
else:
    print("is not a perfect number")
