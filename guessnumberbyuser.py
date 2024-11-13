import random

random_number=random.randint(1 ,10)
print(random_number)

num=None
while random_number!=num:
    try:
        num = int(input("Enter the number :"))
    except Exception as e:
        print(e)
        continue

    if num<random_number:
        print("value is less than number ")
    elif num>random_number:
        print("Value is high than number")
    else:
        print("congratulation!, number match with random number")
        break


