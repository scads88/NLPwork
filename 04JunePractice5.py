# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:59:12 2018

@author: john3
"""

#named entity recognition
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
            tagged=nltk.pos_tag(words)
            namedEnt=nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
            print(namedEnt)
    except Exception as e:
        print(str(e))
process_content()
            