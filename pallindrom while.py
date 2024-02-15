#pallindrome using while loop
num=int(input("enter the number"))
temp=num
revnum=0
while num!=0:
  digit=num%10
  revnum=revnum*10+digit
  num//=10
print("reversed number"+str(revnum))
if temp==revnum:
  print("pallindrome")
else:
  print("not pallindrome")
