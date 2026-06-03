
print("1.ADD 2.SUbstract 3.Multiply 4.divide")
x=int(input("Enter first number :"))
y=int(input("Enter the second number :"))
op=input("Enter the operator :")

match op:
    case "+":
        sum=x+y
        print(sum)
    
    case "-":
        sub=x-y
        print(sub)

    case "*":
        mup=x*y
        print(mup)

    case "/":
        div=x/y
        print(div)

    case _:
        print("enter a valid operator")
