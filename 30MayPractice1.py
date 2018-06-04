# -*- coding: utf-8 -*-
"""
Created on Wed May 30 20:56:43 2018

@author: john3
"""

from nltk.book import *
#concordance=shows every occurrence of a given word with some context
text1.concordance("blue")

#similar=shows words monstrous linked to
text1.similar("monstrous")
text2.similar("monstrous")

#common_texts depreciated

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])


#generate depreciated

#print(len(text3))
#genesis has 44764 words and punc symbols (Tokens= a sequence of characters)
print(sorted(text3))#gives list all urique
#len(set(text3))---> how many unique words were used


print(len(set(text3))/len(text3))
text3.count("smote")

print(100*text4.count("a")/len(text4)) #what percent a word shows up in

def lexical_diversity(text):
    return len(set(text))/len(text)

def percentage(count, total):
    return 100*count/total

print(lexical_diversity(text))

