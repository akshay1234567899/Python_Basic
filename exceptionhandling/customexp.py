class NegativeNumberError(Exception):
    def __init__(self,msg="Negative values are not allowed"):
        self.msg=msg
        super().__init__(self.msg)

# function to check +ve or -ve
def check_positive(number):
    if number<0:
        raise NegativeNumberError("Invalid Number, Please enter the positive number")
    else:
        print(f"The number {number} is positive")

try:
    num=int(input("Enter the number"))
    check_positive(num)
except NegativeNumberError as e:
    print(e)
except ValueError as e:
    print(e)
