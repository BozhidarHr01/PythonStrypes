first = "Vladimir Nabokov"
second = "Vivian Darkbloom"

if len(first) != len(second) and sorted(first.lower()) == sorted(second.lower()):
    print("Anagram!")
else:
    print("Not anagram!")
