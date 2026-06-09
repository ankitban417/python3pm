# categories=[
#     {'cid':1,'name':'Laptop'},
#     {'cid':2,'name':'Mobile'},
#     {'cid':3,'name':'tv'},
# ]

# products=[
#     {'pid':1,'name':'Dell','price':50000,'cid':1},
#     {'pid':2,'name':'HP','price':60000,'cid':1},
#     {'pid':3,'name':'iPhone','price':100000,'cid':2},
#     {'pid':4,'name':'Samsung','price':80000,'cid':2},
#     {'pid':5,'name':'LG','price':40000,'cid':3},
# ]

# Laptop
#   Dell 50000
#   HP 60000

# print("1.Laptop")
# print("2.Mobile")
# print("3.tv")

# cid=int(input("enter the category"))

# for category in categories:
#     if category['cid']==cid:
#         print(f"{category['name']}")
        






































# users=[
#     {'username':'admin','password':'admin123'},
#     {'username':'ram','password':'ram123'},
#     {'username':'shyam','password':'shyam123'},
    
# ]
# usernameinusers=input("enter username:")
# passwordinusers=input("enter the password")
# found = False
# for user in users:
#     if user['username'] == usernameinusers:
#         found = True
#         if user['password'] == passwordinusers:
#             print("login successful")
#         else:
#             print("invalid password")
#         break

# if not found:
#     print("invalid username")


# for x in range(7,1,-1):
#     for y in range(1,x-1):
#         print("*",end=" ")
#     print()



# for x in range(1,6):
#     for y in range(1,x+1):
#         print(y,end="")
#     print()


# for x in range(1,8):
#     for y in range(1,x+1):
#         if x==6:
#             print("*moon*")
#             break
#         else:
#             print("*",end="")
#     print()
# for x in range(1,8):
#     for y in range(1,x+1):
#         if x==6:
#             print("*sun*")
#             break
#         else:
#             print("*",end="")
#     print()
# print("*")
# print("*")
