l=int(input("enter the line"))
n=1
for i in range(1,l+1,):
  for j in range(i):
    print(n,end=" ")
    n+=1
  print()
