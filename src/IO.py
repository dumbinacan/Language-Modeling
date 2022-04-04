#!/bin/python
import pickle

UNIGRAM = 0
BIGRAM = 1
ADD_ONE = 2

class IO:
    """"This class will handle saving and loading the vocabs for the language models"""
    _models = "unigram.vocab", "bigram.vocab"

    def save(self, model, vocab):
        return pickle.dump(vocab, open("../var/models/" + self._models[model], "wb"))

    def load(self, model):
        return pickle.load(open("../var/models/" + self._models[model], "rb"))
