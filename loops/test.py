# x=0
# while x<3:
#     print(x,end=" ")
#     x+=1
# else:
#     print("Done")    

# for i in range(2):
#     for j in range(2):
#         if i==1 and j==1:
#             break
#         print(i,j)

x=0
for i in range(3):
    for j in range(i):
        x+=1
    else:
        x=+5
        print(x)    
