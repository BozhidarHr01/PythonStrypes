list = [1, 2, 3, 1, 2, 6, 7, 3, 4]
unique = []
repeating = False
for element in list:
    if element in unique:
        continue
    unique.append(element)

print(unique)