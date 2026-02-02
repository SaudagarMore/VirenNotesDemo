'''
data=()# data=[]
print(type(data))
mylistdata=list(data)
for j in range(1,5):
    no=int(input("Enter four number:"))
    mylistdata.append(no)

data1=tuple(mylistdata)
print("Minimum value from tuple is:",min(data1))


sd=(10,50,60,33,98,87,52,63) # Tuple
no=63   #int(input("Enter Any number which you want to find:"))
if no in sd:
    print(sd.index(no))
else:
    print("number not found:")
'''
