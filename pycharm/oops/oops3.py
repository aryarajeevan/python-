class Student:
   def __init__(self,name,age):
       self.name=name
       self.age=age
   def disp(self):
       print("Name:%s \n Age:%d" %(self.name,self.age))
st1=Student("Arya",20)
print(st1.disp())