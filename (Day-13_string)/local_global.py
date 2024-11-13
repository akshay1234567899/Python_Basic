# xy=100
# def call():
#     global xy
#     xy=200
#     print(xy)
# call()

#using global variable function to update the value
# example :
# x=100;
# def cool():
#     # global x
#     x=500
#     print(x)
# cool()
# print(x)

# --------------------------------------------------------------------------------------------
# There is no need to declare global variable
def cool1():
    global x
    x=100
    print(x)
cool1()
print(x)


# ==================================================
# arguments --2 types
# 1) Positional Arguments
def fun(i,j):
    print(i,j)

fun(10,90)

# 2) Keyword arguments : passsing the vlaue by specify the value

def fun(a,b):
    print(a,b)
fun(10,b=20)


