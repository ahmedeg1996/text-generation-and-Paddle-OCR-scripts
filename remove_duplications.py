with open(r'C:\Users\v23ASayed2\Desktop\TextRecognitionDataGenerator\trdg\dicts\ar.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split()
unique_words = list(set(words))

with open(r'C:\Users\v23ASayed2\Desktop\TextRecognitionDataGenerator\trdg\dicts\output.txt', 'w', encoding='utf-8') as f:
    for word in unique_words:
        f.write(word + '\n')
