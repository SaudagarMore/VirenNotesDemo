#programme with-out Exception handling..
Exception
while True:
    def demo(no1, no2): print("Addition is:", no1 + no2)
    try: #if
            no=int(input("Enter Any No:"))
            result=no/5
            print("The Sqaure of the value is:",result)
            demo(30, 50)
            for j in range(1, 10):
                print(j, end=" ")
            break
    except ValueError: print("Pleas Enter Only Integers Value")
    except ZeroDivisionError: print("Cant Divide with 0 value")

