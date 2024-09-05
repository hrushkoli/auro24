import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp('Microsoft is generating $198.3 billion in USA')

for entity in doc.ents:
    print(entity.text,'|',entity.label_,'|',spacy.explain(entity.label_))
