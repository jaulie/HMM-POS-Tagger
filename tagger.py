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
output = open("output.pos", "w")
corpus = []

for line in dev:
	line = line.strip("\n")
	corpus.append(line)

previous = "*start_end*"
k = 0
previous_prob = {previous: 1}
viterbi = {}
final = {}
for word in corpus:
	if word == r'\s':
		output.write('\n')
		continue
	# Handle OOV
	if word not in word_tags:
		output.write('{}\tOOV\n'.format(word))
		continue
	# Check if word corresponds to one or multiple tags
	if len(word_tags[word]) == 1:
		output.write('{}\t{} \n'.format(word, word_tags[word][0]))
	# If the word corresponds to multiple tags, find the probability
	# of each tag by iterating through each of the corresponding tags
	else:
		for tag in word_tags[word]:
			# Iterates through the tags associated with that word
			tag_probabilities = pos_prob_table[previous]
			word_emission = word_likelihood[tag]
			if tag in tag_probabilities: tag_prob = tag_probabilities[tag] #probability of the tag
			else: tag_prob = 0.0001
			word_prob = word_emission[word] #probability that that POS tags the word
			# Loop through each of the preceding word's possible tags
			for each in previous_prob: 
				# Calculate the probability based on probability of previous tag
				prob = previous_prob[each] * tag_prob * word_prob 
				# Place it in the Viterbi dictionary
				viterbi[each] = prob 
			# Then get the maximum probability from Viterbi, this is the final probability of this tag corresponding to word
			max_prob = max(viterbi.values())
			final[tag] = max_prob
		previous_prob = final
		# Get the tag that is most probable for this word
		most_prob_tag = max(final, key = final.get)
		output.write('{}\t{}\n'.format(word, most_prob_tag))





