#
#exit(0)
'''
Sid=int(input("Enter Student Id:"))
Sname=input("Enter Studnet Name:")
Smark=int(input("Enter Student Mark:"))
Spercentage=float(input("Enter Student Percentage:"))

print("-----------------Student Details is:--------------")
print("Student id is:",Sid)
print("Student Name is:",Sname)
print("Student Smark is:",Smark)
print("Student Percentage is:",Spercentage,"%")

no1=int(input("Enter First No:"))
no2=int(input("Enter Second No:"))
#/ #// #%(modulus)
# 100 (value) division(10)  reminder=0   division->

print(no1/no2)#division
#print(no1//no2) #division  26-24 ->2
print(no1%no2) # 100%5 -> 0 20
print(no1**no2) #its print the power first value
'''
# = (Assign Operator)
'''
=(Assign operator)
+=(Add And Assign)

== (equal and eqaul)

no=50
no1=no

print(no)
print(no1)

+=

n1=50
n2=25
print(n1+n2)

n1**=5

print(n1)

#n1+=n2


#print(n1+n2)
'''
'''
== (equal Equal opeator)
!= (not Equal operator)
> (greter than)
< (less than operator)
>= (greater than and equal)
<= (less than and equal)

no1=int(input("Enter First:"))
no2=int(input("Enter Second:"))

#print(no1==no2)
#print(no1!=no2)
#print(no1>no2)#true
#print(no1<no2)

print(no1>=no2)
print(no1<=no2)


no1=50
no2=30
no3=65
#and or not // && || !

print(no1>no2 and no2<no3 and no1>=no2)

print(no1<no2 or no2>no3 or no1==no2)
'''
#in ->if value/no is present in sequence or collection it will return true otherwise it will return false.
#not in ->if value/no isnot present in sequence or collection it will return true otherwise it will return false.
'''
La=[10,20,30,40,50,60]
print(98 in La)
name="Kavita"
print('a' in name) 

name1="Pradip"
print('k' not in name1)

#is
#is not
#==

no=100
no1=150

print(no is not no1)

'''
#if statment
'''
if condition:
no=int(input("Enter Any numbeR:"))

if no==20 and no>10 and no<25 and no!=50:#false #True
    print("Yes No is Equal")
else:
    print("No is Not Equal")

no1=int(input("Enter First no :"))
no2=int(input("Enter Second no:"))
if no1>no2:
    print("no1 is max than no2:")
else:
    print("no2 is max than no1:")

#nesting if-else

no1=int(input("Enter Any no:"))

if no1>10:#False
    if no1>20:#True
        if no1>30:#True
            if no1>40:#True
                print("Max than 40:")
            else:
                print("less than 40:")
        else:
            print("less than 30:")
    else:
        print("less than 20:")
else:
    print("less than 10:")
'''
#ladder if-else

no1=int(input("Enter Any number:"))

if no1>=1 and no1<=49:#False
    print("no1 between 1 to 49")
elif no1>=50 and no1<=99: #false
    print("no1 between 50 to 99")
elif no1>=100 and no1<=149:#True
    print("no1 between 100 to 99")
elif no1>=150 and no1<=200:
    print("no1 between 150 to 99")    
else:
    print("value is more than 200:")









































            












































































