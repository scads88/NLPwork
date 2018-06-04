# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:02:29 2018

@author: john3
"""


from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import gutenberg

#sampletext

sample=gutenberg.raw("bible-kjv.txt")

tok=sent_tokenize(sample)
for x in range(25):
    print(tok[x])