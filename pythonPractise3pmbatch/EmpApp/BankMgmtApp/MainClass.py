import random
from random import randint
from BankMgmtApp import  AccountCreation

class MainAccountClas:
    def TakeAccInputs(self):
        self.Accid=int(input("Enter Account ID: "))
        self.Accname=input("Enter Account Name: ")
        self.Accbal=int(input("Enter Account Balance: "))
        self.Accno=random.randint(11111,99999)
        self.Acccontact=input("Enter Account Contact Number: ")
        self.Accaddress=input("Enter Account Address: ")
        self.AccinterRate=int(input("Enter Account Inter Rate: "))
        self.Acctype=input("Enter Account Type:")

    def WrtieFile(self):
        pass

    def ReadFilf(self):
        pass

    def AccountAppOption(self):
        print("1 st for Account Creation")
        print("2 st for Account Details Views")
        no=int(input("Enter Your Choice:"))
        if no==1:
            self.TakeAccInputs()
            p1=AccountCreation.Personal(self.Accid,self.Accname,self.Accbal,self.Accno,self.Acccontact,self.Accaddress,self.AccinterRate,self.Acctype)

            print(p1.DisaplyAccountHolderDetails())

        elif no==2:
            def GetData(self):
                self.readFile()

Main=MainAccountClas()
Main.AccountAppOption()