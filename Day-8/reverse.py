num=int(input("Enter the numbers :"))
rev=0
while(num>0):
    temp=num%10
    rev=rev*10+temp
    num=num//10;
print("reverse of the numbers is :",rev)
