

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from copy import copy 
from sklearn.metrics import accuracy_score
import copy
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string

df = pd.read_csv(r'spam.csv')

le = LabelEncoder()
df['New_Category'] = le.fit_transform(df['Category'])
print(df["Message"].head())
df['Word_Count'] = df["Message"].str.split().str.len()
tokenized_msg = df["Message"].str.lower().str.split(" ")
def alpha_numeric(msg):
  alpha = []
  for token in msg:
    new_m = " ".join(c for c in token if c.isalnum())
    alpha.append(new_m)
  return alpha

for i in range (len(tokenized_msg)):
  tokenized_msg[i]=alpha_numeric(tokenized_msg[i])

df['Message']=tokenized_msg
print(tokenized_msg)

def to_sentence(tokens):
  s=""
  for token in tokens:
    s=s+" "+token
  return s[1:]

for i in range(len(tokenized_msg)):
  tokenized_msg[i]=to_sentence(tokenized_msg[i])
print(tokenized_msg)