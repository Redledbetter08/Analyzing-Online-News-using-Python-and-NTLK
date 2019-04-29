import requests
from bs4 import BeautifulSoup

def parse_article(url):

    response = requests.get(url)

    # create soup object
    soup = BeautifulSoup(response.content, 'html.parser')
    # retrieve all paragraphs

    article = soup.find_all('p')

    # perhaps clean up soup object some more before extracting text?
    text = ''
    # get text from paragraphs
    for p in article:
        text += p.get_text()

    return text