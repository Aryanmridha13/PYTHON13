s1={10,20,45,2,1,23,24,100}
s2={10,30,70,80,34,100,90}
s3={10,30,50,25,70,45}

res1=s1.union(s2,s3)
print(len(res1),res1)

res2=s1.intersection(s2)
print(len(res2),res2)

res3=s1.difference(s2,s3)
print(len(res3),res3)
