# Text Processing Example

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# from collections import Counter

# nltk.download('stopwords')
# nltk.download('punkt')

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

file_path='./paragraph.txt'
text_data = read_file(file_path)
print(text_data)
