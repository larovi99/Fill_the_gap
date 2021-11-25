# Fill the gap
**"Fill the gap"** is a fun game to learn English through music.
This program analises a lyrics, chosen by the user, and removes some words

## Installation
There is no previous module requirements.
I am using python 3.8.10

## Structure of files
The structure of directory is:
- input: contains the lyrics of a song (.txt file)
- output: contains the lyrics of the input song with some gaps (.txt file)

## Running the project (+ example)
To run the project, execute the following command:

```console
foo@bar:~$ python3 lyrics.py
```

After that, tis message will appear:
```console
foo@bar:~$ python3 lyrics.py
Choose the name of the song (name of the file without the extension)
```
Write the name of the song,	specifically the name of the input file that you want to play.
In this example, I am going to use the song inside the input directory: Listen by Beyonce.
```console
foo@bar:~$ python3 lyrics.py
Choose the name of the song (name of the file without the extension)
listen
```
Then, a message is going to pop up and you will need to choose the percentage of words to erase.
```console
foo@bar:~$ python3 lyrics.py
Choose the name of the song (name of the file without the extension)
listen
Choose the percentage of words to erase (value from 0 to 1 (recommedation: aprox 0.05)
(Keep in mind that you are about to erase the same word in all the lyrics and this only counts as 1)
0.05
```
Finally, the code prints some information about the process.
```console
foo@bar:~$ python3 lyrics.py
Choose the name of the song (name of the file without the extension)
listen
Choose the percentage of words to erase (value from 0 to 1 (recommedation: aprox 0.05)
(Keep in mind that you are about to erase the same word in all the lyrics and this only counts as 1)
0.05
number of words :  297
number of words to erase :  15
exceptions words to not erase:  ['a', 'A', 'the', 'The', 'an', 'An', 'And', 'and']
list of words to erase :  ['has', 'listened', 'aside', 'my', 'feeling', 'I', "I've", "don't", 'only', 'but', 'so', "won't", 'in']
```

Now, appears a new file in the ouput directory, with the same name as the input file, however the are a few words missing.


## Extra information
- The words are erased randomy, therefore, the result of the execution of the same song will change
- The is a list, called "list_words_not", that contains words which the code will not erase


