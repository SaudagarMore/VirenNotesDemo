#5)Write a program to input a character and
#check whether it is a vowel or a consonant.
'''
a=input("Enter Any Character:")
vowel='aeiouAEIOU'
'''
# a e i o u ('Vowel')
'''
if a=='a' or a=='e' or a=='i' or a=='u' or a=='A' or a=='E' or a=='I' or a=='U':
    print("This is vowel")
else:
    print("This is consonant")

if a in vowel:# o "aeiouAEIOU
    print("Yes Vowel")
else:
    print("Its consonant")
'''
'''
8)Write a program that checks if a person is eligible for a job based on the following conditions:
Age must be above 18 and below or equal to 60.
If the age condition is satisfied, then check gender:
If male → eligible
If female → eligible only if marital status is "unmarried"
Other genders → not eligible
'''
'''
8)Write a program that checks if a person is eligible for a job based on the
following conditions:
----------------------
Age must be above 18 and below or equal to 60.

If the age condition is satisfied, then check gender:
If male → eligible
If female → eligible only if marital status is "unmarried"
Other genders → not eligible
'''
'''
Name=input("Enter name of person:")
Age=int(input("Enter Any Age:"))
gender=input("Enter Your GendeR:")
status=input("Enter marrital Status:")

#female
if Age>18<=60 and gender=='male':
    print("Eligible")
elif Age>18<=60 and gender=='female' and status=='unmarried':
    print("Eigible:")
else:
    print("Not eligible:")
    
'''
year=int(input("Enter Any Year:"))
if year%4==0:
    print("Yes This is leap year:  ",year)
else:
    print("not this is not leap year:  ",year)










