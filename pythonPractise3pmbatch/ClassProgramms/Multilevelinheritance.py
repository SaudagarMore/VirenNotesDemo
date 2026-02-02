class Account:#parent class
    def __init__(self,accno,accholdername):
        self.accno=accno
        self.accholdername=accholdername
    
    def Show_Account_details(self):
        print("The Account no is:",self.accno)
        print("The Account holder name is:",self.accholdername)

class SavingAccount(Account):#Parent1 inherit into child1
    def __init__(self, accno, accholdername,balance): #2000
        
        Account.__init__(self,accno,accholdername)
        self.accbalance=balance
    
    def Deposit(self,amount): #500
        self.accbalance+=amount #200+=500 ->2500
        print("Bank Total Amount:",self.accbalance)

class PremiumSavingAccount(SavingAccount):
    def __init__(self, accno, accholdername, balance,rewardpoint=0):
        SavingAccount.__init__(self, accno, accholdername, balance)
        self.rewarpoints=rewardpoint
                    
    def Add_reward(self):
        reward=int(self.accbalance*0.01)
        self.rewarpoints+=reward
        print("Reward Adding into the Account balance:",reward,"And Total Reward Points :",self.rewarpoints)
    
    def Show_Full_Details(self):
        self.Show_Account_details()
        print("Balance:",self.accbalance,"Reward points:",self.rewarpoints)

p1=PremiumSavingAccount("1111","Viren More",5000)
p1.Deposit(5000)#7000 70
p1.Show_Account_details()
print("--------------------------")
p1.Add_reward()
p1.Show_Full_Details()        
print("--------------------------")        