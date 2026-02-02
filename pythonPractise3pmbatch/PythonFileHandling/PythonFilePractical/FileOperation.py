'''
open ->is  function which used for open the file.
read ->this function can read all file data or file character or length based on
function arguments values
readline ->this function can read only one single line at time.
we can read file using for loop
'''

TestFiledata=open("Test","r")# r ->file can read
# mydata=TestFiledata.read()
# print(mydata)
#print(TestFiledata.readable())
# myfileline=TestFiledata.readline(20)
# print(myfileline)
myfilelines=TestFiledata.readlines()
print(myfilelines)