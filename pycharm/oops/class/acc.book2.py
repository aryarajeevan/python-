class Bank:
    def _init_(self,name,accno):
        self.name=name
        self.accno=accno
        self.balance=0
    def display(self):
        print("Account details")
        print("----------------")
        print("Acc holder:",self.name)
        print("Acc number:",self.accno)
        print("")
    def deposit(self,deposit):
        self.dp=deposit
        self.balance=self.balance+self.dp
        print("success")
    def withdraw(self,w):
        if w<self.balance:
            self.balance=self.balance-w
            print("successs")
        else:
            print("no balance")
    def amountdisplay(self):
       return self.balance


name=input("enter account holder name:")

accno=int(input("enter account number:"))
b=Bank(name,accno)
b.display()
print("1.desposit money")
print("2.withdraw money")
print("3.view balance")
print("4.exit")
while True:
    c = int(input("enter choice:"))
    if c==1:
        deposit=int(input("amount:"))
        b.deposit(deposit)
    elif c==2:
        wr=int(input("amount to withdraw"))
        b.withdraw(wr)
    elif c==3:
        print("balance",b.amountdisplay())
    elif c==4:
        break
    else:
        print("invalid input")