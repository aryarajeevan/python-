#strong number
num=int(input("enter a number"))
temp=num
sum=0
while num!=0:
  digit=num%10
  fact=1
  while digit>1:
    fact=fact*digit
    digit-=1
  sum=sum+fact
  num//=10
if temp==sum:
  print("strong number")
else:
  print("not a strong number")


