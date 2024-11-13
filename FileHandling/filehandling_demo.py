# file handling in py :
# open : open the file
# Either use double backslashes
# file = open("C:\\Users\\akshaydhiman\\Desktop\\File\\handling\\folder\\example.txt", "w")
# file.write("This is the first instruction.")
# file.write("This is the first instruction.\n")
# file.write("This is the first instruction.")
# file.close()
# file=open("C:\\Users\\akshaydhiman\\Desktop\\File\\handling\\folder\\example.txt", "r")
# print(file.read())
# print(file.readline())
# file.close()


file = open("C:\\Users\\akshaydhiman\\Desktop\\File\\handling\\folder\\example.txt", "a")
file.write(" this is the last line of the file ----- here enjoy")
file.close()
print("the program is executed")

# removed the file from the desktop
# import os
# try:
#     os.remove("C:\\Users\\akshaydhiman\\Desktop\\File\\handling\\folder\\example.txt")
#     print("file is deleted")
# except FileNotFoundError as e:
#     print(e)
#
# os.rmdir("paht of dir pass here link")


