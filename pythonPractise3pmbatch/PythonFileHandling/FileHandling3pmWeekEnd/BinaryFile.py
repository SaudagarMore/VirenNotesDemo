import os
mydata=open("newtest.txt","r")
print(os.path.exists("newtest.txt"))
print(os.path.getsize("newtest.txt"))

# #mydata=""
# import os
# myfile=open("MorePhoto1 (1).jpg","rb")
# mydata=myfile.read()
#
# if os.path.exists("newfile.txt"):
#     print("File Exists")
# else:
#     print("File Not Exists")
#
# os.remove("newfile.txt")
#
#
# # myfile1=open("newfile.txt","wb")
# # myfile1.write(mydata)
# # print("Written")
#
# # mydata=myimgagedata.read()
# # print(mydata)
