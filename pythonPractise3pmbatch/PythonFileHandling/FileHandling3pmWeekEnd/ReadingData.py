#read ->it can read all the text data from the file.
#readline ->it can read only one single lien from file.
#readlines ->it can read all data from file but dispaly on single line.
sd=open("Testfile.txt","r+")
mydata=sd.read()
# for i in range(0,5+1):#0 1 2 3 4 5
#     print(sd.readline())
print(mydata)
sd.write("Python Supports to MongoDb")
print("Data Write")