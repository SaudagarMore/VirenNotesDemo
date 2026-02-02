no=50
class Student:
    mydata=500 #instance variable Class Varialbe
    #static method
    def Adddata(self,sname):
        num1=globals()['no']
        sname1=sname
        print(sname1)
        print("gloal variale value:",num1)
      #  print(Student.mydata)
 
    @staticmethod
    def Statmethod(myno):
        mydata=myno
      #  print(mydata)

        
    #instanc method
    def showdata(self,sfees):
        sfee=sfees
        print(sfee)
    
s1=Student()
s1.Adddata("Kumar")        
s1.showdata(500)
Student.Statmethod(200)