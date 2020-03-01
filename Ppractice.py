n=int(input("Enter the number to search:"))  #40
list=[10,20,30,40,50,60,70,80,90,100]
l=0
u=len(list)-1
for i in range(0,len(list)):
    mid=(l+u)//2
    if list[mid]==n:
        print("Number found",list[mid],"at position",mid)
        break
    else:
        if list[mid]<n:
            l=mid
            print("Number found", list[mid], "at position", mid)
        else:
            u=mid
