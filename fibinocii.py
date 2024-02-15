#fibinocii
limit=int(input("enter the limit"))
f1=0
f2=1
if limit<=0:
  print("no series")
elif limit==1:
    print(f1)
elif limit==2:
    print(f1)
    print(f2)

else:
      print(f1)
      print(f2)
      limit=1-2
      for i in range(1,0,-1):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
