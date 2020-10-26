#!/usr/bin/python3


def read_file(filename):
    """Read a file."""
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"{filename} not found.")
    else:
        return content


def count_words(word, filename):
    """Function to count words in a text."""
    text = read_file(filename).split()
    count = 0
    for line in text:
        count += int(line.lower().count(word))
    print(f"In the {filename} we encontered {count} times the word {word}.")

    
filename = 'dracula.txt'
word = 'the'
count_words(word, filename)

word = 'dracula'
count_words(word, filename)

word = 'blood'
count_words(word, filename)

word = 'dead'
count_words(word, filename)

word = 'chain'
count_words(word, filename)

word = 'god'
count_words(word, filename)

word = 'castle'
count_words(word, filename)

word = 'love'
count_words(word, filename)
