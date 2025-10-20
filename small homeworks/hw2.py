import string
array = input().split()
is_sorted = True
n = len(array)

numeric_array = []
all_numeric = True
for i in range(n):
    if array[i].isdigit():
        numeric_array.append(float(array[i]))
    else:
        all_numeric = False

if all_numeric:
    array = numeric_array

for i in range(n - 1):
    if array[i] > array[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("sorted")
else:
    print("unsorted")