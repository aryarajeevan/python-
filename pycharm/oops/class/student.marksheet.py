class Marksheet:
    def __init__(self,name,mrk1,mrk2,mrk3):
        self.name=name
        self.mrk1=mrk1
        self.mrk2=mrk2
        self.mrk3=mrk3
        self.s=0
        self.average=0
    def display(self):
        print("...... Student Markshet.....")
        print("Name :",self.name)
        print("Mark 1 :",self.mrk1)
        print("Mark 2 :",self.mrk2)
        print("Mark 3 :",self.mrk3)
        self.s=self.mrk1+self.mrk2+self.mrk3
        self.average=self.s/3
        print("Average score :",self.average)
        if self.average>=95:
            print("Grade :","A+")
        elif self.average>=90:
            print("Grade :","A")
        elif self.average>=80:
            print("Grade :","B+")
        elif self.average>=70:
            print("Grade :","B")
        elif self.average>=60:
            print("Grade :","C+")
        elif self.average>=50:
            print("Grade :","C")
        elif self.average>=40:
            print("Grade :","D")
        else:
            print("Grade :","F")

stdname=str(input("Name :"))
mark1=float(input("mark 1 :"))
mark2=float(input("mark 2 :"))
mark3=float(input("mark 3 :"))
m=Marksheet(stdname,mark1,mark2,mark3)
m.display()