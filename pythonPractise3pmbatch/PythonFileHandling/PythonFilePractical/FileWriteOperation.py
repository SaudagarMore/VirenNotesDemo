from PythonFilePractical.FileOperation import TestFiledata

Myfile=open("Hello","w") #write read
Myfile.write("Welcome from Python Porgramming")
Stringdata=("6 to 7 (Transfer after Multithreading)--> "
            "Completed : Core java till Exceptions,Java 8 "
            "update features(On going) Remaining : Java 8 "
            "update features, Multithreading, Frontend "
            "and Advanced Java")

print(Myfile.writable())
Myfile.writelines(Stringdata)
Myfile.close()

Myfile1=open("Hello","r")
mydata=Myfile1.read()
print(mydata)