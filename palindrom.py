#pallindrome or reverse using for loop
a=int(input("enter a number"))
rev=""
temp=a
for i in str(a):
  rev=i+rev
print(rev)
if temp==int(rev):
  print("pallindrome")
else:
  print("not a pallindrome")
