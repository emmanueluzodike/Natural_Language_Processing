# Natural_Language_Processing
This is my NLP portfolio
## Overview of NLP
This is an overview of NLP
you can find the [pdf here](https://github.com/emmanueluzodike/Natural_Language_Processing/blob/main/Overview%20of%20NLP.pdf) 

## Text Processing with Python
- This program reads a csv file that contains Employee information. The attributes of each employee include, the first name, last name, middle initials, id, and phone number. The program reads the file and standardizes the attributes of the file. It ensures that the first name, last name and middle initial are capitalized. If no middle initial exists, it puts a place holder 'X' as the initial. it ensures that the id is in the form: 2 letters followed by 4 digits and the phone number is of the foem xxx-xxx-xxxx.
- You can run the program by simply downloading the project to your laptop/computer and clicking run. Alternatively, you can can run the program in the terminal by entering: "python main.py data/data.csv"
NOTE: If you change the main file name, you will need to edit the run configuration to be able to run it from the ide. You would have to run it from the terminal by entering: "python filename data/data.csv"
- There are some pros and cons to using python for text processing. A few of the pros include the ease of use, redability and the Natural Language toolkit that is availble in python. Some of the cons are that python is not the fastest language for text processing, one reason because strings are not mutable in python. Python is also memory intensive.
- This assignment gave me the opportunity to review regular expressions. I also learned about pickle files and what they are used for.

You can find the[ code here](https://github.com/emmanueluzodike/Natural_Language_Processing/tree/main/Text%20Processing%20with%20Python)

## Word Guessing with Python
- This program reads a text file and tokenizes it
- It then removes all the tokens that are not alphabets, are stopwords and are tokens with length less than 5. 
- It then lemmatizes the tokens, and extracts the unique lemmas
- Finally it extracts the lemmas that are nouns
- These tokens are then used to play a hangman like game

Rules of the game:
- The user starts out with 5 points
- for every letter guessed, the user gains one point and losses 1 point for incorrect guesses
- The game is over when a user losses all their points or the user chooses to quit.

You can find the [code here](https://github.com/emmanueluzodike/Natural_Language_Processing/blob/main/Word%20Guessing%20Game%20-%20NLTK%20Demo/main.py)

## WordNet Demo
This notebook contains a simple demo of WordNet.

You can find the [notebook here](https://github.com/emmanueluzodike/Natural_Language_Processing/blob/main/Word%20Guessing%20Game%20-%20NLTK%20Demo/main.py)