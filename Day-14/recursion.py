# # recursive func : the func which call them self.
def fibbo(n):
    if n==0:
        return 0
    elif n==1:
        return  1
    else:
        return fibbo(n-1) + fibbo(n-2)
# print(fibbo(5))

num=10
for i in range(num):
    print(fibbo(i))