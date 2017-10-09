##
## File runs on python3
## Uses Viterbi algorithm to implement a
## POS Tagger, imports porbability/likelihood
## tables from probabilities.py
##

import nltk
import probabilities
from probabilities import word_tags
from probabilities import word_likelihood
from probabilities import pos_prob_table

dev = open("dev.txt", "r")
output = open("output.txt", "w")
corpus = []
prob = []

for line in dev:
	line = line.strip("\n")
	corpus.append(line)

previous = "*start_end*"
k = 0
previous_prob = [1]
viterbi = {}
for word in corpus:
	# Handle OOV
	if word not in word_tags:
		output.write(word)
		output.write(" OOV \n")
		continue
	# Check if word corresponds to one or multiple tags
	if len(word_tags[word]) == 1:
		output.write('{} {} \n'.format(word, word_tags[word][0]))
	# If the word corresponds to multiple tags, find the probability
	# of each tag by iterating through each of the corresponding tags
	else:
		for tag in word_tags[word]:
			tag_probabilities = pos_prob_table[previous]
			word_emission = word_likelihood[tag]
			tag_prob = tag_probabilities[tag]
			word_prob = word_emission[word]
			for j in range(len(previous_prob)): # Loop through each of the possible preceding tags
				# Calculate the probability based on probability of previous tag
				prob = previous_prob[j] * tag_prob * word_prob 
				# Place it in the Viterbi dictionary
				viterbi[tag] = prob 
			# Then get the maximum probability from Viterbi, this is the final probability of this tag corresponding to word
			output.write('{} {}\n'.format(word, max(viterbi, key = viterbi.get)))
			previous_prob.insert(k, max(viterbi.values()))
			k = k + 1
		k = 0





