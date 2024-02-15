#biggest digit of agiven number
num=int(input("enter a number"))
largedigit=0
for digit in str(num):
  digit=int(digit)
  if digit>largedigit:
    largedigit=digit
print("biggest digit of a given number is :",largedigit)

