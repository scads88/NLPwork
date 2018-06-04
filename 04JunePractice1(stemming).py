# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:56:17 2018

@author: john3
"""

#nltk really just the toolkit, sklearn is where the real ml comes from


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize



#I was taking a ride in the car.
#I was riding in the car.

ps=PorterStemmer()


example_words=["python", "pythoner", "pythoning", "pythoned", "pythonly"]

for w in example_words:
    print(ps.stem(w))


new_text="It is very import to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

wordic=word_tokenize(new_text)

for w in wordic:
    print(ps.stem(w))

