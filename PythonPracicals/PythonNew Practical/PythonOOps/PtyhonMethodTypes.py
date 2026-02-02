# class Person:
#     #instance method
#     #class members
#     MyCollegeName="RSML" #class variable
#     page=25
#     count=0
#     def AddPersondata(self,pname):
#         self.personname=pname
#         print(self.personname)
#         print(self.page)
#         print(Person.page)
        
#     @staticmethod
#     def Count():
#         print(Person.page)
#         for k in range(1,5):
#             print(k)
#             Person.count+=1
            
#     @classmethod         #self/empty // cls
#     def TestClassMethod(self):
#         print(self.page)
#         print(Person.MyCollegeName)
#         print(self.MyCollegeName)
           
# p=Person()  #create new instance create new space/store into different 
# print(Person.page) # stored into static memory
# p.AddPersondata("Pradip")
# Person.Count()
# Person.TestClassMethod()
# p.TestClassMethod()

# class Product:
#     # instance method
#     def PrintCity(self):
#         print("From pune city")
        
#     @classmethod
#     def ProductData(c,pid,pname,price):
#         print("From Class Method")
#         c.pcode=pid
#         c.pname=pname
#         c.pprice=price
#         print(c.pcode," ",c.pname," ",c.pprice)

#     @classmethod
#     def mydetails(self):
#         self.ProductData(1001,"Mi",25000)
#         self.PrintCity(self)
    
#     #2nd instance method
#     def MyFavGame(self):
#         print("My Fav sports is cicket")
#         self.mydetails() 
            
#     @staticmethod
#     def ShowDetails():
#         print("From instance Method")
       
#     @staticmethod
#     def Test():
#         print("i am second static method")
#         Product.ShowDetails()
        
# #Product.mydetails()
# Prd=Product()       
# Prd.MyFavGame()        
# Product.Test()


class Books:
    pstock=100    #class variable
    @classmethod
    def AddBooks(self,bid,bname,bprice):
        print("From Add Books method")
        bcode=bid     # class variable 
        bookname=bname
        bprice=bprice
        print(bcode," ",bookname," ",bprice," ",Books.pstock)

    @staticmethod 
    def BookPurchase():
        print("From Book Purchase")
        Books.AddBooks(101,"Java With classes",400)
        print(Books.pstock)
       
book=Books() 
Books.BookPurchase()
book.AddBooks(102,"Python With classes",500)
