import nltk
from bs4 import BeautifulSoup
import requests
import os

from nltk.corpus import stopwords


def main():
    starter_url = "https://www.digitaltrends.com/computing/how-to-use-openai-chatgpt-text-generation-chatbot/"
    relevant_links = get_relevant_urls(starter_url)
    scrape_urls(relevant_links)
    clean_text_in_file()
    extract_least_important_terms()

    # with open('urls.txt', 'r',  encoding="utf-8") as f:
    #     urls = f.read().splitlines()
    # # for u in urls:
    # #     print(u)
    #
    # # scrape the urls
    # scrape_urls(urls)


def get_relevant_urls(start_url):
    r = requests.get(start_url)

    data = r.text
    soup = BeautifulSoup(data, features="lxml")

    # write urls to a file
    relevant_links = []
    with open('urls.txt', 'w', encoding="utf-8") as f:
        for link in soup.find_all('a'):
            if len(relevant_links) == 15:
                break
            link_str = str(link.get('href'))
            if 'chatgpt' in link_str.lower():
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    relevant_links.append(link_str)
                    f.write(link_str + '\n')

        return relevant_links


# This method scrapes the text in each url and puts it in a text file
def scrape_urls(url_list):
    for i, url in enumerate(url_list):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # write the text to ith file
        with open(f'data/text_{i}.txt', 'w', encoding="utf-8") as f:
            for p in soup.find_all('p'):
                f.write(p.get_text() + '\n')


def clean_text_in_file():
    # create a directory called data
    directory = 'data/'
    for i, filename in enumerate(os.listdir(directory)):
        f = os.path.join(directory, filename)
        with open(f, 'r', encoding="utf-8") as f:
            text = f.read()

        # clean the text
        # remove newlines and tabs
        text = text.replace('\n', ' ').replace('\t', ' ')

        # Extract sentences with NLTK’s sentence tokenize
        sentences = nltk.sent_tokenize(text)
        with open(f'cleaned_data/cleaned_text_{i}.txt', 'w', encoding="utf-8") as f:
            for s in sentences:
                f.write(s + " ")


def extract_least_important_terms():
    # created a directiory called cleaned_data
    directory = 'cleaned_data/'
    term_frequency_dict = {}
    for i, filename in enumerate(os.listdir(directory)):
        f = os.path.join(directory, filename)
        with open(f, 'r', encoding="utf-8") as f:
            text = f.read().lower()

        tokens = nltk.word_tokenize(text)
        tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english')]

        # find the term frequency
        for token in tokens:
            if token in term_frequency_dict:
                term_frequency_dict[token] += 1
            else:
                term_frequency_dict[token] = 1

    # sort the dictionary by value
    term_frequency_list = list(term_frequency_dict.items())
    # print the most 25 terms
    sorted_terms = sorted(term_frequency_list, key=lambda x: x[1])

    # print the least 25 terms
    least_25_terms = sorted_terms[:25]
    print("Least 25 terms: ")
    print(least_25_terms)

    # print the most 25 terms
    most_25_terms = sorted_terms[-40:]
    print("Most 25 terms: ")
    print(most_25_terms)


def build_knowledge_base():
    knowledge_base = {
        'chatgpt': [
            'ChatGPT is a text generation chatbot that uses OpenAI’s GPT-3 language model to generate responses to '
            'user input.',
            'ChatGPT is an AI language model developed by OpenAI',
            'ChatGPT is trained on a massive dataset of text and can generate human-like responses to prompts'
        ],
        'ai': [
            'AI is the simulation of human intelligence processes by machines, especially computer systems.',
            'AI stands for artificial intelligence',
            'AI is a broad field that includes machine learning, natural language processing, and robotics'
        ],
        'model': [
            'A model is a representation of a system, process, or phenomenon.',
            'Models can be used to make predictions, test hypotheses, and understand complex systems.',
            'In AI, models are often used to perform tasks such as image recognition, speech synthesis, and language '
            'translation'
        ],
        'openai': [
            'OpenAI is an artificial intelligence research lab',
            'OpenAI was founded in 2015 by a group of tech leaders, including Elon Musk and Sam Altman',
            'OpenAI is dedicated to advancing artificial intelligence in the way that is most likely to benefit '
            'humanity as a whole'
        ],
        'chatbot': [
            'A chatbot is a computer program that simulates human conversation through voice commands or text chats.',
            'Chatbots can be used for customer service, entertainment, and information retrieval'
            'Chatbots can be programmed to respond to specific prompts or to learn from user interactions'
        ],
        "google": [
            "Google is a multinational technology company",
            "Google is known for its search engine, Android operating system, and suite of online services",
            "Google is also involved in AI research and development"
        ],
        "microsoft": [
            "Microsoft is a multinational technology company",
            "Microsoft is known for its Windows operating system, Office suite, and Xbox gaming console",
            "Microsoft is also involved in AI research and development"
        ],
        "bing": [
            "Bing is a search engine developed by Microsoft",
            "Bing is one of the most popular search engines in the world, with over 10% market share",
            "Bing offers a variety of features, including image and video search, news aggregation, and translation"
        ],
        'code': [
            'Code is a set of instructions that a computer can understand and execute.',
            'Code can be written in various programming languages, including Python, Java, and C++.',
            'Code can be used to automate tasks, create websites, and build software applications.'
        ],
        "responses": [
            "Responses are the outputs generated by an AI system in response to a prompt or input",
            "Responses can be generated using rule-based systems, statistical models, or deep learning algorithms",
            "Responses can vary in quality depending on the complexity of the task and the quality of the input data"
        ]

    }


if __name__ == '__main__':
    main()
