from lib2to3.pgen2.tokenize import tokenize
import nltk
import numpy as np

nltk.download('punkt')
from nltk.stem.porter import PorterStemmer #lancasterstemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32) #one-hot encoding
    for idx, w, in enumerate(all_words):#gives index and word
        if w in tokenized_sentence:
            bag[idx] = 1.0
    
    return bag





