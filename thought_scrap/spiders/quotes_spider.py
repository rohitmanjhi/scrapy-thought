import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # extract_first() (for first item)
        title = response.css('title::text').extract()
        print("*************************")
        yield {'titlename': title}
