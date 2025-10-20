from sys import argv
def analyze_file(file_name):  
    file = open(file_name, 'r')

    words_file = open('words.txt', 'w+')
    sentence_file = open('sentence.txt', 'w')
    bigrams_file = open('bigrams.txt', 'w')

    #words
    flag = 0
    for char in file.read():
        if char.isalnum():
            words_file.write(char)
            flag = 0
        else:
            if flag == 0:
                words_file.write('\n')
            flag = 1

    #sentences
    file.seek(0)
    sentence_endings = ['.', '?', '!']
    line = []
    sentences = []
    for char in file.read():
        line.append(char)
        if char in sentence_endings:
            line = "".join(line).strip()
            if line:
                sentences.append(line)
            sentence_file.write(line)
            sentence_file.write('\n')
            line = []

    #bigrams
    bigrams = []

    for sentence in sentences:
        word_chars = []
        sentences_words = []
        for ch in sentence:
            if ch.isalnum():
                word_chars.append(ch)
            else:
                if word_chars:
                    sentences_words.append(''.join(word_chars))
                    word_chars = []

        for i in range(len(sentences_words) - 1):
            bigram = f"{sentences_words[i]} {sentences_words[i + 1]}"
            bigrams.append(bigram)

        sentences_words = []

    for bigram in bigrams:
        bigrams_file.write(bigram + '\n')
    
    words_file.close()
    sentence_file.close()
    bigrams_file.close()


def word_count(filename):
    stop_words = ['на', 'от', 'в', 'с', 'и', 'се', 'по', 'за', 'или', 'а', 'е']
    words = open(filename, 'r')
    count = {}
    for word in words.readlines():
        word = word.strip()
        if word in stop_words:
            continue
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return sort_by_value(count)

def sort_by_value(dictionary):
    items = list(dictionary.items())
    items.sort(key=lambda x: x[1], reverse=True)
    
    return dict(items)

if len(argv) < 2:
    print("Usage: python analyze_text.py <file_name>")
else:
    analyze_file(argv[1])

print("Word Count:")
print(word_count('words.txt'))