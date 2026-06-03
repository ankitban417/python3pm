# wap to make a atm machine

balance=10000
print("welcome to atm")
pin=int(input("enter the pin:"))

if pin==1234:




    print("1.checkbalace")
    print("2.withdraw")
    print("3.deposit")

    choice=int(input("enter the choice :"))

    if choice==1:
        print("the balance is ",balance)

    elif choice==2:
        amount=int(input("enter the amount"))
        if amount<=balance:
            balance=balance-amount
            print("withdraw sucessfully")
            print("the remaining balace is ",balance)
        else:
            print("insufficent balace")    

    
    else:
        amount=int(input("enter the amount:"))
        balance=balance+amount
        print("deposited sucessfully")
        print("the balance is",balance)
else:    print("invalid pin")