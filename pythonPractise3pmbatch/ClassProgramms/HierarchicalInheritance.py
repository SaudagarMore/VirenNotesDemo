class User:#parent class
    def __init__(self,username,email):
        #instace method
        self.username=username
        self.email=email
    
    def Show_Basic_info(self):
        print("Username is:",self.username)
        print("User Email is:",self.email)

class Buyer(User): # user inherit into child1
    def place_order(self,items):
        print("The username",self.username,"Place Order of this",items)

class Seller(User): #user inherit into child2
    def list_product(self,product):
        print("The user :",self.username,"added new product list",product)
    
class DeliveryAgent(User):
    def delivery_items(self,ordid):
        print("Deliver by:",self.username,"With The This order id:",ordid)

buyer=Buyer("Rohit","Rohit1998@gmail.com")
seller=Seller("Pranit","Pranit1995@gmail.com")
delivery=DeliveryAgent("Sanket","Sanket1980@gmail.com")

Produtlist=["Relaeme","Samsung","MOTO","MIT"]
buyer.Show_Basic_info()
buyer.place_order("Oppo")
print("----------------------------")
seller.Show_Basic_info()
seller.list_product(Produtlist)
print("----------------------------")
delivery.Show_Basic_info()
delivery.delivery_items(1111)    
        