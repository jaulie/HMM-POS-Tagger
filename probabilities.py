##
## File runs on python3
## Makes a table of bigram probabilities for POS
## tags and makes a likelihood table of words with 
## probabilities for each corresponding tag.
##

import nltk

training = open("training.txt", 'r')
pos_prob_table = {}
word_likelihood = {}
words = []
tags = []

# Places words, POS tags from the training corpus into two lists
for line in training:
	line = line.strip("\n")		
	p = line.split("\t")
	if len(p) == 1:
		continue
	words.append(p[0])
	tags.append(p[1])

# Adds sentence boundaries for tags
final_tags = []
previous = "EMPTY"
for tag in tags:
	if previous in ["EMPTY", ".", "!", "?"]:
		final_tags.append('*start_end*')
	else:
		final_tags.append(tag)
	previous = tag
final_tags.append("*start_end*")

# Conditional Frequency Distribution for POS tags
fd_tags = nltk.FreqDist(final_tags)
bigrams = nltk.bigrams(final_tags)
cfd = nltk.ConditionalFreqDist(bigrams)

def get_bigram_probability(first,second):
	bigram_frequency = cfd[first][second]
	unigram_frequency = fd_tags[first]
	bigram_probability = bigram_frequency/unigram_frequency
	return(bigram_probability)

# Places bigram frequencies in dictionary of dictionaries
previous = "*start_end*"
for tag in final_tags:
	next_probability = get_bigram_probability(previous, tag)
	if previous in pos_prob_table: 
		dic = pos_prob_table[previous]
	else: 
		dic = {}
	dic[tag] = (float('%.3g' % next_probability))
	pos_prob_table[previous] = dic
	previous = tag
next_probability = get_bigram_probability(previous, "*start_end*")
if previous in pos_prob_table: 
	dic = pos_prob_table[previous]
else: 
	dic = {}
dic[tag] = (float('%.3g' % next_probability))
pos_prob_table[previous] = dic

# Goes through all words in corpus and stores the occurrence of
# a word's various tags in a dictionary of dictionaries
# called word_likelihood
for i in range(len(words)):
	word = words[i]
	tag = tags[i]
	if word in word_likelihood:
		word_tags = word_likelihood[word]
	else:
		word_likelihood[word] = {}
		word_tags = word_likelihood[word]
	if tag in word_tags: 
		word_tags[tag] = word_tags[tag] + 1
	else: 
		word_tags[tag] = 1

# Goes through nested dictionaries of each word and
# finds probability of each tag
total_words = 0
for word in word_likelihood:
	for word_tag in word_likelihood[word]: 
		occurrences = word_likelihood[word]
		total_words = total_words + occurrences[word_tag]
	for word_tag in word_likelihood[word]:
		occurences = word_likelihood[word]
		probability = occurences[word_tag]/total_words
		occurences[word_tag] = (float('%.3g' % probability))
		word_likelihood[word] = occurrences
	total_words = 0

# Prints POS tag probabilities for DEBUGGING
for key in pos_prob_table:
	print(key)
	for key2 in pos_prob_table[key]:
		d = pos_prob_table[key]
		print("\t{} {}".format(key2, d[key2]))

# Prints likelihood of a words' tag(s)
for word in word_likelihood:
	print(word)
	for tag in word_likelihood[word]:
		tag_dictionary = word_likelihood[word]
		print("\t{} {}".format(tag, tag_dictionary[tag]))





