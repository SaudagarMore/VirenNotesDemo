'''
mylist=[]
for k in range(1,6):
    no=int(input("Enter Any numbeR:"))
    mylist.append(no)

print("My default listis:",mylist)
mylist.pop()
print("After delete using pop:",mylist)

mylist=[]#empty list

for k in range(1,6):#12345
    no=int(input("Enter Any numbeR:"))
    mylist.append(no) # 20 54 63 98 74
index=int(input("Enter Any index for remove value:")) #17 20
length=len(mylist)

if index>length:
    print("cant delete bcoz element not present into that index:")
else:
    mylist.pop(index)
    print("After Removing value using user index :",mylist)

#() []
mydata=["C","CPP","JAVA","C","CPP","JAVA","PYTHON","C"]
dt=mydata[0]
print(dt)
#print(mydata.index(dt))
print(mydata.count(dt))

num=[25,36,98,65,36,78]
print("Original:",num)
num.sort()
print("In Ascending Sort:",num)
num.reverse()
print("After Rerversed Sorting:",num)

mylist1=[]
for j in range(1,4):
    n1=int(input("Enter Any numbeR:"))
    mylist1.append(n1)

print("With out copy:",mylist1)
mycopy=mylist1.copy()
mycopy.pop()
print("After pop:",mycopy)
print("My list:",mylist1)
print("------------------------")
print("After Copy:",mycopy)
print("Sum is:",sum(mycopy))
print("min is:",min(mycopy))
print("max is:",max(mycopy))
print("length is:",len(mycopy))

mycopy=[]
num2=int(input("Enter Any Numer for size of list:"))
for j in range(1,num2+1):
    n1=int(input("Enter Any numbeR:"))
    mycopy.append(n1)
print("Sum is:",sum(mycopy))
print("min is:",min(mycopy))
print("max is:",max(mycopy))
print("length is:",len(mycopy))
'''






























