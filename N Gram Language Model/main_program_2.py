import pickle

import nltk


def main():
    # read the pickle file

    english_unigram_dict, english_bigram_dict, french_unigram_dict, french_bigram_dict, italian_unigram_dict, italian_bigram_dict = read_pickled_dictionary()

    # read file line by line
    with open('data/LangId.test', "r", encoding='utf-8') as f:
        text = f.readlines()
    len_english_tokens = unigram_length('data/LangId.train.English')
    len_french_tokens = unigram_length('data/LangId.train.French')
    len_italian_tokens = unigram_length('data/LangId.train.Italian')
    # open a file to write the output
    with open('data/results.sol', "w", encoding='utf-8') as f:
        for i, t in enumerate(text):
            p_english = compute_prob(t, english_unigram_dict, english_bigram_dict, len_english_tokens,
                                     len(english_unigram_dict))
            p_french = compute_prob(t, french_unigram_dict, french_bigram_dict, len_french_tokens,
                                    len(french_unigram_dict))
            p_italian = compute_prob(t, italian_unigram_dict, italian_bigram_dict, len_italian_tokens,
                                     len(italian_unigram_dict))

            if p_english > p_french and p_english > p_italian:
                f.write(str(i + 1) + " English\n")

            elif p_french > p_english and p_french > p_italian:
                f.write(str(i + 1) + " French\n")

            elif p_italian > p_english and p_italian > p_french:
                f.write(str(i + 1) + " Italian\n")
            else:
                f.write(str(i + 1) + " Unknown\n")

    # compute the accuracy
    accuracy, inaccurate_lines = compute_accuracy()
    accuracy = round(accuracy * 100, 2)
    print("Accuracy: ", accuracy, "%")
    print("Inaccurate lines: ", inaccurate_lines)


def compute_prob(text, unigram_dict, bigram_dict, N, V):
    # N is the number of tokens in the training data
    # V is the vocabulary size in the training data (unique tokens)

    unigrams_test = nltk.word_tokenize(text)
    bigrams_test = list(nltk.ngrams(unigrams_test, 2))

    p_laplace = 1  # Laplace smoothing

    # compute the probability of the text
    for bigram in bigrams_test:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        p_laplace *= (n + 1) / (d + V)

    return p_laplace


# computes the accuracy of the results computed
def compute_accuracy():
    inaccurate_lines = []
    with open('data/results.sol', "r", encoding='utf-8') as f:
        results = f.readlines()

    with open('data/LangId.sol', "r", encoding='utf-8') as f:
        sol = f.readlines()

    count = 0
    for i, r in enumerate(results):
        if r == sol[i]:
            count += 1

        else:
            inaccurate_lines.append(i + 1)

    return count / len(results), inaccurate_lines


def unigram_length(filename):
    # read file and remove newlines
    with open(filename, "r", encoding='utf-8') as f:
        text = f.read().replace("\n", " ")

    # tokenize the text
    tokens = nltk.word_tokenize(text)
    return len(tokens)


def read_pickled_dictionary():
    with open("pickle_file/English_unigram_dict.p", "rb") as f:
        english_unigram_dict = pickle.load(f)

    with open("pickle_file/English_bigram_dict.p", "rb") as f:
        english_bigram_dict = pickle.load(f)

    with open("pickle_file/French_unigram_dict.p", "rb") as f:
        french_unigram_dict = pickle.load(f)

    with open("pickle_file/French_bigram_dict.p", "rb") as f:
        french_bigram_dict = pickle.load(f)

    with open("pickle_file/Italian_unigram_dict.p", "rb") as f:
        italian_unigram_dict = pickle.load(f)

    with open("pickle_file/Italian_bigram_dict.p", "rb") as f:
        italian_bigram_dict = pickle.load(f)

    return english_unigram_dict, english_bigram_dict, french_unigram_dict, french_bigram_dict, italian_unigram_dict, italian_bigram_dict


if __name__ == '__main__':
    main()
