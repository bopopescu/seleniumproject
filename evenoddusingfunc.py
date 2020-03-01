def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    print(even,odd)



lst=[2,4,6,8,10]
count(lst)
