#dict() -> Function we can update the keys of
#any values from dictionary last key will update

ds1={1:"C",5:"cpp",3:"Java",4:"python",2:"PHP"}

'''
print(ds)
print(type(ds))
print(ds.get(4))# 4 ->key ->value Python

ds=dict({'101':"C"})
ds=dict({505:"PHP"})

print(ds)
print(ds.get(1))
print(ds.get('101'))
print(ds.get(2))
print(ds.get(505))

#ds.dict({1:"Python"})
#print(ds)
#ds.clear()
print(ds1.items())
print(ds1.keys())
print(ds1.values())
print("Before Pop:",ds1)
print(ds1.pop(1))
print("After Pop:",ds1)

print("Before Popitem:",ds1)
print("--------------------------")
ds1.popitem()
ds1.popitem()
print("After Popitem:",ds1)

print("Before Update:",ds1)

ds1.update({205:"Spring",207:"React",210:"Hibernate"})
print("After Update:",ds1)

print("Before:",ds1.get(207))

print(ds1.setdefault("c"))

print("After:",ds1.get(208))
#del ds1[207]
#print(ds1)

print(max(ds1))

'''
# Predefined inventory dictionary
inventory = {'pen': 20, 'notebook': 5}

# Ask user for a product name
product = input("Enter the product name to search: ").strip().lower()

# Use .get() to retrieve the quantity safely
quantity = inventory.get(product)

# Display result
if quantity is not None:
    print(f"{product.title()} is available. Quantity: {quantity}")
else:
    print("Item not found.")






