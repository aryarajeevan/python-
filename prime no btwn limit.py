#prime numbers between limits
limit=int(input("enter the starting point"))
end=int(input("enter the ending point"))
for i in range(limit,end+1):
  if limit==1:
    continue
  for j in range(2,i):
    if i%j==0:
      break
  else:
      print(i)
