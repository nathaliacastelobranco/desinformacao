import scrapy

class GloboSpider(scrapy.Spider):
    name = 'globo'
    
    urls = 'https://g1.globo.com/busca/?q=desinformacao&page=%d&ajax=1'
    start_urls = [urls % 1]

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="widget widget--card widget--info"]'):
            title = i.xpath('.//div[@class="widget--info__title product-color "]/text()').get()
            url = i.xpath('.//div[@class="widget--info__text-container"]//@href').get()

            yield {
                'title' : title,
                'url': url
            }

            nextpage = response.xpath('//div[@class="pagination widget"]/a/@href').get()
            if nextpage:
                nextpage = 'https://g1.globo.com/busca/' + nextpage + '&ajax=1'
                yield scrapy.Request(url=nextpage, callback=self.parse)

            
