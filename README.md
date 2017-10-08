# Hidden Markov Model Part of Speech Tagger

This POS Tagger uses the Bigram (Hidden Markov) Model with the Viterbi Probability Algorithm and a Out of Vocabulary Model described below
to assign parts of speech. It is trained on the Wall Street Journal Corpus.

### OOV Model

### BackOff Model
If a bigram has a zero count, backoff to the unigram model.
	!!Has not been implemented!!