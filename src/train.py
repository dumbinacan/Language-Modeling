#!/bin/python
import IO


def train(filepath):
    #consider train new and train update with an additional file as a parameter to update the model
    unigram = dict()
    bigram = dict()
    corpus = open(filepath, "r")
    previous_word = ""
    for line in corpus:
        sentence = line.split(" ")
        for word in sentence:
            update_vocab(unigram, word)
            if previous_word not in bigram:
                #initialize to 2nd dimension!
                bigram[previous_word] = dict()
            update_vocab(bigram[previous_word], word)
    #garbage collection!
    del bigram[""] #ew nasty empty string!
    del bigram[end] #that weird part where we end one sentence and begin another
    IO.save(IO.UNIGRAM, unigram)
    IO.save(IO.BIGRAM, bigram)

def update_vocab(vocab, word):
    if word not in vocab:
        vocab[word] = 0
    vocab[word] = 1