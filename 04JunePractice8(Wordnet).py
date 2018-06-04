# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 21:41:07 2018

@author: john3
"""

from nltk.corpus import wordnet
syns=wordnet.synsets("program")
print(syns)
print(syns[0])
print(syns[0].lemmas()[0].name()) #just the word
print(syns[0].name()) #synset

print(syns[0].definition())
print(syns[0].examples())


synonyms=[]
antonyms=[]

for syn in wordnet.synsets("good"): #this is the word you are looking at synonyms and antonyms for
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print(set(antonyms))


w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))  #wup is word and palmer



w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("car.n.01")

print(w1.wup_similarity(w2))  #wup is word and palmer


#these features generate percent similarity

w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("cat.n.01")

print(w1.wup_similarity(w2))  #wup is word and palmer

#using synsets for termpaper switcheroo writing
#wordbot article switcheroo (daily mail, buzzfeed)