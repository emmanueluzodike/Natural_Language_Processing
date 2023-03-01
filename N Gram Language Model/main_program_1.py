import nltk
from nltk import ngrams
import pickle


# main class
def main():
    # read file
    ud, bd = process_file('data/LangId.train.English')
    # save the dictionaries to a pickle file
    save_dict_to_pickle_file(ud, bd, "English")

    # read file
    ud, bd = process_file('data/LangId.train.French')
    # save the dictionaries to a pickle file
    save_dict_to_pickle_file(ud, bd, "French")

    # read file
    ud, bd = process_file('data/LangId.train.Italian')
    # save the dictionaries to a pickle file
    save_dict_to_pickle_file(ud, bd, "Italian")


def process_file(file_name):
    # read file and remove newlines
    with open(file_name, "r", encoding='utf-8') as f:
        text = f.read().replace("\n", '')

    # tokenize the text
    tokens = nltk.word_tokenize(text)

# create unigram and bigram list
    unigrams = tokens
    bigrams = list(ngrams(tokens, 2))

    # unigram dictionary
    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}

    # bigram dictionary
    bigram_dict = {t: bigrams.count(t) for t in set(bigrams)}

    return unigram_dict, bigram_dict


def save_dict_to_pickle_file(ud, bd, language):
    # save the dictionaries to a pickle file
    pickle.dump(ud, open("pickle_file/" + language + "_unigram_dict.p", "wb"))
    pickle.dump(bd, open("pickle_file/" + language + "_bigram_dict.p", "wb"))


if __name__ == '__main__':
    main()
