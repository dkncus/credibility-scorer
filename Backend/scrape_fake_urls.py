from fake_url_collector import Scraper

fake_news_scraper = Scraper()
fake_news_scraper.add_urls_to_db(['http://beforeitsnews.com/',
                                  'http://bients.com/',
                                  'http://www.infowars.com/',
                                  'http://conservativefrontline.com/'])