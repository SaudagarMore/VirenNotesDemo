# list1=[20,55,63,98,74,52,63,4,5,2,9,88,74,51,63,14,52,63]

# print("Number List:",list1)

# def filteronlyeven(m):#m=[20,55,63,98,74,52,63,4,5,2,9,88,74,51,63,14,52,63]
#     return m%2==0 #

# def filteronlygreterthan30(m):
#     return m>30

# filterdata=filter(filteronlyeven,list1)
# print(type(filterdata))

# filterdata1=filter(filteronlygreterthan30,list1)

# mydata,mydata1=list(filterdata,filterdata1)
# #mydata1=list(filterdata1)

# print("Even list")
# print(mydata)

# print("max than 30 list")
# #print(mydata1)


# Map Function in python
# Testlist=[5,6,8,6,4,9]

# def square(k):
#     return k**3

# squaredlist=map(square,Testlist)

# print("Square of Number:",list(squaredlist))
# print("----------------------------")

#python lambda expression/function
    
Test=lambda a,b: a+b

#checkeveodd=lambda no1: no1%2==0, "Even", "odd"
message=lambda: print("lambda Expression Called")   

calci=lambda p,q:min(p,q)


print(Test(20,30))
#print(message())
print(calci(20,30))

# filter ->it is a predefined function in python which can use for 
# filter data from using colleteion,iterable object(list,tuple,set) 
# using the set of fuction logic filter can only filter data based on function
# condition ....

# map ->map is a predefined function in python which is used to perform the 
# arithmatic and basic logical operation with iterabel oject collcetions
# element it can work on individual value and perform the result and store into the 
# same function and that function create in map object 
# you must need to print the convert map object into the list object or
# can print using for loop iteration

# lambda ->lambda is single line basic expression/function which can use for perform the basic operation 
# lambda didnot work will decision and looping statmnet can dont support to python advanced features
# mostly it run on single line code lambda it is part of function type it can use for short operation 
# and most of the call into the print function.......












