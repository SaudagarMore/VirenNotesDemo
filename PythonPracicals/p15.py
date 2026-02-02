mytuple=(20,50,633,89,74)
print(mytuple)
mylist=list(mytuple)
mylist.append(87)
mylist.append(96)
mylist.append(38)
print("After Adding Value into the list:",mylist)
tuple1=tuple(mylist)
print("New Updated Tuple is:",tuple1)

#print(type(mytuple))
#print(mytuple)
#print(all(mytuple))
#print(any(mytuple))

'''
print(max(mytuple))
print(min(mytuple))
print(sum(mytuple))
print(len(mytuple))

#print(mytuple.index(20))

#print("Total Count is:",mytuple.count(20))
#print("Assending:",sorted(mytuple))
sort=sorted(mytuple)
print("After assnding sorted:",sort)

reversed1=tuple(reversed(mytuple))
print("After Revered:",reversed1)

#reversed(mytuple)
#print("Descending:",mytuple)

n3=40
if n3 in mytuple:
    print("Yes Value is Present:")
else:
    print("no Value not found:")
'''
#slicing
mydata=[10,20,30,40,50,60,70,80,90]
print(mydata[0::]) #

print(mydata[::-1])
