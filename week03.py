import array

arr = array.array('i', [99, 0, -7, 0, 16])
for i in range(len(arr)):
    print(f"{arr[i]:5} {id(arr[i])}")

l = [9, 9]
print(id(0), id(1))