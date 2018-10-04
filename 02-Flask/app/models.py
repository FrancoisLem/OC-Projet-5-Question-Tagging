from flask_sqlalchemy import SQLAlchemy
# import logging as lg
# import enum
import pickle 
import pandas as pd 
import numpy as np
import re
import stop_words
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import unicodedata


from .views import app   


pkl_tags = open('Models/Tags_1500', 'rb')
Tags_1500  = pickle.load(pkl_tags)


def nettoyage(text): 
   
    sw = stop_words.get_stop_words(language='en')
    sw_new = ['will', 'want', 'use', 'like', 'need', 'hi', 'hello']
    sw = sw + sw_new
    
    text = str(unicodedata.normalize('NFD',text ).encode('ascii', 'ignore')) 
    
    Tokens = word_tokenize(text)
    Lemmatizer = WordNetLemmatizer()
    Tokens = [Lemmatizer.lemmatize(w) for w in Tokens]

    Tokens_clean =  [t.lower() for t in re.split(" ", re.sub(r"(\W+|_|\d+)", " ", " ".join(Tokens))) \
                     if t.lower() not in sw and len(t)>1]
    
    Question = [" ".join(Tokens_clean)]
    
    return Question


def get_tags(question): 
    
    # Nettoyage 
    #pkl_fun = open('Models/nettoyage_question.pkl', 'rb')
    #nettoyage  = pickle.load(pkl_fun)  
    #question = nettoyage(question)
    
    # TFIDF
    pkl_fun = open('Models/tfidf.pkl', 'rb')
    tfidf  = pickle.load(pkl_fun) 
    tfidf_quest = tfidf.transform(question)

    # Prediction
    pkl_fun = open('Models/modele_SVC.pkl', 'rb')
    model  = pickle.load(pkl_fun)
    pred = model.predict(tfidf_quest)
 
    # Retrouver Tags 
    tags = np.where(pred, Tags_1500, '').tolist()
    tags = np.unique(tags)
    tags = np.delete(tags, 0).tolist()
    
    return(tags)



