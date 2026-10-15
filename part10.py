# Store Frequency in Dictionary
# Method 1
# find=3
# nums=[1,2,3,3,5,3,5,10,10,2,57]
# freq_set=dict()
# for i in range(0,len(nums)):
#     if nums[i] in freq_set:
#         freq_set[nums[i]]+=1
#     else:
#         freq_set[nums[i]]=1
# print(freq_set[find])
# TC O(N)
# SC 0(N)
# Method 2
find=3
nums=[1,2,3,3,5,3,5,10,10,2,57]
hash_map={}
n=len(nums)
for i in range(0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map[find])
# TC O(N)
# SC 0(N)