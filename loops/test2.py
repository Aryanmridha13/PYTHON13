# p="PASSWORD"
# while True:
#     up=input("enter password :").upper()
#     if up != p:
#         print("Wrong password")
#         for i in range(1,4):
#             n=input("Enter pass")
#             print(f"Wrong password {3-i} attemp avalible ")

#             if n==p:
#                 print("password match")
#                 break
#         else:
#             print("login limit reach exit")
#             break
#     else:
#        print("Password match")
#        exit()                   
    
                
   
p = "PASSWORD"

for i in range(1, 4):
    n = input("Enter password: ").upper()

    if n == p:
        print("Password match")
        break
    else:
        print(f"Wrong password, {3-i} attempts available")

else:
    print("Login limit reached. Exit")                    

                        

