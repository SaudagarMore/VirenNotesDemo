#class declared
class Mobile:
    lounchyear=2025 #class variable/members
    versionupdateyear=0 #2027
    #instance method
    def Add_mobile_Data(UV,mid,mname,mprice):
        mstock=50 #local Variable
        Mobile.versionupdateyear=2027

        #instance variable
        UV.mobid=mid
        UV.mobname=mname
        UV.mobprice=mprice
        print("current product stock is:",mstock)
        print("Mobile Production Year:",UV.lounchyear)
        print("Mobile Version Updated Year:",Mobile.versionupdateyear)
    #instance method
    def Show(self):
        num=20 # local variable
        print("Square is:",num*num)
        print(self.mobid,self.mobname,self.mobprice)

    #instance method
    def Modify(self):
        print(self.mobid,self.mobname,self.mobprice)
        print(Mobile.lounchyear," ",Mobile.versionupdateyear)

    def MyReurnName(self,MynewName):
        self.myname=MynewName
        return "My Office name is:",self.myname

m1=Mobile()
m1.Add_mobile_Data(201,"Moto",15000)
m1.Show()
m1.Modify()
print(m1.MyReurnName("Viren"))