from traceback import print_tb


class MyEvenOddException(Exception):#
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)

def CheckingEvenOfodd(no):
    if no%2==0:
        print("Even No")
    else:
        raise MyEvenOddException("Cant Insert Odd Value")

try:
    no=int(input("Please enter a number"))
    CheckingEvenOfodd(no)
except MyEvenOddException as My:
    print(My)
except ValueError:
    print("Please enter a number")
finally:
    print("Task Completed")
