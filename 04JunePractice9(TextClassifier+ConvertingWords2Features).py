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
import pickle

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
#print(all_words.most_common(15))
#print(all_words["stupid"])

#tut 10 
#freq distrib ordered from most to least common word
#limiting a little bit 
word_features=list(all_words.keys())[:3000]
def find_features(document):
    words=set(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
    return features
#print((find_features(movie_reviews.words("neg/cv000_29416.txt"))))
featuresets=[(find_features(rev), category) for (rev, category) in documents]

#11 naive bayes classifier with nltk
training_set=featuresets[:1900]
testing_set=featuresets[1900:]


#this is a process intensive step
#classifier=nltk.NaiveBayesClassifier.train(training_set)

classifier_f=open("naivebayes.pickle", "rb")
classifier=pickle.load(classifier_f)
classifier_f.close()


print("Naive Bayes Algo Accuracy percent: ", (nltk.classify.accuracy(classifier, testing_set)*100))
classifier.show_most_informative_features(15)

save_classifier=open("naivebayes.pickle", "wb") #generates our pickle shell
pickle.dump(classifier, save_classifier) #what we want to dump and where we want to dump it
save_classifier.close() #closes the now populated pickle document

        