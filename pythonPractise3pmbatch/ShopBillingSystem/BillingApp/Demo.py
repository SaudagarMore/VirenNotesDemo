# mydata1=[('ab',10),('cd',10)]
# mydata1.append(('ef',20))
# print(mydata1)
import  datetime

filename = f"mydate_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

filename1 = datetime.datetime.now()
print(filename1)
mydata={'a':10,'b':20,'c':15,'d':35} #product List


mycart=[] #cart List

while True:
    c=input("Enter Which Product You Want To Cart:") # d
    if c in mydata.keys():
        key=c
        value=mydata.get(c)
        mycart.append((key,value))
        print(mycart)
    else:
        print("Not Present")
