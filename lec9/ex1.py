def createSortedFile(file):
    new_file = open("sortedFile.txt", 'w')
    lines = file.readlines()
    new_file.writelines(sorted(lines))
    new_file.close()
    return new_file

text = open("text.txt", 'r')
createSortedFile(text)
text.close()
