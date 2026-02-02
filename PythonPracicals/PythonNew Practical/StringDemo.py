#str1='he llo '
#str2="WELCOmE in python Programming"
# str3=''' python programmming ''' #""""
# str4="""new String """
# print(str1," ",str2," ",str3," ",str4)
#len()  lower() upper()  replace() find() count()

# print("length of string is:",len(str1))
# print("Upper Case is:",str1.upper())
# print("lower case format is:",str2.lower())
# print(str2)

# print(str2.replace("python","java"))

#print(str2.find("in"))

#print(str2.count('m'))

# print("String Method is",str1.strip())

# print("After Strip length is:",len(str1))

# split()  join() capitalize() title() startswith()
# str5="   Pravin        "
# ld=list(str5)
# print(ld)
# print("Before Strip:",str5," ",len(str5))
# str6=str5.strip()
# print("After Strip:",str6," ",len(str6))
# str7=str5.lstrip()
# str8=str5.rstrip()
# print("After Strip:",str7," ",len(str7))
# print("After Strip:",str8," ",len(str8))

#ab="Pratik            aniket pravin pradip viren rahul rohit"

#cd="java"

#list1=ab.split(" ")

# print(ab.split(" "))
# print(list1)
# for j in list1:
#     print(j)

std="hello"
std1="Djano"
std2="Python support to ml"

newstring="  , ".join([std,std1,std2])

print(newstring)

#print(std.join([" django "," tkinter"]))
#name="python supports to web development"
# print(name.capitalize())
# print(name.title())
# print(name.startswith('python'))
# print(name.endswith('development'))

alpha="abcd"
alpha1="12345"
alpha2="abcd1234"

print(alpha.isalpha())
print(alpha1.isnumeric())
print(alpha2.isalnum())

digit="123456"

print(digit.isdigit())
dba="Python Is pOrtable Programming language"
print("Before:",dba)
print(dba.swapcase())

print(dba.index('h'))












