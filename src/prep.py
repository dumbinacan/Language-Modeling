#!/bin/python
import IO
import tags


#avoiding unking until the very last second could be useful for accuracy esp in addone
def prep(filepath):
    text = open(filepath, "r")
    # TODO hard wire paths to things
    name = filepath.split("/")
    name = name[len(name) - 1]
    path = "../var/preprocs/" + name
    corpus = open(path, "w")
    vocab = dict()
    unks = dict()

    prepped_text = ""
    for line in text:
        tmp = line.split(" ")
        prepped_text += tags.start

        for word in tmp:
            word = (word.lower()).strip()
            prepped_text += word + " "
            if word not in vocab:
                vocab[word] = 1
                unks[word] = 1
            elif word in unks:
                # should unking be done in the training? leave the preprocs looping sentence style??
                del unks[word]
        prepped_text += tags.end

    for word in unks:
        prepped_text = prepped_text.replace(" " + word + " ", tags.unknown)
    corpus.write(prepped_text)  # what if I wrote to the file directly above? Then reopen the file to do the unks bit?
    return path

def addone(bigram):
    #can't I be clever with math operations instead?! leave this for now and get the code running again
    add_one = bigram
    for word1 in bigram:
        for word2 in bigram[word1]:
            add_one[word1][word2] += 1
    return add_one

def sentence(s):
    # TODO have this interface with the vocab and unks the sentence
    tmp = s.split(" ")
    prepped_text = tags.start
    for word in tmp:
        word = (word.lower()).strip()
        prepped_text = word + " "
    return prepped_text + tags.end


def samples(filepath):
    # might be better if organized as preprocess class with preproc for train and test
    text = open(filepath, "r")
    name = filepath.split("/")
    name = name[len(name) - 1]
    path = "../var/preprocs/" + name
    corpus = open(path, "w")
    for line in text:
        corpus.writelines(sentence(line) + "\n")
    return path
