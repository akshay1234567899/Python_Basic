from audioop import reverse

numbers= int(input("enter the numbers"))

r=0
while (numbers>0):
    temp=numbers%10
    r=r*10+temp
    numbers=numbers/10
    print(temp)
