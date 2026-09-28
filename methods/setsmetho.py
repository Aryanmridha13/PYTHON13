s={10,20,30,30,40,50,6,0}
s1={2,3,4,10,20,5,54}
# s.add(7)
# print(s)
# s.update({2,3,4,10,20})
# print(s)
# s.remove(2)
# print(s)
# # s.remove(55)
# s.discard(55)

print(s.union(s1))
print(s.intersection(s1))
print(s.difference(s1))
print(s.symmetric_difference(s1))
print(s.issubset(s1))
print(s.isdisjoint(s1))
