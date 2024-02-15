#smallest digit of a number
n=int(input("enter anumber"))
temp=n
smalldigit=9
for digit in str(n):
  digit=int(digit)
  if digit<smalldigit:
    smalldigit=digit
print("the smallest digit in the given number is",smalldigit)
