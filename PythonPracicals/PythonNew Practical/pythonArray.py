# import array

# # Dictionary of typecodes and example values
# typecode_examples = {
#     'b': [-10, 0, 10],                      # signed char (int)
#     'B': [0, 10, 255],                      # unsigned char (int)
#     'u': ['a', 'b', 'c'],                   # Unicode characters (str)
#     'h': [-1000, 0, 1000],                  # signed short (int)
#     'H': [0, 1000, 65535],                  # unsigned short (int)
#     'i': [-100000, 0, 100000],              # signed int (int)
#     'I': [0, 100000, 4294967295],           # unsigned int (int)
#     'l': [-100000, 0, 100000],              # signed long (int)
#     'L': [0, 100000, 4294967295],           # unsigned long (int)
#     'q': [-10**12, 0, 10**12],              # signed long long (int)
#     'Q': [0, 10**12, 2**64 - 1],            # unsigned long long (int)
#     'f': [1.5, 2.5, 3.5],                   # float (float)
#     'd': [1.123456789, 2.987654321]         # double (float)
# }

# print(f"{'Typecode':<8} {'Values':<40} {'Python Type':<15}")
# print("="*70)

# # Create and print all arrays with type information
# for typecode, values in typecode_examples.items():
#     try:
#         arr = array.array(typecode, values)
#         data_type = type(arr[0]).__name__  # Get Python type name
#         print(f"{typecode:<8} {str(values):<40} {data_type:<15}")
#     except OverflowError as oe:
#         print(f"{typecode:<8} {'(Overflow Error)':<40} Error")
#     except TypeError as te:
#         print(f"{typecode:<8} {'(Type Error)':<40} Error")


# import array

# # Dictionary of typecodes and example values
# typecode_examples = {
#     'b': [-10, 0, 10],                      # signed char (int)
#     'B': [0, 10, 255],                      # unsigned char (int)
#     'u': ['a', 'b', 'c'],                   # Unicode characters (str)
#     'h': [-1000, 0, 1000],                  # signed short (int)
#     'H': [0, 1000, 65535],                  # unsigned short (int)
#     'i': [-100000, 0, 100000],              # signed int (int)
#     'I': [0, 100000, 4294967295],           # unsigned int (int)
#     'l': [-100000, 0, 100000],              # signed long (int)
#     'L': [0, 100000, 4294967295],           # unsigned long (int)
#     'q': [-10**12, 0, 10**12],              # signed long long (int)
#     'Q': [0, 10**12, 2**64 - 1],            # unsigned long long (int)
#     'f': [1.5, 2.5, 3.5],                   # float (float)
#     'd': [1.123456789, 2.987654321]         # double (float)
# }

# # Create and print all arrays with type information
# for typecode, values in typecode_examples.items():
#     try:
#         arr = array.array(typecode, values)
#         data_type = type(arr[0]).__name__  
#         print(f"{typecode:<8} {str(values):<40} {data_type:<15}")
#     except OverflowError as oe:
#         print(f"{typecode:<8} {'(Overflow Error)':<40} Error")
#     except TypeError as te:
#         print(f"{typecode:<8} {'(Type Error)':<40} Error")
