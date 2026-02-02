'''
set1={5,6,9,8,35,26,41,87}
print(type(set1))
print(set1)
set1.add(96)
print("After Add",set1)
myset=frozenset([10,20,30,40,50])

print(max(myset))
print(len(myset))
print(min(myset))
print(sum(myset))

myconvertedset=set(myset)

print(type(myconvertedset))
print(myconvertedset)
print(myset)
print(type(myset))

La=[20,54,63,98,75]
print(La)
copy=La.copy()#shallow Copy
print("Copied List:",copy)
La.pop()
print(La)
print(copy)
copy.append(150)
print(La)
print(copy)
'''

#-------------------------------

import copy
'''
original = [10,20,30,40,50]

copy1=copy.copy(original)
print(original)
print("Shallow Copy:",copy1)
print("----------------------------")
copy1.clear()
print(original)
print("Shallow Copy:",copy1)
'''

'''
original1 = [10,20,30,40,50,60]
copy2=copy.deepcopy(original1)
print(original1)
print("deep Copy:",copy2)
copy2.clear()
print(original1)
print("deep Copy:",copy2)

import copy

original = [[1, 2], [3, 4]]
original.append([9,6])

#sublist

dt=[[10,20,30],[40,50,60],[70,80,90],[100,110,120]]

shallow_copy = copy.copy(original)

deep_copy = copy.deepcopy(original)

original[0][0] = 99
original[2][0] = 330

print("Original:", original)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)
'''
original = [10,20,30,40,50,60]
sb1=original[0:3]#0 1 2
sb2=original[3:6]#3 4 5
sb3=[]
sb3.extend([sb1,sb2])
print(sb3)


















