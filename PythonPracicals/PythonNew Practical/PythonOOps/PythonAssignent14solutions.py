## 14). Design a class Order that:
# Has instance variables: order_id, items, and total_amount
# Keeps a class variable: total_orders to count how many orders have been placed
# Provides:
# Instance method: display_order() to display order details
# Class method: show_order_count() to display total orders placed

class Order:
    total_orders=1
    def __init__(self,ordid,items,total_amount):
        self.ordid=ordid
        self.items=items
        self.total_amount=total_amount
        Order.total_orders+=1

    def display_order(self):
        print("Order id is:",self.ordid)
        print("Order items:",self.items)
        print("Total Amount is:",self.total_amount)
        print("----------------------------------------------------")

    @classmethod
    def Show_order_Count(cls):
        print("Total Placed Orders count:",Order.total_orders)

for j in range(1,5):
    odid=int(input("Enter Order id:"))
    pname=input("Enter Product Name:")
    price=int(input("Enter Product Price:"))
    print("----------------------------------------------------")
    Order.Show_order_Count()
    ord=Order(odid,pname,price)
    ord.display_order()

Order.total_orders-=1
Order.Show_order_Count()
