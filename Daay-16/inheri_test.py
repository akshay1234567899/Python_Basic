# Inherience : inherit the property of one class to another.
# two benifits : reusebility, avoid duplication
# There are four types:
# single(one  parent one child),multilevel (parent to child ........),heirarchy (parent one and child two ),multiple(parent two and one child)


class A:
    def __init__(self):
        print("constructor calling")

    def func(self):
        print("method calling")

obj=A()
obj.func()
