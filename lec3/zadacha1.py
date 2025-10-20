array = [10, 12, 15]
res = True

for i in enumerate(array):
    if array[i] > array[i + 1]:
        res = False
        break

print(res)

#vtori nachin
print(all(array[i] <= array[i + 1] for i in range(len(array) - 1)))
