# n=[5,3,2,2,1,5,5,7,5,10]
# m=[10,111,1,9,5,67,2]
# for x in m:
#     count=0
#     for y in n:
#         if y==x:
#             count+=1
#     print(count)
# TC O(MxN)
# SC O(1)
# hash_list=[0]*11
# for i in n:
#     hash_list[i]+=1
# for num in m:
#     if num<0 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])
# TC O(M+N)
# SC O(1)

# Practice
# solve it by using dictionary


# Method 3
s="azyxyyzaaaa"
q=["d","a","y","x"]
hash_list=[0]*26
for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    hash_list[index]+=1
for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(hash_list[index])
# TC= O(M+N)
# SC O(1)