first = input()
second = input()

if len(first) == len(second) and sorted(first.lower()) == sorted(second.lower()):
    print("True")
else:
    print("False")