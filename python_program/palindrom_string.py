def func(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


enter_string = input("enter string :")

if func(enter_string):
    print("palindrom string")
else:
    print("not a palindrom string")