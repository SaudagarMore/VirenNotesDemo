#clasa Declared
class MyTest:
    #default constructor
    def __init__(self):
        print("Default Constructor")

    #Parameterize Constructor
    def __init__(self,pid,pname):
        self.pid = pid
        self.prdname = pname
        print(self.pid," ",self.prdname)

    def show(self):
        print("i am from show method")

m1=MyTest(1010,"Realme")
m2=MyTest(1011,"oppo")
m1.show()