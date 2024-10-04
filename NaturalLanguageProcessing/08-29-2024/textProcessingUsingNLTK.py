# Text Processing Example

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

def read_file(path):
    with open(path,'r') as file:
        data = file.read()
    return data

def tokenize_text(text):
    tokens= word_tokenize(text)
    return tokens

def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return filtered_tokens

def count_word_frequency(tokens):
    word_freq = Counter(tokens)
    return word_freq

file_path='./paragraph.txt'
text_data = read_file(file_path)

print("Raw Data :\n",text_data)
# print("Tokens :\n",tokenize_text(text_data))
print("Parts of Speech:\n",nltk.pos_tag(tokenize_text(text_data)))
# print("Filtered Tokens After Removing Stop Words :\n",remove_stop_words(text_data))
# print("Word Frequency: \n", count_word_frequency(text_data))


