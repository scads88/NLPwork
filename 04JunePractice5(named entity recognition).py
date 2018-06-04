# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:59:12 2018

@author: john3


NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
"""

#named entity recognition
#useful but false positives can be kinda high
#sometimes just look for nouns as opposed to ne, can combine the 2 if want
#2 named entities back to back they should normally go together
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text=state_union.raw("2005-GWBush.txt")
sample_text=state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
tokenized=custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    
    try:
        for i in tokenized[:5]:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words) #has parts of speech
            namedEnt=nltk.ne_chunk(tagged, binary=True) #chunking via the named entity "tagged"
            
            print(namedEnt)
            namedEnt.draw()
    except Exception as e:
        print(str(e))
process_content()
            