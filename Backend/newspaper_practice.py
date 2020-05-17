"""
Name : newspaper_practice.py
Date : Sat Apr 25th 2020
Author: Peter Stine
Modification History: -
    Peter Stine, Thur Apr 29th 2020

Synopsis: Shows basic usage of newspaper library and sys library to detect
    if an article has a body or not by returning the number of bytes in
    an object

Methods: <List of methods supported in the module>
e.g. “getX() – Returns x Variable”
e.g. “setY(y_set) – Sets the Y variable”

Global Variables:
    article - contains entire parsed html webpage
    url - sample url of news article from findlaw.com
"""

import sys
from newspaper import Article

# extract specific information from a webpage
url = 'https://blogs.findlaw.com/blotter/2009/04/forgive-me-father-for-i-am-about-to-sin-florida-priest-stabbed-in-confessional-forgives-attacker.html'
article = Article(url)  # turn url string into object
article.download()      # download the webpage
article.parse()         # splits up page into useful objects listed below


# print objects for parsed data
#article.html # This will print the entire page's html dump, not useful

# THis function is just to shorten sys.getsizeof(x)
def size(obj):
    return sys.getsizeof(obj)


print("author")
print(article.authors)
print("publish date")
print(article.publish_date)

print("text = ", end='')
print(size(article.text), end='')
print(" bytes ")

print("top_image")
print(article.top_image)
print("movies")
print(article.movies)
print(article)