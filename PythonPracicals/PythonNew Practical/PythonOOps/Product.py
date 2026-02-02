#python class Declared  ->module
class Product:
    #python Constructor
    def __init__(self,pid,pname,price,pstock,psellprice):
        #python product class members//variable
        self.prdid=pid
        self.prdname=pname
        self.prdprice=price
        self.prdstock=pstock
        self.psellingprice=psellprice
               
    #using function class member initialization
    # def StoreProductData(self,pid,pname,price,pstock,psellprice):
    #     #python product class members//variable
    #     self.prdid=pid
    #     self.prdname=pname
    #     self.prdprice=price
    #     self.prdstock=pstock
    #     self.psellingprice=psellprice
    
    #data method /function
    def calculatetotalprice(self):
        print("The product is:",self.prdid)
        print("Product Name:",self.prdname)
        print("Product price is:",self.prdprice)
        print("Product Stock is:",product.prdstock)
        print("Total Selling amount is:",self.prdstock*self.psellingprice)
        
product=Product(pid=1,pname="Oppo",price=15000,pstock=25,psellprice=20000) #object Created
# product.StoreProductData(pid=1,pname="Oppo",price=15000,pstock=25,psellprice=20000)
product.calculatetotalprice()