#custom Exception Creation Code
class MyNewCustomeError(Exception):
    def __init__(self,value):
        self.value=value
        super().__init__(self.value)

#Applicaiton Code
def Test():
    no=int(input("Enter a Number:")) #50
    dividval=int(input("Enter a Dividing Value:")) #0
    if dividval==0:
        raise MyNewCustomeError("Cant Divide By Zero")
    else:
        result=no/dividval
        print("The Result is:",result)
try:
    Test()
except MyNewCustomeError as e:
    print(e)