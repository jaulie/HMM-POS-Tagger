# Hidden Markov Model Part of Speech Tagger

This POS Tagger uses the Bigram (Hidden Markov) Model with the Viterbi Probability Algorithm and a Out of Vocabulary Model described below
to assign parts of speech. It is trained on the Wall Street Journal Corpus.

### Tagger
A probability table is used to store the bigram probabilities of the POS tags in the training corpus. A likelihood table is used to store emission probabilities for each tag. Finally, a word tags table stores the possible corresponding tags of each word in the corpus. 

The tagger will begin by checking the word tags table: if a word has only been tagged with one kind of tag in the training corpus, it will automatically tag that word with its corresponding tag. This serves the double purpose of immediately tagging all punctuation with itself. If a word is tagged in the training corpus with more than one kind of tag, the tagger will implement the Viterbi algorithm by retrieving the word's emission probability for each corresponding tag and the bigram probability for each tag.

In the Viterbi algorithm (bigram model), to determine the probability that a word in the corpus should be tagged with a certain tag, knowing the tag of the previous word and its corresponding probability is necessary. For the purposes of this Tagger, only the top three probabilities of the previous tag will be considered. 
So, to give an example, if the word buffalo is tagged in the training corpus with NNS, N, V, PN, but the probability of buffalo being tagged as a proper noun is relatively lower, the probability for PN will be thrown out and not used in the bigram model.

### OOV Model
For now, every Out of Vocabulary word will be assigned a probability of .0001