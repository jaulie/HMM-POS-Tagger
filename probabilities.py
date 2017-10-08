##
## File runs on Python3
## Makes a table of the prior probabilities for each of
## the POS tags, assuming the bigram model
##

import nltk

pos_prob_table = {}
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

# Calculate bigram frequency of POS tags
fdist = nltk.FreqDist(final_tags)
bigrams = nltk.bigrams(final_tags) #puts list of tags into pairs
cfd = nltk.ConditionalFreqDist(bigrams)

def get_bigram_probability(first,second):
  #if not second in cfd[first]:
  # print('Backing Off to Unigram Probability for',second)
  # unigram_probability = get_unigram_probability(second)
  # return(unigram_probability)
  #else:
  bigram_frequency = cfd[first][second]
  unigram_frequency = fdist[first]
  bigram_probability = bigram_frequency/unigram_frequency
  return(bigram_probability)

# Places bigram frequencies in dictionary of dictionaries
previous = "*start_end*"
for tag in tags:
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

# Prints POS tag probabilities
for key in pos_prob_table:
  print(key)
  for key2 in pos_prob_table[key]:
    d = pos_prob_table[key]
    print("\t{} {}".format(key2, d[key2]))