dict = {"ivan" : 3, "joro" : "2", "pavel" : 3, "a" : "unknown"}
result = []
expected_value = 3
for key in dict:
    if dict[key] == expected_value:
        result.append(key)

print(result)