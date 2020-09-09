import scrapy
from ..items import ThoughtScrapItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class QuotesDivisionSpider(scrapy.Spider):
    name = 'quotes_login'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        print('token: ', token)
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': "rohit@gmail.com",
            "password": "rohit123"
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
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
