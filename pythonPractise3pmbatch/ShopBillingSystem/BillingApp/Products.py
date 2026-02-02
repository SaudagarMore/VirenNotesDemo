from datetime import datetime
class Products:
    myproduct={}
    mycartlist=[]#
    def __init__(self,key,value):# dell,18000
        Products.myproduct.update({key:value})#{dell:18000}

    def getProducts(self):
        print("Product List ")
        print(Products.myproduct)
        print("---------------------"*3)
        for data1 in Products.myproduct.items():
            print("Product Name:",data1[0],"Product Price:",data1[1])
        print("---------------------"*3)

    def ProductBillApp(self):
        print("\n-----------Product Bill App--------")
        while True:
            print("Add items into cart:")
            pname=input("Enter Product Name to cart:")
            if pname in Products.myproduct.keys():
                    pqty=int(input("Enter Product Quantity:"))
                    value=Products.myproduct.get(pname)
                    Products.mycartlist.append((pname,value,pqty))
                    print("Product Added Into The Cart")
                    self.GenerateFinalBill()
            else:
                    print("Product Name not found")

    def GenerateFinalBill(self):
        print("==============")
        price=0
        qty=0
        finalBill=0
        finalgst=0
        Gstrate=5
        for data in Products.mycartlist:
            price=data[1]
            qty=data[2]
            self.TotalGstAmount=(price*qty*Gstrate)/100
            self.TotalAmount=price*qty+self.TotalGstAmount

        finalBill+=self.TotalAmount
        finalgst+=self.TotalGstAmount
        print("--------------------------")
        print("Total Gst:",finalgst)
        print("Total Amount:",finalBill)
        print("---------------------------")
        try:
            pname=''
            price=0
            qty=0
            for data in Products.mycartlist:
                pname=data[0]
                price = data[1]
                qty = data[2]

            Myfile=open("Bills.txt","+a")
            Mydate=datetime.now().strftime("%Y%m%d")
            Myfile.write("\n"+"Bill Date:"+Mydate+"\n")
            Myfile.write("Product Name :"+pname+"\n")
            Myfile.write("Product Price:"+str(price)+"\n")
            Myfile.write("Product Quantity:"+str(qty)+"\n")
            Myfile.write("Total Gst:"+str(finalBill)+"\n")
            Myfile.write("Total Amount:"+str(finalBill)+"\n")
            Myfile.write("----------------------------------")
            Myfile.close()
        except FileNotFoundError:
            print("Invalid File name")

for j in range(0,1):
    pname=input("Enter Product Name:")
    price=int(input("Enter Product Price:"))
    p1=Products(pname,price)

p1.getProducts()
p1.ProductBillApp()