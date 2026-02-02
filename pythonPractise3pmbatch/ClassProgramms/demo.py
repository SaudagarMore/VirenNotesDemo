import array

arr1 = array.array('i', [10, 20, 30, 40])
arr2 = array.array('i', [10, 20, 30, 40, 50])

# Pad arr1 with 0 to match arr2's length
while len(arr1) < len(arr2):
    arr1.append(0)

# OR pad arr2 if arr1 is longer
while len(arr2) < len(arr1):
    arr2.append(0)

Total = array.array('i', [])

for i in range(len(arr1)):
    Total.append(arr1[i] + arr2[i])

print("Resultant Array (with padding):")
for value in Total:
    print(value, end=' ')
