n=153
num=n
numberOfDigits=len(str(num))
total=0
while num>0:
    id=num%10
    total=(id**numberOfDigits)+total
    num=num//10
print(total==n)
# TC O(log10(n))
# SC O(1)