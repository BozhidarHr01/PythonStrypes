histogram = {}
text = input()

for char in text:
    histogram[char] = histogram.get(char, 0) + 1
    # if char in histogram:
    #     histogram[char] += 1
    # else:
    #     histogram[char] = 1

print(histogram)