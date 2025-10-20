parts = input().split()
if len(parts) == 2:
    text, key = parts
else:
    key = parts[-1]
    text = ' '.join(parts[:-1])

result = []
j = 0

for ch in text:
    if ch.isalpha():
        shift = ord(key[j % len(key)].lower()) - ord('a')
        base = ord('a') if ch.islower() else ord('A')
        result.append(chr((ord(ch) - base + shift) % 26 + base))
        j += 1
    else:
        result.append(ch)

print(''.join(result))