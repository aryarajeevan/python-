#big among n numbers
limit=int(input("enter the limit"))
b=0
for i in range(1,limit+1):
  n=int(input())
  if n>b:
    b=n
print ("large is : ", b)
