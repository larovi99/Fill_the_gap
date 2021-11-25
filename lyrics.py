
from random import sample
import re

word_count = 0

print("Choose the name of the song (name of the file without the extension)")
name_song = input()

print("Choose the percentage of words to erase (value from 0 to 1 (recommedation: aprox 0.05)")
print("(Keep in mind that you are about to erase the same word in all the lyrics and this only counts as 1)")
percentage = input()
percentage = float(percentage)


file_name = "input/"+name_song+".txt"
file_name2 = "output/"+name_song+".txt"
list_words = []

with open(file_name, 'r') as file:
    for line in file:
        for word in line.split():
            list_words.append(word)
            word_count += 1

print("number of words : ", word_count)

words_erase = round(percentage * word_count)
print("number of words to erase : ",words_erase)

list_words_erase = sample(list_words, words_erase)

list_words_not = ["a", "A", "the", "The", "an", "An", "And", "and"]
print("exceptions words to not erase: ", list_words_not)
for i in list_words_not:
    if i in list_words_erase:
        list_words_erase.remove(i)
print("list of words to erase : ",list_words_erase)

# Copy input file in output file
fin = open(file_name, "rt")
fout = open(file_name2, "wt")
for line in fin:
    fout.write(line)
fin.close()
fout.close()

with open(file_name2, 'r+') as f:
    text = f.read()
    for i in list_words_erase:
        if i in text:
            text = re.sub("\\b" + i + "\\b", ' ______ ', text)

            f.seek(0)
            f.write(text)
            f.truncate()
