num=int(input("enter the no"))
temp=num
rev=0
while num!=0:
  digit=num%10
  rev=rev*10+digit
  num//=10
if temp==rev:
    print("yes")
else:
    print("not")
