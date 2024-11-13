# # how to create a string ?
# # String are immutable (not changeable)
# from operator import index
#
# s='welcome'
# print(s)
# s=str("welcome")
# s=str('welcome')
# print(s)
#
#  # create the empty string
#  # name=''
#
# name="David"
# # name[0]="j"   # interview question why string is immutable
# print(id(name))
# # memory address :4300218608
#
#
# name=name+"message address"
# # print the memory address of the string
# print(id(name))
# # memory address :4378714224
#
# # ---------------------------------------------------------------
# str="welcome"
# print(str  + " to python")
# # output : welcome to python
# # * print the string multiple times
# print(str*2)
# # output: welcomewelcome
# # -------------------------------------------------------
# # Example - 4 slicing []
# # starting index -- 0
# # ending index --- last index+1
#
# str= "welcome"
# print(str[1:3])
# print(str[:6])
# print(str[1:-1])
# last one charcter will be removed
# ---------------------------------------------------------------------------

# example convert ascii value to caps alpha 1. ord() and chr()
#  /returns the ASCII code of the chracter
# print(ord("A"))
# Chracter representation by a ASCII number
print(chr(1))

# --------------------------------------------------------------------------------

# print(max(("qrs")))
# print(min("ABC"))
# print(len("abcdef")+1)

# -----------------------------------------------------------------------------------
# String comparison
str1="welcome"
str2="welcome"
test=str1==str2
print("output",test)
print(str1>=str2)
# -----------------------------------------------------------------------------------------




