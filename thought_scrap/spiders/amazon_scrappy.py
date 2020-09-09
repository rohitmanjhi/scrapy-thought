import scrapy
from ..items import ThoughtScrapItem


class QuotesDivisionSpider(scrapy.Spider):
    name = 'amazon_scrap'
    start_urls = [
        'https://www.amazon.in/s?k=books&ref=nb_sb_noss'
    ]

    def parse(self, response):
        # extract_first() (for first item)
        items = ThoughtScrapItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('.a-size-medium::text').extract()
            author = quotes.css(
                '.a-color-secondary .a-size-base+ .a-size-base::text').extract()
            price = quotes.css(
                '.s-image-square-aspect , .a-spacing-top-small .a-price-whole::text').extract()
            image = quotes.css('.s-image::text').extract()

            items['title'] = title
            items['author'] = author
            items['price'] = price
            items['image'] = image
            print("************************")
            yield items
