class Person:
    num=25 #class variable
    def mydata(se,pid,pname,page):
        no=100 #Local Variable 
        se.pid=pid # instance variable
        se.pname=pname
        se.page=page

    def dispalypersondetails(se):
        print(se.pid," ",se.pname," ",se.page)

p1= Person()
p1.mydata(101,"Rohit",25)
p1.dispalypersondetails()
        
