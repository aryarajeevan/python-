#calculating electricity bill
units=int(input("enter the units"))
if units<=100:
    amount=units*1.5
    print("amount is :",amount)
elif units<=200:
    amount=units*2.5
    print("amount is :",amount)
elif units<=300:
    amount=units*3.5
    print("amount is :",amount)
else:
    amount=units*5
    print("amount is :",amount)
