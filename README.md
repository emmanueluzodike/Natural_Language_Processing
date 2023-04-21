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

## N Gram Language Model
This folder contains two programs, and datafiles that contain `text` written in 3 different languages (English, French and Italian). It also contains a `test` file to test our N gram model and `sol` file to perform our performance metric.

Program 1:
- Reads a text file and removes new lines.
- Tokenizes the text.
- Uses nltk to create a unigram and bigram list.
- creates a bigram and unigram dictionary that. matches the ngram to its count (number of occurances of the ngram).
- Pickles the dictionary which will be used in program 2.
- We do this for all 3 languages so in total, 6 dictionaries.

You can find the [code here](https://github.com/emmanueluzodike/Natural_Language_Processing/blob/main/N%20Gram%20Language%20Model/main_program_1.py)

Progam 2:
- Reads in the pickled dictionaries created in program 1.
- For each line in the test file, calculate a probability for each lanuage
- Output the langauge with the highest probability a file
- Outputs the accuracy of the calculations.

You can find the [code here](https://github.com/emmanueluzodike/Natural_Language_Processing/blob/main/N%20Gram%20Language%20Model/main_program_2.py)

You can find the [data files here](https://github.com/emmanueluzodike/Natural_Language_Processing/tree/main/N%20Gram%20Language%20Model/data)

## Parsing sentences
You can find the [document here](https://github.com/emmanueluzodike/Natural_Language_Processing/blob/main/Parsing%20Sentences/Document.pdf)

## Web Crawler
you can find the [code here](https://github.com/emmanueluzodike/Natural_Language_Processing/blob/main/Webcrawler/main.py)

## ACL paper summary
you can find the [summary](https://github.com/emmanueluzodike/Natural_Language_Processing/tree/main/ACL%20Paper)

## Text Classification

In this program, we will create three different text classifier models using three different approaches - Naive Bayes, Logistic Regression, and Neural Networks - and compare their performance in classifying text.

We will use an e-commerce dataset that contains a column with item descriptions and a class column with the category of the described item. The goal is to predict the item category based on its description

 you can find the [code here](https://github.com/emmanueluzodike/Natural_Language_Processing/tree/main/Text%20Classification)


## Chatbot

This is a simple chatbot that interfaces with OpenAI / ChatGPT and uses a few NLP techinques such as embedding to store a knowledgebase. It also uses NER techinques to store information about individual users

you can find the [code here](https://github.com/emmanueluzodike/Natural_Language_Processing/blob/main/Chatbot/chatbot.ipynb)

# Summary

In this NLP class, I have gained valuable knowledge on various Natural Language Processing techniques used in everyday technology, such as sentiment analysis for filtering negative comments and Named Entity Recognition and POS tagging for user information extraction. The course has sparked my interest in exploring more NLP techniques and utilizing them in personal projects and even in a professional setting. I am particularly excited about delving into Neural Networks and their applications, not only within NLP but also in other fields.