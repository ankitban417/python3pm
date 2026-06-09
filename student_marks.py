student_marks=[]
num=int(input("enter the nymber of students:"))

x=1
while x<=num:
    print(f"=======Student ID : {x}=======")
    nep=int(input("Enter Nepali Marks:"))
    eng=int(input("Enter English Marks:"))
    math=int(input("Enter math Marks:"))
    social=int(input("Enter social Marks:"))
    computer=int(input("Enter computer Marks:"))
    total=nep+eng+math+social+computer
    student_marks.append(total)
    x+=1

for total in student_marks:
    print("Total marks",total)
    percentage =(total/500)*100
    print("percentage",percentage)
    if percentage>=90:
        print("grade A+")

    elif percentage>=80:
         print("grade A")

    elif percentage>=70:
     print("grade B+")

    elif percentage>=60:
     print("grade B")

    elif percentage>=50:
     print("grade C+")

    elif percentage>=40:
        print("grade C")

    elif percentage>=30:
        print("grade D")

    else:
         print("grade NG")

   
