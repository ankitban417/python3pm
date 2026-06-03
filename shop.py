# wap to make a laptop shopping website

print("#############welcome to laptop shopping website##############")
print("1. dell-$10000")
print("2. hp-$8000")
print("3. lenovo-$12000")
print("4. apple-$150000")
choice=int(input("enter the choice:"))

if choice==1:
    product="dell"
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
    product="hp"
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
    product="lenovo"
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
    product="apple"
    qty=int(input("enter the quantity:"))
    total=qty*150000
    print("the total amount is",total)
     
    print("do you want to proceed to payment" )
    proceed=input("enter yes or no:")
    if proceed=="yes":
        print("payment sucessfully")
    else:
        print("order cancelled")   

cname=input("enter the your name:")
cnumber=input("enter phone number:")
caddress=input("enter the address:")
print("#####THIS IS YOUR BILL#####")
print(f"Company Name: {cname}")
print(f"Phone Number: {cnumber}")
print(f"Address: {caddress}")
print(f"Product: {product}")
print(f"Quantity: {qty}")
print(f"Total Amount: {total}") 