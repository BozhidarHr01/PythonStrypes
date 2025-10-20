import string
input_string = input("Insert input string to cipher: ")
key = int(input("Insert key form 1 to 25: "))

alphabet = string.ascii_uppercase
ciphered_list = []
for char in input_string:
    if char.isalpha():
        ciphered_letter = chr((ord(char) + key) % ord("Z"))
        ciphered_list.append(ciphered_letter)
    else:
        ciphered_list.append(char)
print("Ciphered string:", "".join(ciphered_list))

#2nd solution
alphabet = string.ascii_letters
cipher = alphabet[3:] + alphabet[0:3]
#...
print(cipher)
new_alpha = str.maketrans(alphabet, cipher)
print(input_string.translate(new_alpha))