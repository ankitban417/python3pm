# wap to enter a number and check whether it is even or odd

# a=input("enter a number;")
# a=int(a)

# if a%2==0:
#     print("the number is even")

# else:
#     print("the number is odd")

# wap to enter five subject marks and calculate the total percentage and grade

# a=int(input("enter the marks of subject 1:"))
# b=int(input("enter the marks of subject 2:"))
# c=int(input("enter the marks of subject 3:"))
# d=int(input("enter the marks of subject 4:"))
# e=int(input("enter the marks of subject 5:"))

# total=a+b+c+d+e

# print(total)

# percentage=(total/500)*100
# print(percentage)

# if percentage>=90:
#     print("grade A+")

# elif percentage>=80:
#     print("grade A")

# elif percentage>=70:
#     print("grade B+")

# elif percentage>=60:
#     print("grade B")

# elif percentage>=50:
#     print("grade C+")

# elif percentage>=40:
#     print("grade C")

# elif percentage>=30:
#     print("grade D")

# else:
#     print("grade NG")

# wap to enter a number and check whether it is divisible by 3 and 5
# a=int(input("enter a number:"))

# if a%3==0 and a%5==0:

#     print("the number is divisible by 3 and 5")


# wap to enter three numbers and print in descending order

# a=int(input("enter a number :"))
# b=int(input("enter second number"))
# c=int(input("enter third number"))

# if a>b and a>c:
#     if b>c:
#         print(a,b,c)
#     else:
#         print(a,c,b)

# elif b>a and b>c:
#     if a>c:
#         print(b,a,c)
#     else:
#         print(b,c,a)

# elif c>a and c>b:
#     if a>b:
#         print(c,a,b)
#     else:
        # print(c,b,a)

# wap to make a atm machine

# balance=10000
# print("welcome to atm")
# pin=int(input("enter the pin:"))

# if pin==1234:




#     print("1.checkbalace")
#     print("2.withdraw")
#     print("3.deposit")

#     choice=int(input("enter the choice :"))

#     if choice==1:
#         print("the balance is ",balance)

#     elif choice==2:
#         amount=int(input("enter the amount"))
#         if amount<=balance:
#             balance=balance-amount
#             print("withdraw sucessfully")
#             print("the remaining balace is ",balance)
#         else:
#             print("insufficent balace")    

    
#     else:
#         amount=int(input("enter the amount:"))
#         balance=balance+amount
#         print("deposited sucessfully")
#         print("the balance is",balance)
# else:    print("invalid pin")






                


# wap to make a laptop shopping website

print("#############welcome to laptop shopping website##############")
print("1. dell-$10000")
print("2. hp-$8000")
print("3. lenovo-$12000")
print("4. apple-$150000")
choice=int(input("enter the choice:"))

if choice==1:
    qty=int(input("enter the quantity:"))
    total=qty*10000
    print("the total amount is",total)
     
    print("do you want to proceed to payment" )
    proceed=input("enter yes or no:")
    if proceed=="yes":
        print("payment sucessfully")
    else:
        print("order cancelled")
elif choice==2:
    qty=int(input("enter the quantity:"))
    total=qty*8000
    print("the total amount is",total)
     
    print("do you want to proceed to payment" )
    proceed=input("enter yes or no:")
    if proceed=="yes":
        print("payment sucessfully")
    else:
        print("order cancelled")
elif choice==3:
    qty=int(input("enter the quantity:"))
    total=qty*12000
    print("the total amount is",total)
     
    print("do you want to proceed to payment" )
    proceed=input("enter yes or no:")
    if proceed=="yes":
        print("payment sucessfully")
    else:
        print("order cancelled")                
elif choice==4:
    qty=int(input("enter the quantity:"))
    total=qty*150000
    print("the total amount is",total)
     
    print("do you want to proceed to payment" )
    proceed=input("enter yes or no:")
    if proceed=="yes":
        print("payment sucessfully")
    else:
        print("order cancelled")        




# match case in python

 