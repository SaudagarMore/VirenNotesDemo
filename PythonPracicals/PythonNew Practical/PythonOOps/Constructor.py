


# #class Declared
# class mobile:
#     #instance method
#     def show1(self,no1,no2):
#         print("This is show method",no1+no2)
            
# class Sample(mobile):
#     def show1(self, no1, no2):
#         super().show1(no1, no2)
#         print(no1*no2)
    
# s1=Sample()
# s1.show1(20,10)

#1000 dataabase server port api 
# sending rewuest 
#value
class Demo: #parent class
    def adddata(self,id1,name):
        self.no=id1
        self.name=name
    
    def showdata(self):
        print(self.no*self.no)
        print(self.name)
    
class Demo1(Demo):
    def mydetails(self):
        print(self.no*self.no*self.no)
    
     
d1=Demo1()
d1.adddata(20,"Pratik")
d1.showdata()
d1.mydetails()
