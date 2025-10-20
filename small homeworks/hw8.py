d = {1:'a', 2:'b', 3:'c', 4:'a', 5:'d', 6:'e', 7:'a', 8:'b'}

expected_value = input().strip()
result = []

for key, value in d.items():
    if value == expected_value:
        result.append(key)

print(result)