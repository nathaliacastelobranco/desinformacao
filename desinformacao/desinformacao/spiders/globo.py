import scrapy


class GloboSpider(scrapy.Spider):
    name = 'globo'
    allowed_domains = ['g1.globo.com']
    start_urls = ['http://g1.globo.com/']

    def parse(self, response):
        pass
