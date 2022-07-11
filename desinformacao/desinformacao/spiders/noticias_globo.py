from tracemalloc import start
import scrapy
import json

class NoticiasGloboSpider(scrapy.Spider):
    name = 'noticias-globo'

    urls = []
    with open('links.json') as json_data:
        data = json.load(json_data)
        for i in range(len(data)):
            url = data[i]['url']
            urls.append(url)

    start_urls = urls
            
    def parse(self, response):
        for i in response.xpath('//div[@class="glb-grid"]'):
            title = i.xpath('.//h1[@class="content-head__title"]//text()').get()
            date = i.xpath('.//div[@class="content-publication-data__text"]//p[@class="content-publication-data__updated"]/time/text()').get()
            text = i.xpath('.//div[@class="mc-article-body"]//div[@class="mc-column content-text active-extra-styles "]//text()').getall()
            url = response.url

            yield {
                'title' : title,
                'date' : date,
                'text' : text,
                'url': url
            }
