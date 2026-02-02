'''
3. Remove Last Item Using .popitem() (Predefined)
Given:
sales_log = {'item1': 'mouse', 'item2': 'keyboard', 'item3': 'laptop'}
Use .popitem() 
Q)-to remove the last item, and print the removed item and the updated dictionary.

sales_log = {'item1': 'mouse', 'item2': 'keyboard', 'item3': 'laptop'}
print("Before Pop:",sales_log)
sales_log.popitem()
print("After Popitem:",sales_log)
-----------------------------------------------------------
4. Update Inventory with New Shipment (Predefined)
Inventory:inventory = {'apple': 10, 'banana': 5}
New shipment:shipment = {'banana': 7, 'orange': 8}
Use .update() 
Q)-to merge shipment data into inventory and print the updated dictionary.

inventory = {'apple': 10, 'banana': 5}
shipment = {'banana': 7, 'orange': 8}
print("Predefined Inventory:",inventory)
inventory.update(shipment)

print("After:",inventory)
for item,qty in inventory.items():
    if item in inventory:
        inventory[item]+=qty
    else:
        inventory[item]=qty

print("new inventory:",inventory)

#for item,qty in shipment.items():
#    inventory[item]=shipment.get(item,1)+qty

5. Invert Dictionary (Swap Keys and Values) 
(User Input) Ask the user to enter 3 country-capital pairs 
(e.g., "India":"Delhi") into a dictionary.
Q)Create a new dictionary where the capitals are keys and countries are values.

country={}
country1={}
for s in range(3):#3
    key=input("Enter The county Name:")
    value=input("Enter The Capital Name:")
    country[key]=value# starp
    
print("origibal dictionary:",country)
for key,value in country.items():#
    print(key,value)
    country1[value]=key

print('new swappied key and vlaue diciontary',country1)
for key,value in country1.items():#
    print(key,value)

#6. Find the Top Scorer (Predefined) 
#From the given marks: marks = {'Neha': 91, 'Rohit': 86, 'Simran': 94, 'Amit': 88} 
#Q)-Write a program to find and print the student with the highest score.
marks = {'Neha': 91, 'Rohit': 86, 'Simran': 94, 'Amit': 88}
maxx=max(marks)
print(maxx,marks.get(maxx))

#9. Handle Missing Keys Using .get() 
#(User Input) Ask the user to enter a product
#Q-) name to search in this dictionary: inventory = {'pen': 20, 'notebook': 5}
#Use .get() to print the quantity or a default message if the item does not
#exist.
inventory = {'pen': 20, 'notebook': 5, 'laptop':25}

print(inventory)

name=input("Enter Item name which you want to find into the list:")

for key,value in inventory.items():
    if key==name:
        print('item found in inventory ')
        print(key,value)
        break;
else:
    print("Inventory are empty or item not found into the inventory")
'''
#12. Total Stock Using .values() (Predefined)
#stacks={1:2000,2:2400,3:3500,4:1500}
#Q-)Using the same store dictionary, calculate and print the total stock (sum of all values).

















