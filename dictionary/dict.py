print("1. add a contact")
print("2. delete a contact")
print("3. edit a contact")
print("4. search a contact")
print("5. list all contacts")
print("6. exit")
contactbook={}
choice=int(input("enter your choice"))
while choice!=6:
  if choice==1:
   name=(input("enter the name"))
   phno=int(input("enter the no"))
   contactbook[name]=phno
   print("1 contact added successfully")
elif choice==2: 
   name=input("enter the name of contact to delete")
   contactbook.pop(name)
   print("1 contact deleted successfully")
elif choice==3:
  name=input("enter the name of the contact to edit")
  phno=int(input("enter the phone number"))
  contactbook[name]=phno
  print("contact edicted successfully")
elif choice==4:
  name=input("enter the name")
  print("phone number of",name," : ",contactbook[name])
elif choice==5:
  print("name\t\t phone number")
  for x,y in contactbook.items():
    print(x,"t\t",y)
  else:
    print("invalid choice !!!")
  choice=int(input("enter your choice"))


