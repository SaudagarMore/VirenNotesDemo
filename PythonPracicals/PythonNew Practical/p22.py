#symmetric_difference ->it is return the symmetirc difference between two sets
#in that both sets not matched values will print

#issubset ->true
#issuperset ->true/false 
#isdisjoint  True/False boolean method

'''
seta={20,60,50,88,963,64,22}
setb={25,60,53,48,965,64,22}
print(seta)
print(setb)
print("----------------------------------")
setc=setb.symmetric_difference(seta)
print(setc)

seta={10,20,30,40,50}
setb={25,30,10,20,30,40,66,50,90}

print(setb.issubset(seta))

s1={10,20,30,40}
s2={10,20}
print(s2.issuperset(s1))

c1={2,6,5,9,3}
c2={15,8,90,1,7}

print(c1.isdisjoint(c2))

user=input("Enter True /False Value:")

if user=="True":
    userbool=True
elif user=="False":
    userbool=False
else:
    print("Invalid Value:")

print("boolean Result is:",user)


no=int(input("Enter any number:"))
#ab=True #False
cn=0
if no<0:
    print("Not primce not number :")
else:
    for k in range(1,no+1):
        if no%k==0:
            print(k)
            cn+=1

if cn==2:# ->>>>>     if(true/false)-> ab==True
    print("Yes prime number:")
else:
    print("not prime:")
    '''

no1=int(input("Enter any number:"))
if no1>1:
    for s in range(2,no1):
        if no1%s==0:
            print("is not prime")
            break
    else:
        print(no1,"yes it is prime")
else:
    print(no1 ,"is not prime number:")







































































