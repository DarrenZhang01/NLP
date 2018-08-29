# Referrence from http://python.jobbole.com/88874/
import nltk
import urllib.request
from bs4 import BeautifulSoup

# nltk.download()
url = "http://www.darrenzhang.com"
response = urllib.request.urlopen(url)
html = response.read()
# print(html)
soup = BeautifulSoup(html,"html5lib")
# print(soup)
text = soup.get_text(strip=True)
# print(text)
tokens = text.split()
# print(tokens)
freq = nltk.FreqDist(tokens)
# Plot the result into a graph
freq.plot(20, cumulative=False, title="word frequency in " + url)
