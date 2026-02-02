# open() function is used to create/open a file
# "r" mode means write mode
file=open("myfile.txt","r")
# Read() function Read text from the file
data=file.read()
print(data)
# close file after Reading
file.close()
print("File content Read successfully!")
