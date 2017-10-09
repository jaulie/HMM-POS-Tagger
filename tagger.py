##
## File runs on python3
## Uses Viterbi algorithm to implement a
## POS Tagger
##

import nltk
import probabilities

dev = open("dev.txt", "r")
corpus = []
prob = []

for line in dev:
	line = line.strip("\n")
	corpus.append(line)


