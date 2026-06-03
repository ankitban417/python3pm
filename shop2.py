# wap to make a computer bazar model
print("###### Welcome To Computer Bazar######")
print("1.Acer(RS 10000)")
print("2.HP(RS 20000)")
print("3.apple(RS 50000)")
choice=int(input("Select your option:"))
qty=int(input("enter the quantity"))


if choice==1:
    laptop="Acer"
    
    price=10000*qty


elif choice==2:
    laptop="HP"
    
    price=20000*qty
    

elif choice==3:
    laptop="apple"
    price=50000*qty
else:
    print("option not available")
delivery_option=int(input("Delivery options:Home(Rs1000) 2.Store pickup(RS:0):") )

if delivery_option==1:
    tax=(price*13)/100
    dfee=1000
    pacakging=int(input("1.Plastic(RS1000) 2.Bag(RS:2000) 3.Gift box(RS:3000):"))
    if pacakging==1:

        pack_price=1000
    elif pacakging==2:
        pack_price=2000
    else:
        pack_price=3000
elif delivery_option==2:
    tax=0
    dfee=0
    pacakging=int(input("1.Plastic(RS1000) 2.Bag(RS:2000) 3.Gift box(RS:3000):"))
    if pacakging==1:
        pack_price=1000
    elif pacakging==2:
        pack_price=2000
    else:
        pack_price=3000

    delivery_location=int(input("1.Kathmandu(RS:13%) 2.LTP(RS:0)  3.BKT(RS:0):"))
    if delivery_location==1:
        address="kathmandu"
        tax=(price*13)/100
    elif delivery_location==2:
        address="Bhaktaour"
        tax=0
    elif delivery_location==3:
        address="Lalitpur"  
        tax=0  
    else:
        print("delivery is not available in the location")

total=price+tax+pack_price+dfee

cName=input("enter your name:")
cPhone=int(input("enter your phone number"))


print("#####This is your Bill####")
print("Customer name:",cName)
print("Product Name:",laptop)
print("quantity",qty)
print("Phone Number:",cPhone)
print("Laptop Price:",price)
print("Delivery Price:",dfee)
print("Pacakaging cost:",pack_price)
print("Tax Amount:",tax)
print("Grand Total=",total)



