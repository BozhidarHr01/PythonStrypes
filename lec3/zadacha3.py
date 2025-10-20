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


#vtori nachin
list = sorted(list)
repeating = False
for i in range(len(list) - 1):
    if list[i] == list[i + 1]:
        repeating = True
        break
if repeating:
    print("Има повторение")
else:
    print("Няма повторение")