# #positional Arguments
# def ab(n1,n2):
#     print(n1+n2)

# ab(10,20)

# #Required Arguments
# def cd(no1,no2,no3):
#     return no1*no2*no3

# print(cd(20,30,8))
    
# #default Arguments
# def dt(m1=5,n2=10):# reinitialization n=5 10
#     print(m1+n2)

# dt()#positional +default

# #Keyword Arguments
# def Demo(n1=65,n2=20):
#     if n1>n2:
#         print(n1, "is max")
#     else:
#         print(n2,"is max")
        
# Demo(n1=5,n2=10) #keyword arguments
# #key word arguments
# def MyCityname(a,b):
#     print(a+b)

# MyCityname(a="karvenagar",b="pune",)

#variable lenth and keyword arguments
# def DisplayNames(*name):
#     print(name)
    
# DisplayNames("php","c","cpp","java","python")
# def td(a,*b):
#     c=a,sum(b)
#     print(c)
    
# td(20,40,50,30)

# def varlength(*no):
#     print(no)

# varlength(20,55,66,98,74,12,36)

#positional kwrs (keywrds arguments)
def PrintData(**mydta):#dicationary
    print(mydta)
    print(mydta.get("age"))
    
PrintData(name="Viren",age=26,class1="MCA")

