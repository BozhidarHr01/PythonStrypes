histogram = {}
text = input()

for char in text:
    if char.isalpha():
        char_lower = char.lower()
        histogram[char_lower] = histogram.get(char_lower, 0) + 1

print(sorted(histogram.items()))