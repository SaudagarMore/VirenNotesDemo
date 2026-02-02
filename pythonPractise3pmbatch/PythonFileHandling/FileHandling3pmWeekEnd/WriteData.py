#write
#writelines
mydata=open("Testfile.txt","a")
mydata.writelines("\nThis is Python Full Stack !")
mydata.close() #file closed by close function
print("Data Written")
mydata.write("hii")


# if mydata.writable():
#     print("Yes We Can Write Into file")
# else:
#     print("No")