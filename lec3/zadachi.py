# zadacha 1
array = ['b', 'a']
res = True

for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
        res = False
        break

print(res)

#vtori nachin
print(all(array[i] <= array[i + 1] for i in range(len(array) - 1)))

#zadacha 2
first = "Vladimir Nabokov"
second = "Vivian Darkbloom"

if sorted(first.lower()) == sorted(second.lower()):
    print("Anagram!")
else:
    print("Not anagram!")

#zadacha 3
list = "Vladimir Nabokov"
repeating_letters = []
repeating = False
for element in list:
    if element in repeating_letters:
        repeating = True
    repeating_letters.append(element)

if repeating:
    print("Има повторение")
else:
    print("Няма повторение")



