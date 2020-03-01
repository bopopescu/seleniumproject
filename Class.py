class Student:

    model='hyundai'

    def __init__(self,name,age,color,tyre):
        self.name=name
        self.age=age
        self.color=color
        self.tyre=tyre

    def info(self):
        print("student information",self.name,self.age)

    def car(self):
        print("car informtaion is:",self.color,self.tyre)

    @classmethod
    def inclass(cls):
        print(cls.model)

    @staticmethod
    def none():
        print("this is static method")

Student.inclass()
s1=Student('hem',30,'white',4,)
s2=Student('raj',29,'blue',5)
s1.info()
s1.car()
s2.info()
s2.car()
s1.none()