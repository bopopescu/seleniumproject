
def fact(n):
    f=1
    if n<1:
        print("Enter number greater than or equal to one")
    elif n==1:
        print("factorial is:",n)
    else:
        for i in range(1,n+1):
            f=f*i
        print(f)


n=int(input("Enter the  number:"))
fact(n)