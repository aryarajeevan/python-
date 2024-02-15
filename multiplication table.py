#multiplication tables up to a given limit
limit=int(input("enter the starting point"))
end=int(input("enter the ending point"))
for i in range(limit,end+1):
  print("multiplication of ", str(i))
  for j in range(0,11):
    print(str(j*i))
