#!/bin/python
import math
import test

def sentence(model, line):
    return math.pow( 2, ( -1 * test.calculate_probability(model, line) ) )

def file(model, filepath):
    text = open(filepath, "r")
    l = 0.0
    M = 0
    for line in text:
        l += test.calculate_probability(model, line)
        M += 1
    return math.pow( 2, (-1 * l/M) )