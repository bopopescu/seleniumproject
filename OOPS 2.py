class Employee:
    def __init__(self,ename,esal,eaddr):
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr

    def info(self):
        print("My name is ",self.ename)
        print("My esal is : ",self.esal)
        print("My eaddr is : ",self.eaddr)

e1=Employee('Hemraj',25000,'banglore')
e2=Employee('arun',30000,'Hyderabad')
e1.info()
e2.info()