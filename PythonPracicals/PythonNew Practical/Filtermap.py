#3)String["Python", "is", "Platform", "independent", "proramming", "language"]
#Given a list of lowercase strings, use map()  to convert all to uppercase.

# def ConvertUpperCase(val):
#     return val.upper()

# String=["Python","is","Platform","independent","proramming","language"]

# myconveredata=map(ConvertUpperCase,String)

# print(list(myconveredata))
#4)create a list as Test[] add 10 string values from user
#and filter only those with more than 5 characters using filter()

# Test=[]
# for j in range(1,10):
#     value=input("Enter five String Values:")
#     Test.append(value)

# def filterthanfivelength(Test):
#     return len(Test)>=5

# Filtereddata=list(filter(filterthanfivelength,Test))
# print("Max than 5 lenth:",Filtereddata)

# 5)Ask the user to input an alphanumeric string. Use filter()  
# to extract all digits from it.

# string=input("Enter Any String:")
# def filteralphanumericdata(string):
#     return string.isdigit()    
    
# filteredstring1=list(filter(filteralphanumericdata,string))
# print("Extracted digit is:",filteredstring1)

#6)Given a list of strings, return a list with all strings reversed using map().
# demo="Virat"
# demo1="ABCD"
# mycopy="".join([demo,demo1])

# strings=["Rohit","Pradip","Rushi","Akash","Ganesh","Amar"]
# #reversed usin Slice
# def reversedusingslice(strings):
#     return strings[::-1]
# #reverse using Join and reversed function
# def ReversedStringFunction(strings):
#         return "".join(reversed(strings))

# myreversedata1=list(map(reversedusingslice,strings))
# print(myreversedata1)

# myreversedata=list(map(ReversedStringFunction,strings))
# print(myreversedata)

#7)Write a generator function that yields numbers from 1 to N (user input).

# def Generatordata(n):
#     for k in range(1,n):
#         yield k

# no=int(input("Enter Any numbeR:"))
# mydata=list(Generatordata(no))
# print(mydata)

#9)Write a generator that yields even numbers up to a user-specified limit/numers.
# def Generatordata(n):
#     for k in range(2,n,2):
#         yield k

# no=int(input("Enter Any numbeR:"))
# mydata=list(Generatordata(no))
# print(mydata)

#10)Write a generator that yields prime numbers up to a user-defined limit/numbers.

# def isprime(n):#100
#     for j in range(1,n+1):#1,100
#         cn=0
#         for o in range(1,j+1):
#             if j%o==0:
#                 cn+=1
#         if cn==2:  
#             yield j

# no=int(input("Enter Any numbeR:"))#100
# mydata=list(isprime(no))#100
# print(mydata)

# #11)Use a generator expression to calculate squares of numbers from 1 to 10.
# def Generatordata(n):
#     for k in range(1,n):
#         yield k*k

# no=int(input("Enter Any numbeR:"))
# mydata=list(Generatordata(no))
# print(mydata)

# #12)Write a generator that yields only numbers divisible by 3 from 1 to N.
# def Generatordata(n):
#     for k in range(1,n):
#         if k%3==0:
#             yield k

# no=int(input("Enter Any numbeR:"))
# mydata=list(Generatordata(no))
# print(mydata)

#13)Write a generator that yields each character of a string (user input) one by one.
# def Generatordata(n):
#     for k in n:
#         yield k

# no=input("Enter Any numbeR:")
# mydata=list(Generatordata(no))
# print(mydata)

#14)Convert a predefined list of items into a generator
# and print all elements one by one.
# def alllistdata(mydata):
#     for j in mydata:
#         yield j

# predefinedlistdata=["C","CPP","JAVA","Python","Php","Perl","Go"]
# printdetails=list(alllistdata(predefinedlistdata))
# for s in printdetails:
#     print(s)

#15)Write a generator that counts down from N to 0 (input from user).

# def CountDown(m):
#     while m>=0:
#         yield m
#         m-=1
        
# num=int(input("enter Any number:"))
# finallist=list(CountDown(num))
# print(finallist)

#8)Write a generator to generate the first N Fibonacci numbers.
