import random
import sys
import nltk

from nltk.corpus import stopwords


# main function
def main():
    # check for system arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py <path to file>")
        sys.exit(1)
    # read file
    with open(sys.argv[1], "r") as f:
        # read input file as raw text
        text = f.read()

    # calculate lexical diversity
    calculate_lexical_diversity(text)

    tokens, nouns = process_text(text)

    # create a dictionary of nouns and their frequencies
    noun_dict = {noun: tokens.count(noun) for noun in nouns}

    # sort the dictionary by value
    sorted_noun_dict = sorted(noun_dict.items(), key=lambda x: x[1], reverse=True)

    # print the top 50 nouns
    print("50 most common words (nouns) and their counts : ", sorted_noun_dict[:50])

    # list of the top 50 nouns
    list_of_words = [sorted_noun_dict[i][0] for i in range(50)]
    # print(list_of_words)

    game(list_of_words)


def calculate_lexical_diversity(text):
    # all tokens
    tokens = [word for word in text.split() if word.isalpha() and word not in stopwords.words('english')]

    # set of unique tokens
    unique_tokens = set(tokens)

    # calculate lexical diversity
    lexical_diversity = len(unique_tokens) / len(tokens)

    print("Lexical Diversity: {:.2f}".format(lexical_diversity))


def process_text(text):
    # tokenize the lowercase text
    tokens = nltk.word_tokenize(text.lower())

    # remove stopwords and non-alphabetic tokens and tokens with length less than 5
    tokens = [token for token in tokens if token.isalpha()
              and token not in stopwords.words('english')
              and len(token) > 5]

    # get list of unique lemmas
    wnl = nltk.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(token) for token in tokens]
    unique_lemmas = set(lemmas)

    # pos tags on unique lemmas
    pos_tags = nltk.pos_tag(unique_lemmas)

    # print first 20 pos tags
    print("first 20 tagged unique lemmas: ", pos_tags[:20])

    # get list of nouns
    nouns = [word for word, pos in pos_tags if pos.startswith('NN')]

    # number of tokens (with stopwords removed, non-alphabetic tokens removed, and tokens with length less than 5
    # removed)
    print(f"Number of tokens: {len(tokens)}")

    # number of nouns
    print(f"Number of nouns: {len(nouns)}")

    # return tokens and nouns
    return tokens, nouns


# game function
def game(list_of_words):
    letter, points = " ", 5

    # get a random word from the list
    word = random.choice(list_of_words)
    # letters found
    letters_found = set()
    print(word)
    letters_left = len(word)

    print("Lets play a guessing game!")
    # create a list of underscores
    underscores = ["_"] * len(word)

    # print the underscores
    print(" ".join(underscores))

    # letter = input("Guess a letter: ")
    # loop until the user has guessed all the letters
    while points > 0 and letter != "!" and letters_left > 0:
        letter = input("Guess a letter: ")
        # check if the user wants to quit
        if letter == "!":
            print("Bye!")
            break
        # check if the letter is in the word
        if letter in word and letter not in letters_found:
            letters_found.add(letter)
            print("Right! Score is ", points + 1)
            points += 1
            # loop through the word
            for i in range(len(word)):
                # check if the letter is in the word
                if word[i] == letter:
                    # replace the underscore with the letter
                    underscores[i] = letter
                    letters_left -= 1

            # print the underscores
            print(" ".join(underscores))

        else:
            print("Sorry, guess again. Score is ", points - 1)
            points -= 1
            # print the underscores
            print(" ".join(underscores))

        # if the user has guessed all the letters
        if letters_left == 0:
            print("You win!")
            print("Current Score is", points)

            print("Would you like to play again? (y/n)")
            play_again = input()
            if play_again == "y":
                # get another random word

                # empty the letters found set
                letters_found = set()

                # get new random word
                word = random.choice(list_of_words)
                print(word)
                letters_left = len(word)
                # create a list of underscores
                underscores = ["_"] * len(word)
                # print the underscores
                print(" ".join(underscores))
                print("\n")
            else:
                print("Thanks for playing! Your final score is", points)
                break

    if letter == "!":
        print("Thanks for playing!")

    else:
        print("Game Over!")

    return None


# call main function
if __name__ == "__main__":
    main()
