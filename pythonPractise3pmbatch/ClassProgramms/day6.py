'''
#print() 
#function Declared

#parameterized function
def Calci(a,b):#function Parameters
    #function defined null null 
    print(a+b)#a+b ->

Calci(10,20) #funcation Called
Calci(30,40) # funcation called
Calci(40,70)

#non parameterized function
def hello():
    print("it is hello function")

#hello() #function

print("---------------------------------")
def mydata(pid,pname,page,psalary):
    name=input("Enter Person Name which you want to find")
    print("person name is:",name)
    if pname=="Rutik":
        print(pid)
        print(pname)
        print(page)
        print(psalary)
    else:
        print("person details not found")

mydata(101,"Rohit",25,25000)

print("----------------------------------")
def SI(amount,rate,time):   
    si=(amount*rate*time)/100
    print("The Simple Interest is:",si)
    print("Payable Total Amount:",amount+si)

amount=int(input("Enter Principle Amount:"))
rate=float(input("Enter Rate of Interest:"))
time=int(input("Enter Duration of Time into years:"))

SI(amount,rate,time) #function Called

def CalciMulti(no1,no2):#parameter created
    return no1*no2 # 5*6 ->30 CalciMulti=30

print(CalciMulti(10,20))

result=CalciMulti(5,6) #arguments passed no1=5 no2=6
print("Total Multiplication is:",result)

#indirect recursion function
def d1(a):
    print(a*a*a)

def d2():
    print("This is second function")

def d3():
    d2()
    print("This is third function")


d1(6)
d3() #function called

#filter
#iterale object list

def FilterEvenlist(n):
    if n%2==0:
        return n

def FilterDivisiobleBy3(no):
    if no%3==0:
        return no
    
mydata=[10,45,98,66,32,71,8,59,67,23,58,49,64,10,12,18,33,39]

filteredevenlist=list(filter(FilterEvenlist,mydata))
filterdivisibleby3=list(filter(FilterDivisiobleBy3,mydata))

print("Even list is:",filteredevenlist)
print("Divisible by 3 values are:",filterdivisibleby3)

# yield ->return

def printable(num):
    for k in range(1,11):
        yield num*k #25 ,50,...250


print(list(printable(10)))

for value in printable(25):
#    print(value)
'''
def calci(no):
    return no*no

data=[10,20,30,40,50]

mysquarelist=(list(map(calci,data)))

print("Square list is:",mysquarelist)






























