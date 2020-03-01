class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def talk(self):
        print("My name is:",self.name)
        print("My roll no is : ",self.rollno)

s1=Student('hemraj',100)
print(s1.name)
print(s1.rollno)
s1.talk()

s2=Student('arun',200)
s2.talk()