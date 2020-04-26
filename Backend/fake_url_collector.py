import newspaper
import pymongo


class Scraper:

    def __init__(self):
        self.url_list_aggregate = []
        self.client = pymongo.MongoClient("mongodb+srv://DBuser_Mitchell:KB1KS69n01GKeWPo@cluster0-mbyvk.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.FakeNewsCheckerDB
        self.collection = self.db.mitchell_testing

    def add_urls_to_db(self, url_list):

        for url in url_list:

            source = newspaper.build(url, memoize_articles = False)
            website_title = source.brand

            for article in source.articles:

                article_url = article.url
                source_entry = {
                    "website": website_title,
                    "url": article_url
                }

                self.url_list_aggregate.append(source_entry)

        self.collection.insert_many(self.url_list_aggregate)
        self.url_list_aggregate.clear()
