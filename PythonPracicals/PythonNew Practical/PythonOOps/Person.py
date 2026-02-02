# # programme for class and object of person
# #self
# #class Declared /created
# class Person:
#      #method of class with including 4 parameters of person
#     def AddNumbers(data,num1,num2):
#         data.no1=num1
#         data.no2=num2
    
#     def CheckMaxandMin(mydata):
#         if mydata.no1>mydata.no2:
#             print(mydata.no1,"is max than",mydata.no2)
#         else:
#             print(mydata.no2,"Max than ",mydata.no1)
        
#     def PrintListDeails(self,Mylist):
#         self.newlist=Mylist

#         for j in self.newlist:
#             print(j)
    
#     def AddlistNewItem(self):       
#         Demolist=[]
#         Demolist.extend([10,20,30,40,50])
#         self.newlist.extend(Demolist)
#         print("New Updated list is:",self.newlist)
        
#     def GetPersonDetails(self,pid,pname,page,pcontact):
#         #class members created (personid,personnamepersonage,personcontact)
#         self.personid=pid  #201
#         self.personname=pname
#         self.personage=page
#         self.personcontact=pcontact
        
#         #data method
#     def PrintPersonDetails(self,pid,pname,page,pcontact):
#         self.GetPersonDetails(pid,pname,page,pcontact)
        
#         print("Person id is:",self.personid)
#         print("Person Name is:",self.personname)
#         print("Person Age is:",self.personage)
#         print("Person Contact:",self.personcontact)
                
#         #data method
#     # def TestAppp(self):
#     #     for k in range(1,5):
#     #         print(k," ","Person Data Printed")
   
# #object creation in python
# mydata=["C","CPP","Java","Python"]
# P1=Person()
# #P1.AddNumbers(20,30)
# #P1.CheckMaxandMin()
# P1.PrintListDeails(mydata)
# P1.AddlistNewItem()

# #P1.PrintPersonDetails(101,"kunal",25,9307014300)

# #method Called Using Person Class Object
# #P1.PrintPersonDetails()
# #P1.TestAppp()               




class Test:
    name="Viren More"
    def demo(cls):
        cls.name="Pravin"
        print(cls.name)



t1=Test()
print(t1.name)
t1.demo()