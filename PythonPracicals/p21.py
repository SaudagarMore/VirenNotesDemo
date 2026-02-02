#add ->can add multiple single value
#update ->update the set data of can extend value
#remove-> if value not found it will give error
#discard-> if value not found it will not show error
#pop ->it remove first value
#clear ->clear all values
#copy ->copy into another set
#union ->merge two set 
#intersection ->show the common value from two sets
#difference ->show the difference from selected set..
#symmetric_difference ->show the diffrence values from both sets...

#ab={10,20,50,60,80,90,30,70,60}
#ab.add(500)
#ab.add(690)
#ab.add(870)
#print(ab)
#ab.update([52,38,41,96])
#print(ab)
#ab.remove(80)
#print(ab)
#ab.discard(9600)
#print("After Discard value:",ab)
#ab.pop()
#print("After Pop:",ab)
#ab.clear()
#print("Before Copy:",ab)
#cpy=ab.copy()
#print("After Copy:",cpy)
'''
union
sd={20,50,60,30,80}
nm={80,40,50,75,26}
print("First set:",sd)
print("Second set:",nm)
print("--------------------------------")
un=sd.union(nm)
print("First set:",sd)
print("Second set:",nm)
print("New Set:",un)

#intersection
sd={20,50,60,30,80}
nm={40,52,75,26,23}
print("First set:",sd)
print("Second set:",nm)
print("--------------------------------")
un=nm.intersection(sd)
print("First set:",sd)
print("Second set:",nm)
print("New common set:",un)

#difference
cd={20,56,30,98,65}
rt={25,63,30,20,112,56}
print("First set:",cd)
print("Second set:",rt)
print("--------------------------------")
newset=rt.difference(cd)
print("First set:",cd)
print("Second set:",rt)
print("new difference set:",newset)

#symmetric_difference
cd={20,56,30,98,65}
rt={25,63,30,20,112,56}
print("First set:",cd)
print("Second set:",rt)
print("--------------------------------")
newset=cd.symmetric_difference(rt)
print("First set:",cd)
print("Second set:",rt)
print("new difference set:",newset)
'''









#exit(0)
