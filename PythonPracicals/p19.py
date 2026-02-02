''''
#9)Take a number from the user and check
#if it is a palindrome by reversing it using a loop.
no=int(input("Enter any numbeR:"))
n1=no
rev=0
while n1>0:#True 0>0
    rem=n1%10#1%10  ->
    rev=(rev*10)+rem #32*10+1 ->321
    n1=n1//10#123//10 ->
    
if no==rev:
    print("It is palindrome:")
else:
    print("not palindrome")

#10)Print odd numbers in reverse order from 99
#to 1 using a for loop.
for i in range(99,1,-1):#
    if i%2==1:#99%2==1 99/49/2/25/2 13/2 7/2 3/2  1
        print(i,end=" ")

#11)Print a triangle pattern of stars using nested for
#loops. 10 
*
* *
* * *
* * * *
* * * * *
-------------------------------------
for k in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

#13)Print even numbers between 1 to 50,
#skipping odd numbers using continue.
for k in range(0,51):
    if k%2==1:
        continue
    print(k,end=" ")

#14)Take user input repeatedly in a loop and break
#if the user enters 0.
while True:
    no=int(input("Enter Any numbeR:"))
    if no==0:
        break
    print(no)

#15)Find the first number between 1 and 100 divisible
#by both 3 and 7 then break the loop.
for k in range(1,101):
    if k%3==0 and k%7==0:
        print(k)
        break

----------------
while using the always try to take continue end of the line
based on condition or problem

#16)Print numbers from 1 to 50, skipping multiples of
#5 using continue. while loop
j=1
while j<=50:
    if j%5!=0:
        print(j)
    j+=1
    continue

for k in range(1,51):
    if k%5!=0:
        print(k,end=" ")
    continue

#17)Loop through numbers 1 to 10 and use pass when
#the number is 5.

for s in range (1,11):
    print(s)
'''















