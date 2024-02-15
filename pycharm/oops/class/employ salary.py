class Employee:
    def __init__(self,name,basic_sal,percent_deduction,percent_allowance):
        self.name=name
        self.basic=basic_sal
        self.allowance=percent_allowance
        self.deduction=percent_deduction
        self.net_salary=0
    def display(self):
        self.net_salary=self.basic+(self.basic*self.allowance/100)-(self.basic*self.deduction/100)
        print("....Salary Details....")
        print("Name :",self.name)
        print("Basic Salary :",self.basic)
        print("Deduction :",self.deduction)
        print("Allowance :",self.allowance)
        print("Net Salary : ",self.net_salary)
name=str(input("enter the name :"))
basic=int(input("enter the basic salary :"))
deduction=int(input("enter the deduction :"))
allowance=int(input("enter the allowance"))
sal=Employee(name,basic,deduction,allowance)
sal.display()
