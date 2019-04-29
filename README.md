# Analyzing Online News using Python and NTLK

## CS50 final project by Tom Gurrie

The purpose of this project is to allow the user to compare the text structure and overall sentiment of
of two online news articles. I've built a front end website which will allow the user to simply copy and paste
URLs of online news articles of their choice into two web forms, which can then be submitted by clicking on
the 'Compare' button. Once the articles have been submitted, the python back end will take care of the
text analysis and the user will then be redirected to the 'results' page which will display the results of the
comparison between the two articles.

## Pre-requisites

Below is a list of libraries and packages that are used in my code. Although most of these should
automatically be included in your python setup, it's possible that you may have to download
SentimentIntensityAnalyzer to your IDE if you receive an error message. Enter the following into
your command line to achieve this:

 **python -m nltk.downloader vader_lexicon**

The libraries and packages are:

* Flask
* BeautifulSoup (from bs4)
* Requests
* nltk
* urllib
* plotly
* SentimentIntensityAnalyzer (from nltk.sentiment.vader)

### 1 - Running the website

In order to get the website up and running, navigate to the **project** directory and type in **flask run**.
Next click on the URL displayed in the terminal and you should be taken to the website homepage.

### 2 - Navigating the website

On the homepage the first things you should see are a brief introduction to the project and a sidebar
'menu' on the left hand side of the screen. You can navigate through the website by clicking on the items
on the menu.

* **Home** will redirect you to the homepage
* **Overview** will take you to a more detailed description of what takes place in the analysis
* **Compare** will take you to the page where you submit the URLs of the articles you want to compare
* **Contact** will take you to page containing my picture, email address, GitHub and LinkedIn

Also note the **Menu** button on the home page. By clicking on this button you can toggle the menu sidebar
on and off.

### 3 - Comparing articles

In order to compare articles navigate to the **compare** page using the menu. This will take you through
to a webpage which contains two boxes. Enter in your first URL into the first box and your second URL
into the second box (you can copy and paste URLs into the box directly from your browser). Click compare
to then run the analysis.

### 4 - Results

After clicking compare you will then be taken to the results page, which should contain some text containing
the results of the analysis as well as the sentiment analysis chart. By hovering over the plot and clicking
on the camera icon you can also download the plot as a png.

If you wish to make some further comparisons between articles then you can click on the **compare** button
on the menu which will take you back to the compare page. You can then repeat step 3.
