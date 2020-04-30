#

from newspaper import Article

# extract specific information from a webpage
url = 'https://blogs.findlaw.com/blotter/2009/04/forgive-me-father-for-i-am-about-to-sin-florida-priest-stabbed-in-confessional-forgives-attacker.html'
article = Article(url)  # turn url string into object
article.download()      # download the webpage
article.parse()         # splits up page into sections


# print objects for parsed data
#article.html

print("author")
print(article.authors)
print("publish date")
print(article.publish_date)
print("text")
print(article.text)
print("top_image")
print(article.top_image)
print("movies")
print(article.movies)
