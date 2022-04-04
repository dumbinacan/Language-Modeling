#!/bin/python
#previously prob.py
import math
import IO
import prep


def calculate_probability(model, sentence):
    if model >= IO.BIGRAM:
        vocab = IO.load(IO.BIGRAM)
        if model == IO.ADD_ONE:
            prep.addone(vocab)
        return bigram(vocab, sentence)
    return unigram( IO.load(IO.UNIGRAM), sentence )

def unigram(model, sentence):
    words = sentence.split(" ")
    probs = 0.0
    total = total_tokens(model)
    for word in words:
        probs += math.log2(model[word] / total)
    return probs

def bigram(model, sentence):
    words = sentence.split(" ")
    probs = 0.0
    word1 = ""
    for word2 in words:
        if word1 != "":
            if word2 in model[word1]:
                probs += math.log2(model[word1][word2]/total_tokens(model[word1]))
            else:
                return 0
            word1 = word2
    return probs

def total_tokens(vocab):
    total = 0
    for word in vocab:
        total += vocab[word]
    return total