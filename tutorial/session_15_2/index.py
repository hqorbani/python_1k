import nltk
# nltk.download()
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
fourgram_measures = nltk.collocations.QuadgramAssocMeasures()
finder = BigramCollocationFinder.from_words(
    nltk.corpus.genesis.words('shallow.txt'))
print(finder.nbest(bigram_measures.pmi, 10)) 