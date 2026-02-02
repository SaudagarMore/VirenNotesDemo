'''
import array

# Dictionary of typecodes and example
values
typecode_examples = {
    'b': [-10, 0, 10],
# signed char (int)
    'B': [0, 10, 255],
# unsigned char (int)

    'u': ['a', 'b', 'c'],
# Unicode characters

    'h': [-1000, 0, 1000],
# signed short (int)

    'H': [0, 1000, 65535],
# unsigned short (int)

    'i': [-100000, 0, 100000],
# signed int

    'I': [0, 100000, 4294967295],
# unsigned int

    'l': [-100000, 0, 100000],
# signed long (same as int on many systems)

    'L': [0, 100000, 4294967295],
# unsigned long

    'q': [-10**12, 0, 10**12],
# signed long long

    'Q': [0, 10**12, 2**64 - 1],
# unsigned long long

    'f': [1.5, 2.5, 3.5],
# float

    'd': [1.123456789, 2.987654321]
# double
}


# Create and print all arrays
for typecode,
values in typecode_examples.items():
    try:
        arr = array.array(typecode, values)

        print(f"typecode '{typecode}': {arr.tolist()}")
    except OverflowError as oe:
        print(f"typecode '{typecode}': OverflowError with values {values} -> {oe}")

    except TypeError as te:
        print(f"typecode '{typecode}': TypeError with values {values} -> {te}")
'''

































num=int(input("Enter Any number:"))
print("Previous Number value is:",num)

num+=10
print("New Update Number value is:",num)
















