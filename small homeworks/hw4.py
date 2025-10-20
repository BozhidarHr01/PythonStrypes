list = input().split()
dict = {}
has_duplicate = False

for elem in list:
    if dict.get(elem):
        has_duplicate = True
        break
    else:
        dict[elem] = True

print(has_duplicate)