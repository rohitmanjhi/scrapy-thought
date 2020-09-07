import scrapy
from ..items import ThoughtScrapItem


class QuotesDivisionSpider(scrapy.Spider):
    name = 'quotes_pages_url'
    page_number = 1
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
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

        # Get pages
        next_page = 'http://quotes.toscrape.com/page/' + \
            str(QuotesDivisionSpider.page_number)+'/'
        # next_page = response.css('li.next a::attr(href)').get()
        print('next_page: ', next_page)

        if QuotesDivisionSpider.page_number < 11:
            QuotesDivisionSpider.page_number += 1
            yield response.follow(next_page, self.parse)
