class Product:       
    mylist=[]
    mylist1=[]
    def __init__(self,pid,pname,price):#3 parameters
        self.pno=pid       
        self.pname=pname
        self.price=price
        self.mylist.append(self.pno)
        self.mylist.append(self.pname)
        self.mylist.append(self.price)          
     
P1=Product(101,"Mi",10000)#constructro initlized   
#print(P1.mylist)

P2=Product(102,"Realeme",12000)#constructro initlized   
print(P1.mylist)
print(P2.mylist1)

# P3=Product(103,"Oppo",14000)#constructro initlized   
# print(P3.mylist2)




