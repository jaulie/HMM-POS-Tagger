##
## File runs on Python3
## Makes a table of the prior probabilities for each of
## the POS tags, assuming the bigram model
##

import nltk

test = ["NNP", "VBP", "NN"]
training = open("training.txt", 'r')
tags = []

# Places POS tags from the training corpus into a list
for line in training:
	line = line.strip("\n")		
	p = line.split("\t")
	if len(p) == 1:
		continue
	tags.append(p[1])

#fdist = nltk.FreqDist(tags)

# Adds sentence boundaries
final_tags = []
previous = "EMPTY"
for tag in tags:
	if previous in ["EMPTY", ".", "!", "?"]:
		final_tags.append('*start_end*')
	else:
		final_tags.append(tag)
	previous = tag
final_tags.append("*start_end*")

#fdist = nltk.FreqDist(final_tags)
bigrams = nltk.bigrams(final_tags)
cfd = nltk.ConditionalFreqDist(bigrams)

def multiply_list(inlist):
    out = 1
    for number in inlist:
        out *= number
    return(out)

def get_bigram_probability(first,second):
    if not second in cfd[first]:
        print('Backing Off to Unigram Probability for',second)
        unigram_probability = get_unigram_probability(second)
        return(unigram_probability)
    else:
        bigram_frequency = cfd[first][second]
    unigram_frequency = fdist2[first]
    bigram_probability = bigram_frequency/unigram_frequency
    return(bigram_probability)

def calculate_bigram_freq_of_sentence_token_list(tokens):
    prob_list = []
    ## assume that 'START' precedes the first token
    previous = '*start_end*'
    for token in tokens:
        if not token  in fdist2:
            token = '*oov*'
        next_probability = get_bigram_probability(previous,token)
        print(previous,token,(float('%.3g' % next_probability)))
        prob_list.append(next_probability)
        previous = token
    ## assume that 'END' follows the last token
    next_probability = get_bigram_probability(previous,'*start_end*')
    print(previous,'*start_end*',next_probability)
    prob_list.append(next_probability)
    probability = multiply_list(prob_list)
    print('Total Probability',float('%.3g' % probability))
    return(probability)

result = calculate_bigram_freq_of_sentence_token_list(test)



