from flask import Flask, abort, redirect, render_template, request, Markup
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from urllib.request import urlopen
from soup import parse_article
from vader import sentiment_analysis
from freq_dist import word_frequency
from sentiment_plot import sentiment_plot


# initialize web app
app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")


@app.route("/contact", methods=["GET"])
def contact():

    if request.method == "GET":

        return render_template("contact.html")

@app.route("/overview", methods=["GET"])
def overview():

    if request.method == "GET":

        return render_template("overview.html")


@app.route("/compare", methods=["GET", "POST"])
def compare():

    if request.method == 'GET':

        return render_template("compare.html")

    if request.method == 'POST':

        """Handle requests for / via GET (and POST)"""
        # if one of the boxes has missing data then render error
        if not request.form.get('url1') or not request.form.get('url2'):
            return render_template('error.html', error = 'Error', text = 'Please enter 2 valid URLs in the boxes!')

        # retrieve URL1
        url1 = request.form.get('url1')
        print(url1)
        # retrieve URL2
        url2 = request.form.get('url2')
        print(url2)

        # if url is CNN or huffington post then return error
        if "cnn.com" in url1 or "huffingtonpost.com" in url1:
            return render_template("error.html",error = 'Website Not Supported', text = 'Sorry, articles from this website are not currently not supported...')
         # if url is CNN or huffington post then return error
        if "cnn.com" in url2 or "huffingtonpost.com" in url2:
            return render_template("error.html",error = 'Website Not Supported', text = 'Sorry, articles from this website are not currently not supported...')
        # parse articles
        text1 = parse_article(url1)
        text2 = parse_article(url2)


        # get sentences
        sentences1 = sent_tokenize(text1)
        sentences2 = sent_tokenize(text2)

        # get words
        words1 = word_tokenize(text1)
        words2 = word_tokenize(text2)

        # most common words
        freq1 = word_frequency(words1)
        freq2 = word_frequency(words2)
        freq = list(zip(freq1, freq2))

        # run vader sentiment analysis
        sentiment1 = sentiment_analysis(sentences1)
        sentiment2 = sentiment_analysis(sentences2)

        # chart
        my_plot_div = sentiment_plot(sentiment1, sentiment2)

        # render template
        return render_template("result.html",
                                sentence_num1 = len(sentences1), # get number of sentences from first article
                                sentence_num2 = len(sentences2), # get number of sentences from second article
                                words = freq, # get most common words from frequency distribution
                                characters1 = len(text1), # get number of characters from first article
                                characters2 = len(text2), # get number of characters from second article
                                quotes1 = int((text1.count("\"") + text1.count("“") + text1.count("”"))/2), # get number of quotations in first article
                                quotes2 = int((text2.count("\"") + text2.count("“") + text2.count("”"))/2), # get number of quotations in second article
                                chart = Markup(my_plot_div)) # render sentiment chart
