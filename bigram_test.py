## This file assumes Python 3
## To work with Python 2, you would need to adjust
## at least: the print statements (remove parentheses)
## and the instances of division (convert
## arguments of / to floats), and possibly other things
## -- I have not tested this.

import nltk
from nltk.corpus import brown

test_sentence_tokens = ['a','fact','about','the','unicorn','is','the','same','as','an','alternative','fact','about','the','unicorn','.']

words = brown.words()
fdist1 = nltk.FreqDist(w.lower() for w in words)

total_words = len(words)

print('Frequency of tokens in sample sententence in Brown according to NLTK:')

print('{:>11}   {:^11}'.format('WORD', 'OCCURANCE'))

for word in test_sentence_tokens:
    print('{:>11} | {:<11}'.format(word, fdist1[word]))


input('Pausing: Hit Return when Ready.')

print('Given that there are',total_words,'in the Brown Corpus, the unigram probability of these words is as follows (rounded to 3 significant digits):')


print('{:>11}   {:^11} {:^6}'.format('WORD', 'OCCURANCE', 'UNIGRAM PROB'))
for word in test_sentence_tokens:
    unigram_probability = 100 * (fdist1[word]/total_words) 
    print('{:>11} | {:<11}| {:.3f}%'.format(word, fdist1[word], unigram_probability))


input('Pausing: Hit Return when Ready.')

## ADD convert single count items to OOV
## make simple assumption about sentence endings,
## and the position of START and END (sentence boundaries)
'''
words2 = []
previous = 'EMPTY'
sentences = 0
for word in words:
    if previous in ['EMPTY','.','?','!']:
        ## insert word_boundaries at beginning of Brown,
        ## and after end-of-sentence markers (overgenerate due to abbreviations, etc.)
        words2.append('*start_end*')
    if fdist1[word]==1:
        ## words occurring only once are treated as Out of Vocabulary Words
        words2.append('*oov*')
    else:
        words2.append(word)
    previous = word
words2.append('*start_end*') ## assume one additional *start_end* at the end of Brown

fdist2 = nltk.FreqDist(w.lower() for w in words2)
## get Unigram counts for all words occuring more than once
## and also a count for OOV words

print('There are',fdist2['*oov*'],'instances of OOVs')

print('Unigram probabilities including OOV probabilities.')

def get_unigram_probability(word):
    if word in fdist1:
        unigram_probability = fdist2[word]/total_words
    else:
        unigram_probability = fdist2['*oov*']/total_words
    return(unigram_probability)

for word in test_sentence_tokens:
    unigram_probability = get_unigram_probability(word)
    print(word,float('%.3g' % unigram_probability))

input('Pausing: Hit Return when Ready.')
## make new version that models Out of Vocabulary (OOV) words

print('Calculating bigram counts for sentence, including bigrams with sentence boundaries, i.e., *BEGIN* and *END*')
print('Assuming some idealizations: all periods, questions and exclamation marks end sentences;')

bigrams = nltk.bigrams(w.lower() for w in words2)
## get bigrams for words2 (words plus OOV)

cfd = nltk.ConditionalFreqDist(bigrams)

# for token1 in cfd:
#     if not '*oov*' in cfd[token1]:
#         cfd[token1]['*oov*']=1
#         ## fudge so there can be no 
#         ## 0 bigram

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



result = calculate_bigram_freq_of_sentence_token_list(test_sentence_tokens)
'''