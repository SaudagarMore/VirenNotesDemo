
# #abstract class
from abc import ABC, abstractmethod
class Student(ABC): #Student is a abstract class created.
#     #instance method
#     # def hello(self):
#     #     print("Hello")
#     #
#     # #static method
#     # @staticmethod
#     # def Test():
#     #     print("This is static method")
#
    #abstract method
    @abstractmethod
    def Sample(self):
        pass
#
# class Student1(Student):
#     def Sample(self):
#         print("this is sample from Student Abstract class")
#
#     def Test1(self):
#         print("hii")
#
# class Student2(Student):
#     def Sample(self):
#         print("This is another second use of Sample method")
#
# s2=Student2()
# s2.Sample()
# print("--------------------------")
# s1=Student1()
# s1.Test1()
# s1.Sample()
# #s1.hello()
# #Student1.Test()