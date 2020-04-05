#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk, csv, random

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

ListOfNews = []

with open(./data/"Fake.csv") as csvfile:
        
    reader = csv.reader(csvfile)
    next(reader) # skip header line

    for row in reader:
        title = word_tokenize(row[0])
        body = []
        for w in word_tokenize(row[1]):
            if w not in stop_words:                            #filter stop words
                wLower = w.lower()                             #convert body to lower case
                wLowerLematized = lemmatizer.lemmatize(wLower) #lemmatize each word in body
                body.append(wLowerLematized)
        real = False
        
        news = (title, body, real)
        
        ListOfNews.append(news)
        
with open(./data/"True.csv") as csvfile:
        
    reader = csv.reader(csvfile)
    next(reader) # skip header line

    for row in reader:
        title = word_tokenize(row[0])
        body = []
        for w in word_tokenize(row[1]):
            if w not in stop_words:
                wLower = w.lower()
                wLowerLematized = lemmatizer.lemmatize(wLower)
                body.append(wLowerLematized)
        real = True
        
        news = (title, body, real)
        
        ListOfNews.append(news)
        
random.shuffle(ListOfNews)

print(ListOfNews[0])

