# Student Information System
# Problem Statement:
# Create a class named Student with the following:
# Data Members:
# 1)name (string)
# 2)roll_number (integer)
# 3)marks (float)

# Member Functions:
# input_details() – to accept values from the user. 
# display_details() – to display student details.

# Task:
# Create an object of the class and use it to input and display details of a student.
roll_number=int(input("Enter Roll No:"))
marks=int(input("Enter Your Marks:"))
gender=input("Enter Gender for Student:")

class Student:        
    #instance method       
    def input_Details(name):        
        print("")     
    
    #instance method
    def display_details(name):
        print("Student Roll No:",roll_number)
        print("Student Marks is:",marks) 
        print("Student Gender is:",gender)        
        
s1=Student() #object Created

s1.input_Details()
s1.display_details()

# roll_number=int(input("Enter Roll No:"))
# marks=int(input("Enter Your Marks:"))
# gender=input("Enter Gender for Student:")