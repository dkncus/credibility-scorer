"""
Module: news_article_scraper.py
Author: Shawn Li
About: Scrape data (titles, url, author, text) from articles
"""

import newspaper
import pymongo
from newspaper import Config, news_pool


class Extractor:
    def __init__(self, collection_name):
        self.url_list_aggregate = []
        self.client = pymongo.MongoClient(
            "mongodb+srv://Dev01:M6pcc9wA01vtOj8B@cluster0-mbyvk.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.FakeNewsCheckerDB
        self.collection = self.db[collection_name]
        self.config = Config()

    def is_collection_init(self):
        if (self.collection.estimated_document_count() == 0):
            self.config.memoize_articles = False  # download all articles that availible from network
            print("No records deteced in the collection, set config.memoize_articles = False")
        else:
            self.config.memoize_articles = True  # eliminate all articles which have already been crawled
            print("Records detected in the collection, set config.memoize_articles = True")
        self.config.fetch_images = False  # no image will be download

    def build_newspaper(self, url_list):
        """
        Builds source objects, network[i] contains categories, feeds, articles
        ------
        Args:
            url_list(list): a list of news network url
        ------
        Returns:
            None
        """
        network = []
        for site in url_list:
            network_papers = newspaper.build(site, config=self.config)
            network.append(network_papers)
            print("Network {0} contains : {1} articles ".format(site, network_papers.size()))

        # Init Muli-Threading Downloads
        news_pool.set(network, threads_per_source=2)
        news_pool.join()
        return network

    def scrape(self, sources):
        """
        Scrape the source articles
        """
        for i in range(len(sources)):
            print('downloading and parsing from -->', sources[i].brand)
            for articles in sources[i].articles:
                # if "cn.nytimes.com"  in article.url or "/es/" in article.url :
                article = newspaper.Article(articles.url.strip(), config=self.config)
                try:
                    article.download()  # downloads HTML content
                    article.parse()  # parse the article
                #                    article.nlp() #  keyword extraction wrapper
                except newspaper.article.ArticleException as err:
                    print(err)
                    continue
                # populate article obj
                news_object = {
                    "title": article.title,
                    "network": sources[i].brand,
                    "url": article.url,
                    "time": (str(article.publish_date).split(" "))[0],
                    "author": article.authors,
                    "articleBody": article.text,
                    #                    "keywords" : article.keywords
                }
                # inserting data in collection
                try:
                    self.collection.insert_one(news_object)
                except newspaper.article.ArticleException as err:
                    print(err)


if __name__ == "__main__":
    network_url = ['http://nytimes.com',
                   'https://www.newyorker.com',
                   'https://www.npr.org',
                   'http://washingtonpost.com',
                   'http://wsj.com',
                   'https://www.businessinsider.com/news',
                   'https://theweek.com/',
                   'https://qz.com/',
                   'https://www.theskimm.com/news',
                   'https://www.afp.com/en',
                   'https://www.pbs.org/',
                   'https://www.bbc.com/news',
                   'https://abcnews.go.com/',
                   'https://www.nbcnews.com/',
                   'https://apnews.com/',
                   'https://www.cbsnews.com/',
                   'https://www.reuters.com/',
                   'https://www.bloomberg.com/',
                   'https://www.usatoday.com/',
                   'https://www.csmonitor.com/',
                   'https://thehill.com/',
                   'https://www.politico.com/',
                   'https://www.axios.com/',
                   'http://www.thefiscaltimes.com/',
                   'https://www.forbes.com/',
                   'https://reason.com/',
                   'https://www.newsy.com/',
                   'https://www.aljazeera.com/',
                   'https://ijr.org/',
                   'https://www.huffpost.com/',
                   'https://www.marketwatch.com/latest-news',
                   'https://www.theatlantic.com/news/',
                   'https://fortune.com/',
                   'https://talkingpointsmemo.com/news',
                   'https://www.vox.com/',
                   'https://theglobalobservatory.org/']

    #
    test = Extractor('Shawn_metadata')
    test.is_collection_init()
    #
    sources = test.build_newspaper(network_url)
    #
    test.scrape(sources)
