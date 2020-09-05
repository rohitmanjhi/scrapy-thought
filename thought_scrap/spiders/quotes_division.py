import scrapy
from ..items import ThoughtScrapItem


class QuotesDivisionSpider(scrapy.Spider):
    name = 'quotes_divison'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # extract_first() (for first item)
        items = ThoughtScrapItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            print("************************")
            yield items
