file = open("myfile.txt", "w") # Creating a text file and writing content into it
# open() function is used to create/open a file
# "w" mode means write mode

file.write("Hello! This is a sample text written into the file.\n")
# write() function writes text into the file
file.write("This is the second line of the file.\n")
file.write("i am learning Devops from Tutedude platform")
# close file after writing
file.close()
print("File content written successfully!")
