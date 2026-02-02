'''
#18)Take a number from the user and check if
#it is prime using a loop and break when
#divisible.
abc=True
num=int(input("Enter Any numbeR:"))
if num<0:
    print("it is not Valid numbeR:")
else:
    for j in range(2,num):#2,3,,4
        print(j)
        if num%j==0:#20%2==0 True 13%3==1
            abc=False #
            break

if abc==False:
    print("prime numbeR:")
else:
    print("Number not Prime:")

#19)Create a guessing game where the user guesses
#a random number, breaking the loop when guessed
#correctly.
import random
no=random.randint(1,100)#
#use for take random value or digit from random function
while True:
    num=int(input("Enter number which you want to guess:"))
    if num==no:
        print("Yes Number Guess Succesfully",num," ", no)
        break
    else:
        continue

#20)Create an infinite loop that asks for user
#input, uses pass for empty input, and breaks if
#input is "exit"
while True:
    no=input("Enter Any Value:")
    if no=="":
        pass
    else:
        print("Your Name is:",no)
        exit(0)
'''
#exit(0)





    


