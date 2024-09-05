import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Hi, my personal email address is hrushkoli1@gmail.com, and my university email address is hrishikesh.koli.mscai2024@aurouniveristy.edu.in")

emails = []
for tokens in doc:
    if tokens.like_email:
        emails.append(tokens.text)

print(emails)
