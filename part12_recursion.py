# head recursion
# count=0
# def func():
#     global count
#     if count==4:
#         return
#     print("recursion")
#     count+=1
#     func()
# func()
# tail recursion
count=0
def func():
    global count
    if count==4:
        return
    count+=1
    func()
    print("recursion")
func()

# TC O(N+1) => O(N)
# SC O(N+1) => O(N)