#2.Q: Create a set of vowels {‘a’, ‘e’}. Ask the
#user to input multiple vowels (comma-separated),
#convert them into a list, and update the set.
#Display the result.
'''
vowels={'a','e'}
j=0
while j<=2:
    vowel=input("Enter The Vowel: ")
    vowels.add(vowel)
    la=list(vowels)
    j+=1

print("set data:",vowels)
print("list data:",la)

#9. Q: Ask the user to enter two sets
#(comma-separated). Find and print their
#intersection.
seta={0,}#dictionary
setb={1,}

for j in range(1,5):
    num1=int(input("Enter First Set:"))
    seta.add(num1)
print("-------------------------------------")
for j in range(1,5):
    num1=int(input("Enter Second Set:"))
    setb.add(num1)

print("Default seta is:",seta)
print("Default setb is:",setb)
setc=seta.intersection(setb)
print("-------------------------------------")
print(seta)
print(setb)
print(setc)

#12. Q: Ask the user to enter two sets.
#Check if the first is a subset of the
#second using issubset().

seta=[]#dictionary
setb=[]

for j in range(1,8):
    num1=int(input("Enter First Set:"))
    seta.append(num1)
print("-------------------------------------")
for j in range(1,5):
    num1=int(input("Enter First Set:"))
    setb.append(num1)

myset=set(seta)
myset1=set(setb)

print(myset1.issubset(myset))
'''
#print(seta.issubset(setb))

#15. (Combination of Methods)

'''
Q: You have two sets:
registered = {'Rohit', 'Rahul', 'Pravin'}
attended = {'Pravin', 'Kumar', 'Rohit'}
Add 'David' to registered
Find attendees who were not registered

Find common members (intersection)

Check if all attendees are part of registered

registered = {'Rohit', 'Rahul', 'Pravin'}
attended = {'Pravin', 'Kumar', 'Rohit'}
registered.add('David')
notregistered=attended.difference(registered)
commonmember=attended.intersection(registered)
print(registered)
print(attended)
print(notregistered)
print(commonmember)
print(registered.issubset(attended))
'''
