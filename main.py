def count_words():
    text_file = input('Enter text file name: ')
    word_count = 0
    file = open(text_file, 'r')
    for sentences in file:
        words = sentences.split(' ')
        word_count = word_count + len(words)
        print("Words: " + str(word_count))


count_words()