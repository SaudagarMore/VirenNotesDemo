#declaration of function
#-----------------------------
#name of function is abcd
'''
def abcd():#function declaration
    #function defined
    print("hii from abcd:")

#function calling
abcd()
abcd()
for k in range(10):
    abcd()

def Calci(a,b,c):#function parameters
    print(a*b*c)#calci logic add (int)


no1=int(input("Enter First numer:"))
# 10 20 30
no2=int(input("Enter Second numer:"))
no3=int(input("Enter Third numer:"))

Calci(no1,no2,no3)#arguments function

print("fsdfsdfsdf")
print("")

return a+b+c+d //function

def hello():
    return "my name is Viren"

print(hello())#function called

#def Demo(a,b):
#    return a*b #40*30 ->1200

#print(Demo("Viren"))
#print("hello")
#print(Demo(40,30))

#print(Demo(20,10))#20*10 ->200

#n1=Demo("Rahul")
#print(n1)



'''
#direct Recursion
'''
def show():#function creation/declaration
    #function defined
    print("hii this is show function:")
    show()

show()#function calling
'''

#indirect recursion

#function 1
def abc(a,c):
    print(a*c)

#function 2
def test():
    print("hii this is from Test")
#    abc(10,30)#10*30 ->300
    abc(10,50)

    

test() #called
































