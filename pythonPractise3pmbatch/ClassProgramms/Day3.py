# operators
# decision making statement

# python looping statement
#for k in range(1,11+1):
#    print(k,end=" ")

#print("-------------------------\n")
#for k in range(0,100+1,+10):
#    print(k,end=" ")
#print("-------------------------\n")

#no=int(input("Enter Any numbeR:"))

#for s in range(1,no+1):
#    if s%5==0:
#        print(s,end=" ")

#for p in range (20,0,-1):
#    print(p)

#python while loop

'''
syntax:
j=1
while(j<=20){
j++/j--
}

while():

1 to 50

list ->
100

5369 ->for loop

+=/-=

print("-----------------while loop-------------------")
no=1 # intialization
num=25    

while(no<=num):#1<=25
    cn=no
    t=1
    while(t<=10):#t
        print(cn*t,end=" ")
        t+=1
    print()
    no+=1
'''
#name="Kavita"
#print(name)

#for d in name:
#    print(d)
#pyton collections framework
#------------------------------------
#list
#1000 ->
'''
la=[10,20,"c","cpp","c",10,50]
print(la)
print(la[3])
print(type(la))
# capital
#append(),max(),min(),sum(),len(),extend(),insert()
'''
Test=[]
Test.append(200)
Test.append(400)
Test.append(200)
Test.append(200)
Test.append(200)
Test.append(250)

Test.extend([150,210,900,980,760])

Test.insert(5,770)

#print("After Added:",Test)
#print("Max Value from list:",max(Test))
#print("Min value From list:",min(Test))
#print("sum of all values from list:",sum(Test))
#print("length of list:",len(Test))
#print("Before Remove:",Test)
j=400
if j in Test:
    Test.remove(j)
#    print(Test)
else:
    print("Value not found into the list:")

print("Before pop:",Test)
#Test.pop(3)
#Test.pop()
#print("After Remove:",Test)

#Test.clear()
#print(Test.index(150))
#print(Test.count(770))
#Test.sort()
#Test.reverse()
#copymylist=Test.copy()
#print("Before Copy:",Test)
#print("After Copy:",copymylist)


#Tuple,set,dictionary

#list()
mytuple=tuple(Test)
myset=set(Test)
print(mytuple)
print(myset)












































