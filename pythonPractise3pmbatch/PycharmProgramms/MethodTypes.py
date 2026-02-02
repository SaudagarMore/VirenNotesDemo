'''
python class members types and class methods types
1)instance variable/members
------------------------------
i)this member create into any method/any constructor but using the self/any object called as instance method
ii)we can use this types of member in all over class..

2)local variable and memeber
i)this members create into the any methods but with out using any object/self
ii)this members can only use in that method in where created..

3)class variables and members
i)this members create outside of the any method but inside of the class.
ii)this members can be use in all over class..
---------------------------------------------
class methods and its types.
----------------------------
1)instance method
i)this method is declared into the class using def keyword but this method parameter must
be have atleast one self/refereve variable name.
ii)this method to call outside of the class we need to create the object of the class
iii)for call to instance method object must required/need.

2)static method
i)this is declared/defined using the def keyword and also for that we need declared
as @staticmethod decoarator on the top the method name this method can default/parameterized
ii)this method can call using direct class name no need creation of object to calling this method.

3)class method
i)it is third types of method in python which is declared using def keyword and also for that
we need declared as @classmethod decorator on the top the method name this method can call
using object or with class name

'''
#class Declared
class Test:
    #instance method //non static method
    def Demo(self):
        print("Demo method")

    def My2ndeDemoMethod(self):
        print("My2ndeDemo method")
        self.Demo()

    @staticmethod
    def Sample(name,age): #static method
        myname=name  #local variable
        myage=age
        print(myname," ",myage)
        print("hii i am static method")

    @classmethod
    def Classmethoddemo(cls,uid,uname,ucontact):# self,cls
        cls.userid=uid
        cls.uname=uname
        cls.ucontact=ucontact
        print(cls.userid," ",cls.uname," ",cls.ucontact)

t1=Test() #object Created
t1.My2ndeDemoMethod() #instance method called
Test.Sample("Viren",26) #static method called
t1.Classmethoddemo(201,"Viren","9307014300")
#Test.Demo() #instance method called