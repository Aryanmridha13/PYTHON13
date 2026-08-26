# METHOD IN LIST
l1=[10,20,30]
print(l1)
l1.clear()
print(l1)

# 2 copy

l2=[10,20,30]
l3=l2.copy()
print(id(l2),id(l3))

# 3 count

l4=[10,20,39,40,50,10,10,30,20,10]
l5=l4.count(10)
print(l5)

# append

l6=[10,20,30]
l6.append(1000)
print(l6)

# 5 extend
l7 = [10,20,30,30,40]
l7.extend([10,30,50,60,70])
print(l7)

# 6 insert

l8 = [10,20,30,10,60,20,90]
l8.insert(2,25)
print(l8)

# 7 pop 
l9=l8.pop(2)
print(l8)

l10=l8.remove(60)
print(l8)