# Custom exception class
class MyCustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_value(x):
    if x < 0:
        raise MyCustomError("Negative value is not allowed!")
    else:
        print("Value is fine:", x)

try:
    check_value(20)
except MyCustomError as e:
    print("Caught an error:", e)

