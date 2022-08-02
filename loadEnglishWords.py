"""
This program loads the english words into 
"""
from english_words import english_words_set

def putWordsInFile(file="words.txt"):
    f = open(file, "w")
    for word in english_words_set:
        f.write(word + '\n')
    f.close()

putWordsInFile()