from PythonPackage1.ProductData import ProductData
from PythonPackage1.First import  Calculate,MydataList

p1=ProductData("Realeme",10,5000)
p1.PrintProductDetails()
print(Calculate(20,60,50))

MydataList.append("Java")
MydataList.append("Python")
MydataList.append("C++")
for j in MydataList:
    print(j)