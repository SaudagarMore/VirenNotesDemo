#5)Write a program to input a character and check whether it is a vowel or a consonant.
# aeiou AEIOU constant.

#char=input("Enter any character:")
#data='aeiouAEIOU'

#present=False
#for j in data: #aeiouAEIOU
#    if j==char:
#        print("it is vowel")
#        present=True
#if present==False:
#    print("this is constant")
'''
set1={10,20,33,40,50,60}

set2={10,20,30,50,60,70}
print(set1)
print(set2)

set3=set2.difference(set1)
print("----------------------------")
print(set3)

set4={10,20,33,40,50,60}
set5={10,20,30,50,60,70}
print(set4)
print(set5)
set6=set4.symmetric_difference(set5)
print("-----------------")
print(set6)

#(other_set)
#issuperset(other_set)

#seta={10,20,30,40}
#setb={10,30}

#print(seta)
#print(setb)

#print(setb.issubset(seta))

#print(seta.issuperset(setb))



#setdata1={1,2,3,4,5}
#setdata2={7,8,9,10,11}
#print(setdata1)
#print(setdata2)
#print(setdata1.isdisjoint(setdata2))

'''
#[]
#tule ()
#set {}
#frozenset
#frozenset  ([])
'''
myset=frozenset([10,20,30,40,50,60])

print(myset)
print(type(myset))
mydata=set(myset)

mydata.add(650)

print(mydata)
myvalue=frozenset(mydata)
print(myvalue)
'''
#Mydata={1:"c",2:"cpp","java":500,12.5:950}
#print(Mydata)
#print("----------------")
#Mydata.update({5:"python"})
#print("After adding:",Mydata)
#print(type(Mydata))
#Mydata.clear()
'''
print("Value is:",Mydata.get(2))
print("-----------------------------------")
print("all Key are:",Mydata.keys())
print("-----------------------------------")
print("all data are:",Mydata.items())
print("-----------------------------------")
print("all data are:",Mydata.values())
'''


#Mydata.pop(1)
#print("------------------------")
#print("After Using Pop:",Mydata)
#Mydata.popitem()
#Mydata.popitem()
#print("After popitem:",Mydata)
#Mycopieddict=Mydata.copy()
#print("Copied Dictionary is:",Mycopieddict)

#data={15:10,8:20,35:300,27:50,41:60}

#print(len(data))
#print("minimum key:",min(data))
#print("Maximum key:",max(data.values()))
#print(sum(data))
#print("total is:",sum(data.values()))
'''
print(data.keys())
print(list(reversed(data)))

print(data)
print("converting dictionary into list:",list(data))
print("converting dictionary into list:",list(data.values()))

print("Str conversion:",str(data))

print("-----------------------------")
print("Before Sorted:",data.keys())
print("Sorted key is:",sorted(data))
print("Values are:",data.values())
print("Sorted value is:",sorted(data.values()))
'''
#exit(0)


mydt={1:"c",2:"cpp",3:"java",4:"python",5:"php"}
print(mydt)

#key=int(input("Enter Any Key which you want to find in mydt dictionary:"))

#if key in mydt:
#    print("yes key is present into mydt dicionary")
#else:
#    print("no key is not present into mydt dictionary")

#del mydt
#print("Dictionary delete")
#print("After Delete diconary:",mydt)

pairs=[(1,"c"),(2,"cpp"),(3,"java"),(4,"python")]
print(type(pairs))
print(pairs)

myconverdict=dict(pairs)
print(type(myconverdict))
print("After Converting data:",myconverdict)








































