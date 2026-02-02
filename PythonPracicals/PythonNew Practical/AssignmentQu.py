#7)Create a function is_even(num) that returns True if the number is even,
# otherwise False.

#8)write a function get_grade(marks) that returns "Pass"
# if marks >= 40 else "Fail".

# def is_even(num):
#     if num%2==0:
#         print(True)
#     else:
#         print(False)
    
# is_even(22)# called

# def get_grade(marks):
#     if marks>=40:
#         return "pass"
#     else:
#         return "Fail"

# no=int(input("Enter Your Grande marks:"))
# print(get_grade(no))

# 12)Write a function power(base, exponent) that calculates base^exponent.
# Get both values from user input.

# def power(base,exponent):
#     print(base**exponent)

# power(5,4)

# 9)Write indirect recursive functions functionA(n) and functionB(n) to print
# numbers from n to 0.

# 10)Use indirect recursion to calculate factorial of a number using fact1(n) 
# and fact2(n).

# def funcA(n):
#     for s in range(n,0,-1):
#         print(s,end=" ")

# def funB(b):
#     funcA(b)

# funB(20)

# def fact1(n):
#     factcalci=1
#     for s in range(1,n+1):
#         factcalci=factcalci*s
#     print("Factorial is:",factcalci)

# def fact2(n):
#     fact1(n)

# no=int(input("Enter No For Calcualte Factorial:"))
# fact2(no)    


# 14)Write a function vowel_count(word) that returns the count of vowels in the string.
# Get the string from user input.
# def vowel_count(word):
#     cn=0
#     for words in word:
#         if words in 'aeiouAEIOU':
#             cn+=1
#     print("Tota Vowel is in string :",cn)

# string=(input("Enter Your String:"))
# vowel_count(string)

#16)Write a function remove_duplicates(lst) that removes duplicates from a list.

# def remove_duplicates(mydata):
#     print("Unieque list:",set(mydata))

# mydatalist=[10,25,10,25,30,63,25,40,10,25,30,85,22,96]
# print("with Duplicates:",mydatalist)
# remove_duplicates(mydatalist)

#17)Write a function count_even_odd(numbers) that returns a 
# tuple with counts of even and odd numbers.

# def count_even_odd(numbers):
#     evenlist=[]
#     oddlist=[]
#     for j in numbers:
#         if j%2==0:
#             evenlist.append(j)
#         else:
#             oddlist.append(j)
    
#     print("Even Counted Tuple is:",sum(tuple(evenlist)))
#     print("odd Counted Tuple is:",sum(tuple(oddlist)))


# listdemo=[20,50,30,11,16,48,79,63,15,24,28,79,65,43,52,67,12,10,587,54,74]

# count_even_odd(listdemo)


# 18)write a function is_palindrome(word)
# that returns True if the word is a palindrome (reads the
# same forwards and backwards).

# def is_palindrome(word):   
#     if word==word[::-1]:
#         return True
#     else:
#         return False
# a = (input('enter a word:'))#NAYAN ->nayan
# print(is_palindrome(a))
#20)Write a function common_elements(list1, list2)
#that returns a list of common elements between two lists.

def common_elements(list1,list2):
    return list(set(list1)&set(list2))

        
    
    
mylist=[10,20,30,40,50,60,10,20,30,40,89,96,96,33,45,78,45]
mylist1=[16,22,35,44,50,60,10,20,30,40,89,96,96,33,45,78,45]

print(common_elements(mylist,mylist1))