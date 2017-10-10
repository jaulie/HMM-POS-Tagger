# Hidden Markov Model Part of Speech Tagger

This POS Tagger uses the Bigram (Hidden Markov) Model with the Viterbi Probability Algorithm and a Out of Vocabulary Model described below
to assign parts of speech. It is trained on the Wall Street Journal Corpus.

## Deployment
Run tagger.py on python3. At the top of the script it takes a development file. It outputs into output.pos.
The tagger is trained in probabilities.py, which takes a training file.

### Tagger
A probability table is used to store the bigram probabilities of the POS tags in the training corpus. A likelihood table is used to store emission probabilities for each tag. Finally, a word tags table stores the possible corresponding tags of each word in the corpus. 

The tagger will begin by checking the word tags table: if a word has only been tagged with one kind of tag in the training corpus, it will automatically tag that word with its corresponding tag. This serves the double purpose of immediately tagging all punctuation with itself. If a word is tagged in the training corpus with more than one kind of tag, the tagger will implement the Viterbi algorithm by retrieving the word's emission probability for each corresponding tag and the bigram probability for each tag.

### OOV Model
For now, every Out of Vocabulary word will be assigned a probability of .0001