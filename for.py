# total_user=?
# total_male=?
# total_female=?
# total_active=?
# total_inactive=?
# total_active_male=?
# total_active_female=?
# total_inactive_male=?
# total_inactive_female=?

students=[
    {'name':'ram','gender':'male','status':True},
    {'name':'shyam','gender':'male','status':False},
    {'name':'sita','gender':'female','status':True},
    {'name':'gita','gender':'female','status':False}
]

# total students
# total_students=len(students)
# print("total students is",total_students)
#total active



# total_active = 0
# for student in students:
#     if student['status'] == True:
#         total_active += 1

# print("Total active students:", total_active)
total_inactive = 0
for student in students:
    if student['status'] == False:
        total_inactive += 1

print("Total active students:", total_inactive)

# total_male
total_male=0
for student in students:
    if student['gender'] == 'male':
        total_male+=1
print("total male are",total_male)


total_female=0
for student in students:
    if student['gender'] =='female':
        total_female+=0
print("total female are",total_female)

total_active_male=0

for student in students:
    if student['gender']=='male':
    
        if student['status']==True:
                total_active_male+=1
print("the total active male ",total_active_male)


total_active_female=0
for student in students:
    if student['gender']=='female':
        if student['status']==True:
            total_active_female+=1      
print("total active female are",total_active_female)

total_inactive_male=0

for student in students:
    if student['gender']=='male':
    
        if student['status']==False:
                total_inactive_male+=1
print("the total inactive male ",total_inactive_male)

total_inactive_female=0
for student in students:
    if student['gender']=='female':
    
        if student['status']==False:
                total_inactive_female+=1
print("the total inactive female ",total_inactive_female)