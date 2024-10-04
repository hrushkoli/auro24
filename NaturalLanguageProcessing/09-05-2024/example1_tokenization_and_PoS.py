import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K startup for $1 billion")

print(doc)

for token in doc:
    print(token.text, token.lemma_, token.pos_)
