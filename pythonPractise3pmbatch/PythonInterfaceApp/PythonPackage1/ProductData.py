class ProductData:
    def __init__(self,pname,pstock,price):
        self.pname=pname
        self.pstock=pstock
        self.price=price

    def PrintProductDetails(self):
        print("product name: ",self.pname)
        print("product stock: ",self.pstock)
        print("product price: ",self.price)
