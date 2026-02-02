'''
'''
from BankInterface import  BankMgmt
class AccountHolder(BankMgmt):
    def __init__(self,Accid,AccName,AccBal,Accno,Acccontact,AccAddress,Acctype):
        self.accId = Accid
        self.accName = AccName
        self.AccBal = AccBal
        self.accno = Accno
        self.acccontact = Acccontact
        self.accAddress = AccAddress
        self.acctype = Acctype

    def DisaplyAccountHolderDetails(self):
        return  "Acc Details is:",self.accId,self.accName,self.AccBal,self.accno,self.acccontact,self.accAddress,self.acctype