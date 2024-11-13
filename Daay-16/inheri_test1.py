from re import A


class B(A):
    def __init__(self):
        print("constructor calling class B")
obj=B()
obj=A()