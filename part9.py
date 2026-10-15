# Print All Factors of a Given Number 
# brute force
# num=2
# result=[]
# for i in range(1,num+1):
#     if num%i==0:
#         result.append(i)
# print(result)

# TC O(N)=> O(N)
# SC O(k) k=amount of factor

# better solution
# num=10
# result=[]
# for i in range(1,num//2):
#     if num%i==0:
#         result.append(i)
# result.append(num)
# print(result)

# TC O(N/2)=> O(N)
# SC O(k) k=amount of factor

# optimal solution
from math import sqrt
num=36
result=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if num//i !=i:
            
            result.append(num//i)
        print(num//i)
print(result)

# TC O(N)+O(NlogN)
# SC O(k) k=amount of factor