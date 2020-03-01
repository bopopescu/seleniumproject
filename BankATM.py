print("welcome to SBI bank")
restart=('Y')
chances=3
balance=100
while chances>=0:
    pin=int(input("Insert card and Enter pin number :"))
    if pin==(1234):
        print("pin entered correctly")
        while restart not in ('n','N','NO','no'):
            print("press 1 to check balance\n")
            print("press 2 to withdraw\n")
            print("press 3 to pay\n")
            print("press 4 to return card\n")
            option=int(input("Enter any choice:"))
            if option==1:
                print("your balance is A$")
                restart=input("would you like to go back?")
                if restart in ('n','N','NO','no'):
                    print("Thank you")
                break
            elif option==2:
                withdrawal=float(input("how much would you like to withdraw"))
                if withdrawal in [10,20,30,40,100]:
                    balance=balance-withdrawal
                    print("Your balance is :",balance)
                    restart=input("would you like to continue")
                    if restart  in ('n','N','NO','no'):
                        print("Thank you")
                        break
                elif withdrawal not in [10,20,30,40,100]:
                    print("amount invalid")
            elif option==3:
                pay=float(input("Enter the amount to pay"))
                balance=balance+pay
                print("Balance after payment is",balance)
                restart=input("would you like to continue:")
                if restart  in ('n','N','NO','no'):
                    print("Thank you")
                    break
            elif option == 4:
                print("card returned Thank you")
    elif pin != (1234):
        print("Invalid pin, enter correct one")
        chances=chances-1
        if chances == 0:
            print("Attempts over")
            break