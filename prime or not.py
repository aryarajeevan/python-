#prime or not
num=int(input("enter the number"))
if num!=1:
  for i in range(2,num):
    if num%i==0:
      print("composite number")
      break
  else:
    print("prime")
else:
  print("prime or composite")
