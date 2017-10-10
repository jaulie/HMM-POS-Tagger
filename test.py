import nltk
from nltk.corpus import brown

# b_words = brown.words()
my_corpus = ['hello', 'there', 'friend', 'friend', 'friends']
print('My corpus:', my_corpus)

my_fdist = nltk.FreqDist(w.lower() for w in my_corpus)
print('{:>8}{:^11}{:^11}'.format('word','occurance','probability'))

for word in my_corpus:
	occurance = my_fdist[word]
	prob_occurance = occurance / len(my_corpus)
	print('{:>8}{:^11}{:^11}'.format(word,occurance,prob_occurance))


	