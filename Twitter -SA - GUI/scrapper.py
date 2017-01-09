# This program scraps twitter pages for tweets. Is written by jeev20. https://github.com/jeev20

from bs4 import BeautifulSoup
from urllib import *
import urllib
from textblob import TextBlob
import sys
import time
import webbrowser


# open a public URL, in this case, the webbrowser
url1 = "https://twitter.com/twitter"
webbrowser.open_new_tab(url1)

time.sleep(3)


# user can input twitter account
url = raw_input("Please paste link to twitter account : ")



#input webaddress of the twitter account
webadd = urllib.urlopen(url).read()
soup = BeautifulSoup(webadd, "html.parser")


#tweet title extraction
def title():
	return(soup.title.text)


# function to return latest tweet

def getText():
	for tweets in soup.find_all('div',{"class": "content"}):
		twe = (tweets.find('p').text)
		return twe
		
def time():
	for tweets in soup.find_all('a',class_="tweet-timestamp js-permalink js-nav js-tooltip"):
		time = (tweets.get_text())
		return time		


# function returning sentiment analysis value for the tweet
def getTextsa():		
	twe = getText()
	test = TextBlob(twe)
	sa = (test.sentiment.polarity)
	return sa


#used for debugging
#prints the tweet and the sentiment analysis value 
print title()
print ""
print getText()
print ""
print time()
print ""
print "Sentiment Value is: ",float ("%.4f" %(getTextsa()))

