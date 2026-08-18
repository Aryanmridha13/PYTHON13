# gendar=input("Enter gendar :")

# if gendar=="male" or gendar=="others":
#     age=int(input("age"))
#     if age>=18 and age<=65:
#         print("E")
#     else:
#         print("N")

# elif gendar=="fe":
#     age=int(input("age"))
#     if age>=21 and age<=45:
#         print("FF")
#     else:
#         print("nn")
# num=int(input("Enter number"))

# if num%3==0:
#     print("Divide by 3")
# elif num%5==0:
#     print("Divide by 5")
# elif num%7==0:
#     print("Divide by 7")
# else:
#     print("NO")

########



val=input("Enter value  ")

if val>="A" and val<="Z":
    print("uper")
elif val>="a" and val<="z":
    print("lower")
elif val>="0" and val<="9":
    print("Number")
else:
    print(f"{val} Special Char..!!")


