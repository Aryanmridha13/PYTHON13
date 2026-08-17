n = int(input("Enter a number :"))

if n <= 9 and n >= -9:
    print(f'{n} is a single digit number')

elif (n > 9 and n <= 99) or (n < -9 and n >= -99):
    print(f'{n} is a double digit number')

elif (n > 99 and n <= 999) or (n < -99 and n >= -999):
    print(f'{n} is a triple digit number')

else:
    print(f'{n} is not single, double or triple digit number')