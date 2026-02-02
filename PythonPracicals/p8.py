# even or odd
'''num=55
if num%2==0:#false 1(empty) #True >
    print("This is even:")
    print("This is if statment")
else:
    print("This is odd:")
    print("This is false statement:")
    
no1=55
no2=55
if no1==no2:
    print("equal:")
else:
    print("not qual:")

no1=60
no2=50
no3=70
if no1>no2 and no2<no3 :
    print("Okk")
else:
    print("Condition false:")
'''
'''
#Q7.Ask the user for their age. Check and print
#whether they are eligible to vote (age ≥ 18).
age=int(input("Enter Any numbeR:"))
if age>=18:
    print("Eligible for voting:")
else:
    print("Not eligible for voting:")
'''
#Q8.Take a number from the user and check if it
#is even by comparing number % 2 == 0.
'''
no=int(input("Enter Any numbeR:"))
if (no%2==0):
    print("It is even:")
else:
    print("it is odd:")
'''
#Q9.Take two inputs and check if both are equal
#using == and !=. # and or
'''
no1=int(input("Enter Any numbeR:"))
no2=int(input("Enter Any numbeR:"))
if no1==no2:
    print("Equal:")
else:
    print("Not Equal:")

#Q15.Ask the user for a string and a character.
#Check whether the character is in the string
#using the in operator.
str1=input("Enter Any String:")
st=input("Enter Any character:")

if st in str1:  print("yes found:")

else:    print("not found:")

#nesting if-else
num1=int(input("Enter any numbeR:"))

if num1>10:
    print("max than 10:")
    if num1>20:
        print("max than 20:")
        if num1>30:
            print("max than  30:")
        else: print("not max than 30:")       
    else: print("not max than 20:")
else: print("not max than 10:")

#Q6.Take two numbers and print
#whether the first
#is greater than, less than, or equal to the
#second.
#a>b and a==b
#else Not Equal Lessa than b
no1=int(input("Enter First No:"))
no2=int(input("Enter Second No:"))
if no1>no2:
    print("max than no2:")
else:
    print("not max than no1:")
if no1==no2:
    print("Equal:")
else:
    print("not equal:")
if no1<no2:
    print("no1 is less than no2:")
else :
    print("no2 is less than no1:")

num1=int(input("Enter The Product Value:"))
if num1>=1 and num1<=4999:
    print("no discount:")
elif num1>=5000 and num1<=10000:
    print("Discount is:",num1-500)
elif num1>=10001 and num1<=30000:
    print("Discount is:",num1-1000)
elif num1>=30001 and num1<=50000:
    print("Discount is:",num1-5000)
else:
    print("no Discount Available:")
'''    

















    


































    
