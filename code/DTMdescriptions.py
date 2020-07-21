import nltk
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import ssl

class DTMdescriptions:
    def __init__(self, sentence, fature_values):
        self.sentence = sentence
        self.fature_values = fature_values.tolist()

        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('stopwords')
        nltk.download('wordnet')
    # find the part of speech a word belongs to, this is used in lemmaSentence
    # Can be adjective, noun, verb, or adverb
    def get_wordnet_pos(word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

    # find the root word of a word based on the part of speech it belongs to
    # eg "hiking" becomes "hike" (verb) but "cats" becomes "cat"(noun)
    def lemmaSentence(self):
        lem = WordNetLemmatizer()
        # split sentence into indipendent words
        token_words=word_tokenize(self.sentence)
        # find root word for each word
        lemma_sentence = [lem.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(self.sentence)]
        # put sentence back together
        return " ".join(lemma_sentence)

    #turn sentence into document term matrix with the features of the original dataset
    def DTM(self):
        data = [self.sentence]
        # only use numbers and letters and make all letters lower case
        token = RegexpTokenizer(r'[a-zA-Z0-9]+')
        #stop words = words like "is","the",and "and"
        vectorizer = CountVectorizer(stop_words = 'english', strip_accents='unicode', tokenizer = token.tokenize)
        DTM = [0]* (len(self.fature_values))
        vectorizer.fit_transform(data)
        words = vectorizer.get_feature_names()
        for word in words:
            # if a word in the new description was in the original data set,
            # add 1 to that spot in the new DTM
            try:
                index = self.fature_values.index(word)
                DTM[index] +=1
            except Exception as e:
                continue

        return np.array(DTM).reshape(1, -1)
