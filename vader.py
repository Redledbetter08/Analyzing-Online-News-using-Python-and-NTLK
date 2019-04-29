import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(article):

     # set initial sentiment scores
     neg = 0
     pos = 0
     neu = 0
     # initialize model
     sid = SentimentIntensityAnalyzer()
     # pass each sentence through analyzer, extracting the positive, negative and neutral sentiment for each sentence
     for sentence in article:
          ss = sid.polarity_scores(sentence)
          neg += ss['neg']
          pos += ss['pos']
          neu += ss['neu']

     return (pos, neg, neu)

