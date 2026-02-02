#example of Python Compile/Method overloading polymorphism..
class ABCD:
    def Show(self):
        print("hello This is Show Method")

    def Show(self,name):
        self.name=name
        print("hello This is second Show Method",self.name)

    def Show(self,name,surname):
        self.name=name
        self.surname=surname
        print("hello This is third Show Method",self.name,self.surname)

ab=ABCD()
ab.Show("Viren","More")
ab.Show("Ravi","Pawar")