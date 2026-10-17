# Print x, n times
# def fun(x,n):
#     if n==0:
#         return
#     print(x)
#     fun(x,n-1)
# fun(15,4)

# Print 1 to n head 
# def fun(x,n):
#     if x>n:
#         return
#     print(x)
#     fun(x+1,n)
# fun(1,4)

# Print n to 1 head 
# def fun(x,n):
#     if x<n:
#         return
#     print(x)
#     fun(x-1,n)
# fun(4,1)

# Print n to 1 tail
# def fun(x,n):
#     if x>n:
#         return
#     fun(x+1,n)
#     print(x)
# fun(1,4)

# Print 1 to n tail
# def fun(x,n):
#     if x<n:
#         return
#     fun(x-1,n)
#     print(x)
# fun(4,1)

# single parameter
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
fun(4)