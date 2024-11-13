from audioop import reverse
# captilize method
from audioop import reverse

s="string in python"
print(s.capitalize())
# output:String in python


# title method
print(s.title())
# output :String In Python


# upper case
print(s.upper())

# swapcase
print(s.swapcase())
print("string".swapcase())

# replace method
print(s.replace("py","on"))

# reverse string
# two method to reverse the string

demo_string="akshay"
rev_str=""
for i in demo_string:
    rev_str=i+rev_str
print("the reverse of string is =",rev_str)


# Slicing to reverse the string
s="dhiman"
demo=s[::-1]
print(demo)





