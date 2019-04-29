# Analyzing Online News using Python and NTLK

## Introduction

The goal of this project is to allow the user to make both semantic and syntactic comparison between 2 online news articles.
This has been inspired the recent events regarding the 2016 US election and "fake news" as well as the focus being made on
how online media (particularly social media) is able to specifically users based upon their interests and online activity.
The result of this is that we are constantly receiving heavily targeted and personalized web content, essentially creating a 'bubble'
where we are only exposed to news from sources that are deemed to be suitable for us.

My initial idea was to attempt to classify the amount of political bias contained in a news story. For
example, a right-leaning news website may use different sentiment and language compared to a left-leaning site,
even though they are reporting on exactly the same story. It soon became apparent however that this
was quite quickly going to become an incredibly complex task as it would require me to gather enormous amounts of articles
from various different websites and attempt to classify them as 'left' or 'right'. This also opens up the possibility of
introducing my own bias into the analysis as I would have to personally classify those articles myself as either being left
or right leaning. Instead, I thought it made more sense to focus on the differences between two articles in terms of sentiment
and syntactic structure, hence allowing the user to observe the differences for themselves and draw their own conclusions on the
amount of bias present in a news article.

In order to achieve the above I utilized the popular Python natural language processing library NLTK to
anaylze the news articles. To make the project accessible to everyone I opted to build an interactive
website where the user simply needs to copy and paste URLs from selected news articles and input them
into the forms on the compare page. The python backend then reads the HTML from the URLs, parses out
the text which is then passed to the sentiment anaylzer. Once the text has been analyzed the results
are then displayed back to the user using a plotly chart and some HTML tables.

### Parsing HTML

In order to parse the text from the webpage, I used the library BeautifulSoup. I specifically searched for all
paragraph tags in the html in order to retrieve the text. Although this method often results in the inclusion
of some 'noise' at the beginning and end of the text, I felt this was necessary and the best and reliable
way of ensuring that all the article text is read from multiple different websites.

### NLTK

NLTK was used in Pset 6 for similarites and I had used it before on an online course so it seemed to me an
obvious choice to use for my sentiment analysis. For my sentiment analyzer, I ended up using Vader, a valence-based
sentiment analyzer. I utilized sent_tokenize to split the text into sentences which could then be passed into the
analyzer. I then calculated the overall positive, negative and neutral sentiment distrubution to determine the degree
of positive, negative and neutral sentiment present in the article.

I also utilized the FreqDist function which creates a frequency distribution of the all of the words in the text. By using
the most_common method on the distribution I could then extract the 10 most common words in the article. I also used
the built in nltk list of stop words to prevent stop words from showing up in the most common words. After some experimentation
I also added some additional stopwords myself which seemed to be appearing quite often such as 'said' and 'mr'.


### Python text analysis

As well as using NLTK, I also used some basic python to extract the number of characters and number of
quotations contained in the article. To get the number of quotations, I had to ensure that multiple
different encodings of quotation marks were accepted and then divide the total by 2 in order to reach
the true number of quotations. The number of characters and sentences were simply calculated by calling
len on the full text and the sentence tokenized text.

### Website

The web application is built using Flask and adopts the bootstrap template listed here:

https://startbootstrap.com/template-overviews/simple-sidebar/

It consists of the following pages which can be navigated to via the sidebar:

* Home - The homepage gives an introduction to the project.
* Overview - This page gives a more detailed and technical description of the project.
* Compare - This page contains the web forms where the user is required to input the URLs which will then be sent to the backend.
* Contact - This page contains a picture of myself, my email address as well as links to my GitHub and LinkedIn.

There are also two additonal pages:

* Error - this page contains error messages that are triggered by certain events.
* Result - this page displays the results of the analysis to the user.

### Plotly

In order to effectively display the distribution of positive, negative and neutral sentiment, I opted to
use donut charts. These have been generated using plotly which allows me to convert the chart into HTML
which can then be rendered directly in the page. Most of the formatting for the graph is pre-generated
statically in sentiment_plot.py but the values and labels are passed to the function from application.py.

I had quite a lot of difficulty figuring out the resizing of the graph but eventually settled on setting the
size directly in the plot using the layout and width properties.