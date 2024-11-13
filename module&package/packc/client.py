import sys
sys.path.append("/Users/akshaydhiman/PycharmProjects_SDET_08_01/pythonProject/module&package/packA")
sys.path.append("/Users/akshaydhiman/PycharmProjects_SDET_08_01/pythonProject/module&package/packB")


import emp as e
import stu as s

obj1=e.employee(101,'akshay',10000)
obj1.display()


obj=s.student(102,'dhiman','A')
obj.display()


