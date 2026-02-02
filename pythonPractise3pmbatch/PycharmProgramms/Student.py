#class Declared
#self
class Student:
    #class data method
    def CalculateInterest(mydata,PrincipalAmount,Intertestrate,InterestTime):
        mydata.Amount=PrincipalAmount
        mydata.interestRate=Intertestrate
        mydata.interestTime=InterestTime

    def CalciInterest(self2):
        print("Pricipal Amount (Thousands) ",self2.Amount,"Interest Rate (%) ",self2.interestRate,"Interest Time (Years) ",self2.interestTime)

        Si=(self2.Amount*self2.interestRate*self2.interestTime)/100
        return Si

    def AddStudent(self,sid,sname,sfees,ssubject,smarks):
        self.studentid = sid     #studentid ->class data members/variable
        self.Name=sname
        self.fees=sfees
        self.subject=ssubject
        self.mark=smarks

    def DisplayStudent(self):
        print("Student id is:",self.studentid)
        print("Student Name is:",self.Name)
        print("Student Fees is:",self.fees)
        print("Student Subject is:",self.subject)
        print("Student Mark is:",self.mark)

S1=Student()
PrincipalAmount=int(input("Enter Principal Amount:"))
Intertestrate=int(input("Enter Interest Rate:"))
interesttime=int(input("Enter Interest Time:"))

S1.CalculateInterest(PrincipalAmount,Intertestrate,interesttime)

print("Total Simple Interest is:",S1.CalciInterest())
print("--------------------------------------------------------------------")
S1.AddStudent(101,"Virat",10000,"Python Programming",78)
S1.DisplayStudent()
