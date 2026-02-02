print("Welcome in My Application")
Mydata=[]
Mydata.append("C")
Mydata.append("CPP")
Mydata.append("Java")
Mydata.append("Python")
print(Mydata)
try:
    no=int(input("Please enter a number:"))
    no1=int(input("Please enter a number:"))
    result=no1/no
    print("Result is:",result)
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Cant divide by zero input only postive number")

for j in range(1,10):
    print(j,end=" ")