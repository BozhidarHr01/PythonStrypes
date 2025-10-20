input = input().split()
key = int(input[-1]) 

input_str = " ".join(input[:-1])
result = []
for char in input_str:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        result.append(chr((ord(char) - start + key) % 26 + start))
    else:
        result.append(char)

print("".join(result))
