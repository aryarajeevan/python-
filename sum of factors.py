
#sum of factors
n=int(input("enter the number"))
sum=0
for i in range(1,n+1):
  if n%i==0:
    sum=sum+i
    print(i)
print(sum)
