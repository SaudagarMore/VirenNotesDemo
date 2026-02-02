'''
Mydata=[10,20,50,60,877]
print(type(Mydata))
#using print Function
print(Mydata)
#using For Loop
for j in Mydata:
    print(j)
#usin Slicing
# 0 to last
print(Mydata[0:6])
da=[10,20,30,50]
print("addition is:",sum(da))
Marks=[]
print(Marks)
Marks.append(95)
no=int(input("Enter My Marks:"))
Marks.append(no)
for j in range(1,3):
    n1=int(input("Enter Student Marks:"))
    name=input("Enter My Name:")
    Marks.append(n1)
    Marks.append(name)
    
print("After Adding list:",Marks)
print(sum(Marks))
'''

da=[10,20,30,50]

print(da)
da.insert(0,95)
da.insert(3,95)
'''
print(da)
da.remove(30)

no=int(input("Enter Any NumbeR:"))
data=True

for j in da:
    if j==no:#True
        da.remove(no)
        print("YEs Value Remove:")
    else:
        print("No Value not Remove:")

#        data=False

if data:#True False
    print("Number not present into list:")
else:
    print("Number found and delete:")
   ''' 
print(da)
da.append(50)
da.append(50)
da.append(50)
da.append(50)
da.pop(4)
print("After Pop",da)
print(max(da))
print(min(da))
print(len(da))
#da.clear()
print("After Clear:",da)
print(da.index(50))
print(da.count(50))

da.sort()
print("After Sort:",da)
da.reverse()
print("After Reverse:",da)

shallcy=da.copy()
print("Original:",da)
print("Copy",shallcy)
print(len(da))
print(len(shallcy))

shallcy.remove(20)
print("after Revove:",shallcy)
print(da)
print("-------------------------------------------")
mk=[20,60,80,90]

rt=[65,23,88]
sb=[1,9,63,77,88]
print(mk)
mk.extend([20,50,66,88,99,120])
mk.extend(rt)
print("-------------------------")
print("After Extend:",mk)









































