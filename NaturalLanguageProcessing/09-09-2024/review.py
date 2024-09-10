import numpy as np
import pandas as pd 
import re
import nltk
import spacy
import string

df= pd.read_csv('./review.csv')
print(df.head())

df.rename(columns={"Review Text":'text'},inplace=True)

print(df.head())


