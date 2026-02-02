'''
for j in range(1,21):
    if j==10: # j==11
        pass
    print(j,end=" ")

print("\n===========================")

for j in range(1,11):
    if j==5:
        break
    print(j,end=" ")
print("\n===========================")
for k in range(1,11):
    if  k==6:
        continue
    print(k,end=" ")

no=int(input("Enter Any numbeR:")) #10
#10 ->9
for k in range(1,no):#1 2 3 ..10
    print("squares is:",k*k)
    
#take a number from user and calcualte the sum
#off all digits from 1 to that n number:
#5 1 2 3 4 5 ->15 is sum of digit

no=int(input("Enter any number:"))
add=0
for j in range(1,no+1):
    add+=j

print("The Addition of digit is:",add)
    
#take  number from user (solve using while loop)
#print the how many number 
#are even and odd in 1 to that number...
no=int(input("Enter Any number:"))
even=0
odd=0
for p in range(1,no+1):
    if p%2==0:
        even+=1
    else:
        odd+=1

print("Total Even is:",even)
print("Total Odd Is:",odd)

#12345->5 digit
#2)take  a number from user and count the digit
#from that number  1234 ->4
no=int(input("Enter Any numbeR:"))
count=0
#no=3456
while(no>0):#3456   ->3456>0 true/false 345>0 true/false 34>0 true/false 3> 0>0 true/false
    no=no//10 # 345=3456//10 -> 345 ->345//10 ->34 ->34//10 ->3 3//10 ->0.0
    count+=1 #count=1 ->count2 ->count3 ->count=4
    
print("The Total Count of that number is:",count)
'''
#3)take  a number from user and print the reverse of that number 1234 ->4321
no=int(input("Enter any numbeR:")) #no->98652   ->2
rev=0
while(no!=0):
    d=no%10 #12.3 
    rev=(rev*10)+d
    no=no//10

print("The Reverese Number is:",rev)































































