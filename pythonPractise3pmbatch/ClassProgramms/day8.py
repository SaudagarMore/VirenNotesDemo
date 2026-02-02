#python Array#-------------------
#import array  as k
#() rounded brcker
#[]
#{}

#this is initialized array
# mydata=k.array('i',[10,20,30,40,98,65,74,30,0,-2]) #interger arrray

# mydata1=k.array('i',[])#This is empty array

# floatarray=k.array('d',[20.5,30.4,55.2,10.4,99.6])
# print(type(mydata))

# print("My Integer Array is:",mydata)
# print("My Float Array is:",floatarray)

# int ->int ,short,long
# float ->float,double
# str  char,string
# bool ->boolean

# import array
# # Dictionary of typecodes and example values
# arr1=array.array('b', [-10, 0, 10]) # signed char (int)
# arr2=array.array('B', [0, 10, 255])              # unsigned char (int)
# arr3=array.array('u', ['a', 'b', 'c'])           # Unicode characters
# arr4=array.array('h', [-1000, 0, 1000])         # signed short (int)
# arr5=array.array('H', [0, 1000, 65535])      # unsigned short (int)
# arr6=array.array('i', [-100000, 0, 100000])      # signed int
# arr7=array.array('I', [0, 100000, 4294967295])   # unsigned int
# arr8=array.array('l', [-100000, 0, 100000])   # signed long (same as int on many systems)
# arr9=array.array('L', [0, 100000, 4294967295])   # unsigned long
# arr10=array.array('q', [-10**12, 0, 10**12])    # signed long long
# arr11=array.array('Q', [0, 10**12, 2**64 - 1])    # unsigned long long
# arr12=array.array('f', [1.5, 2.5, 3.5])           # float
# arr13=array.array('d', [1.123456789, 2.987654321]) # double

# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)
# print(arr6)
# print(arr7)
# print(arr8)
# print(arr9)
# print(arr10)
# print(arr11)
# print(arr12)
# print(arr13)
import array as arr
myarry=arr.array('i',[])
myarry.append(50)
myarry.extend([10,20,30,88,75,50,50,41,63,98])

# for k in myarry:
#     print(k)

# print("----------------------------")
# for index in range(0,myarry.__len__()):
#     print(index,end=" ")
    
# no=int(input("Enter Any Value fro store into the arry:"))
# myarry.append(no)

print("After Inserting Array:",myarry)

#myarry.insert(2,96)
#print("After inserting array into the index:",myarry)

#myarry.remove(50)
#print("After Remov:",myarry)
# myarry.pop()
# myarry.pop()
# print("After Pop:",myarry)
#myarry.clear()
#print("After Clear:",myarry)

# print("The index position of the value is:",myarry.index(88))
# for k in myarry:
#     if k==88:
#         print(myarry.index(k)+1)

# print("Total Counted Value is:",myarry.count(50))

# myarrycopy=myarry.__copy__()
# print("After copy:",myarrycopy)

# print("Total Value stored into the array are:",myarry.__len__())
# print("get Item  is:",myarry.__getitem__(1))

# for j in range(0,myarry.__len__()):
#     print(myarry.__getitem__(j))

# myarry.__setitem__(3,38)
# print("After Changing array value:",myarry)

# myarry.__delitem__(5)
# print("Afte Deleting index vlaue of the arry:",myarry)

# search=int(input("Enter Number Which you want to find into the array:"))
# if myarry.__contains__(search):
#     print("yes value is found")
# else:
#     print("Value not found into the arrray")
for k in myarry:
    print(k)
    
for j in myarry.__iter__():
    print(j)




















