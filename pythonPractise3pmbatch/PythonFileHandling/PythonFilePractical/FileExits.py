import os
# if os.path.exists("Hello"):
#     print("File Is Present")
# else:
#     print("File Is Not Present")
# os.remove("newfile1")
mydata=open("DemoFile","r")
print(mydata.seek(0))
print(mydata.seek(5))