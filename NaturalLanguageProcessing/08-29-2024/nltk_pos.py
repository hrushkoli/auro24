# Importing required libraries
import nltk
nltk.download('punkt')  # Download the tokenizer
nltk.download('averaged_perceptron_tagger')  # Download the PoS tagger

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog."

doc = "Apple is looking at buying U.K startup for $1 billion"

# Tokenizing the sentence
tokens = nltk.word_tokenize(doc)

# Performing PoS tagging
pos_tags = nltk.pos_tag(tokens)

# Display the tokens with their corresponding PoS tags
print(pos_tags)
