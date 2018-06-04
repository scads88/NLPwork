# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 20:56:11 2018

@author: john3
"""

#lemmatizing 
#very similar to stemming but root word is real word
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python")) #default pos is gunna be a noun, if word not noun gotta pass thru pos
print(lemmatizer.lemmatize("better", pos="a")) #adjective
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run", "v"))