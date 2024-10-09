import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp('Microsoft is generating $198.3 billion in USA')

displacy.render(doc,style='ent') # It renders a HTML object highligting entities (ent) in the doc
