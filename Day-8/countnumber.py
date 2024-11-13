# number=list(map(int,input("Enter the numbers :").split(",")))
# print(number)
# for i in set(number):
#     print(f"number count {i} = {number.count(i)}")


# count number of vowel in list
number=list(input("Enter the elements :").split())
print(number)
vowels=set("aeiouAEIOU")
vowels_count=0
for i in number:
    for char in i:
        if char in vowels:
            vowels_count+=1
print("Number of vowels are :",vowels_count)
