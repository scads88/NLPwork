# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 22:01:04 2018

@author: john3
"""

#looking at binary breakdown

#what if trinary (buy sell hold)
import nltk
import random
from nltk.corpus import movie_reviews

#gunna call the words "features" make up the elemnts of something
documents=[(list(movie_reviews.words(fileid)), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
#print(documents[1])

all_words=[]
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words=nltk.FreqDist(all_words)
print(all_words.most_common(15))

print(all_words["stupid"])
        
"""
documents=[]

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid)), category)
"""
        