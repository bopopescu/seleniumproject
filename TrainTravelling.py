travelling=input("yes or no:")
while travelling == 'yes':
    num=int(input("Enter  umber of passengers travelling :"))
    for num in range(1,num+1):
        name=input("Enter name:")
        age=int(input("Enter age :"))
        sex=input("Enter sex:")
        print("Name is :",name)
        print("Age is :",age)
        print("Sex is:",sex)
    travelling=input("for got someone :?")
if travelling=='no':
    print("no one travelling")