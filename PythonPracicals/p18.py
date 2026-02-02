'''
#1*2*3*4*5->120

#5)Take a number from the user and calculate its
#factorial using a for loop.
no=int(input("Enter ANy number:"))
fa=1 #0
for k in range(1,no+1):
    fa=fa*k

print("Factorial of ",no,"is",fa)

#6)Display the first 10 Fibonacci numbers using a while loop.
#10 0=0 0+1 ->1
#1+2->3
#3+4->7  7+5->12+6->18+7->25+8->33+9=42+10->52
a=0

first=0
second=1
while a<=9:#1<=10
    print("fibonacci series :",(a+1),"=",first)#0
    calculate=first+second #0+1->1
    first=second #1 first=1 second ->1
    second=calculate#second =>1
    a+=1
    
print(" ")

#7)Take a string from the user and print all characters.
st=input("Enter Any String:")
for i in st:
    print(i)
'''
#8)Take a number from the user and find the sum
#of its even digits using a while loop.
num=int(input("Enter Any number:"))# 12345678 ->
sum1=0
cn=num
while cn>0:
    rev=cn%10
    if rev%2==0:
        sum1+=rev
    cn=cn//10

print("Addition is:",sum1)
