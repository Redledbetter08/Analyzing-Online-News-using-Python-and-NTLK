import nltk

# adapted from https://stackoverflow.com/questions/28392860/print-10-most-frequently-occurring-words-of-a-text-that-including-and-excluding
def word_frequency(words_list):
    # get stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    # add additional stopwords
    stopwords.extend(("said","says","would","could","should","mr","miss","mrs"))
    # get frequency distribution for words (not including stopwords)
    words = nltk.FreqDist(w.lower() for w in words_list if w not in stopwords and w.isalpha())
    # retrieve ten most common words
    common_words = words.most_common(10)
    return common_words