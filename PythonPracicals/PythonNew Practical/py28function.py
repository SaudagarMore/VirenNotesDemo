'''
function declaration/creation
function definition
function calling //excute
------------------------------
function with paramter
function with arguments
--------------------------
function with return 

print ->it can pritn  or write the text on output screen
return ->it can return value/data to the self function name.

print("dfgdfg")

return "fjdhfkjg"

def hello(no1,no2):#declare
    print(no1*no2)#definition
    
hello(20,60)#60*20 
hello(60,30)

def db(no3):
    return no3*no3 #5*5 ->25

print(db(5))
a=db(10)#100
print(a)

def show(id,name):
    return id,name

print(show(101,"Pravin"))
print("-----------------------------------")
def printable():
    for k in range(1,51):
        return k

    
#La=printable()
#for s in La:
#    print(s)
print(printable()) #1
print(printable()) #1

print(printable()) #1
print(printable())

#printable()
def mylist(data):#parameter data[100,200,300]
    for s in data:
        return s       
        
    # la=[]
    # for k in range(1,6):
    #     no=int(input("Enter Five Number:"))
    #     la.append(no)
    
    # print("My list is:",la)

sd=[] #list

sd.append(100)
sd.append(200)
sd.append(300)

#print(mylist(sd))
print(mylist(sd))

#mylist(sd)#argument
'''
#function recursion
#---------------------------
'''
i)function recusion/recursive function
i)in that we create function it call itself or any another function
called as function recursion/recursive function..

2)types of recursive function
i)direct recursion
i)in the direct recursion function calls itself /self function
called as function recursion.

ii)indirect recursion
i)in that function calls another function /second
declare function called as indirect recursion function.

def Test(j):#j=7 60
    print(j)
    Test(10)
    # if j<0:#6<1 
    #     return 1
    # else:
    #     return j+Test(j-1) #7*6 ->42*5 ->5+4->       
Test(4)
'''
#indirect recursion
#--------------------------------
def function1(no1): #no1->6
    print(no1*no1)# 6*6 ->36

def function2(no1,no2):
    print(no1+no2)# 5+10 -> 15
        
def function3(no1,no2):#n1=10 ,n2=5, n3=6
    function1(no1)#n3 =>6
    function2(no1,no2)# 5,10
    
    
def Sample(num1):
    p=100
    print(num1," ",p)

def Sample1(num1):
    p=200
    print(num1," ",p)


# no1=int(input("Enter No1:"))
# no2=int(input("Enter No2:"))
# no3=int(input("Enter No3:"))
    
function3(10,5)
Sample(50)
Sample1(250)















