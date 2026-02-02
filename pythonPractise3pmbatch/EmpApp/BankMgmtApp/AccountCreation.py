'''

'''
from BankMgmtApp.AccountHolder import AccountHolder
class SavingAccount(AccountHolder):
    def __init__(self,Accid,AccName,Accno,Acccontact,AccAddress,AccinterRate=5,Acctype="Saving"):
        super().__init__(Accid, AccName, Accno, Acccontact, AccAddress, Acctype)
        self.accinterRate = AccinterRate #intsnace variable

    def Deposit(self):
        amount=int(input("Enter Deposit Amount:"))
        self.AccBal+=amount
        return  "Now Acc Balance Is:",self.AccBal

    def Withdraw(self):
        amount=int(input("Enter Withdraw Amount:"))
        self.AccBal-=amount
        return  "Now Acc Balance Is:",self.AccBal

    def CalculateInterest(self):
        Interest=(self.AccBal*self.accinterRate)/100
        return  "Interest Rate is:",self.AccBal+Interest

class CurrentAccount(AccountHolder):
    def __init__(self,Accid,AccName,Accno,Acccontact,AccAddress,AccinterRate,Acctype="Current"):
        super().__init__(Accid, AccName, Accno, Acccontact, AccAddress, Acctype)
        self.accinterRate = AccinterRate

    def CalculateInterestRate(self):
        Interest = (self.AccBal * self.accinterRate) / 100
        return "Interest Rate is:", self.AccBal + Interest

class Personal(AccountHolder):
    def __init__(self,Accid,AccName,Accbal,Accno,Acccontact,AccAddress,AccinterRate,Acctype):
        super().__init__(Accid, AccName,Accbal,Accno, Acccontact, AccAddress,Acctype)
        self.accinterRate = AccinterRate

    def CalculateInterestRate(self):
        Interest = (self.AccBal * self.accinterRate) / 100
        return "Interest Rate is:", self.AccBal + Interest
