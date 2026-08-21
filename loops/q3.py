# n=10
# while n > 1:
#     print(n,end=" ") 
#     n-=1

# n = int(input("n :"))
# for i in range(1,11):
#     print(f'{n} * {i} =  {n*i}')


# n=int(input("n :"))
# sum=0

# for i in range(1,n+1):
#     sum+=i
#     # print(i,end=" ")
#     print(sum,end=" ")
# print(sum)    


# n=int(input("n "))

# for i in range(1,n+1):
#     if i%5==0:
#         print(f"{i} is divisible by 5" )

# n=int(input("N :"))

# i=1
# cnt=0
# while i<=n:
#     cnt+=1
#     i+=1
# print(cnt)    

# n=int(input("n :"))
# i=1
# sum=0
# while i<=n:
#     if i%2==0:
#         print(i,end=" ")
#         sum+=i
#     i+=1
# print(f' sum is = {sum}')


n=int(input("n: "))
i=1
while i <= n:
    if i%3==0:
        print(f'{i} is divided by 3')
    i+=1    