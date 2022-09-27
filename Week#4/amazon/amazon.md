# Using scrapy to login to forms:
```python
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]
    def parse(self, response):
        token = response.css('form input::attr(values)').extract()
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'zainalishah51471@gmail.com',
            'password' : 'gggggeezzzzz'
        }, callback = self.start_scraping)
    def start_scraping(self,response):
        open_in_browser(response)
        items = QuotetItem()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
```

# Amazon Scraping:
```python
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A3248684011&dc&ds=v1%3AI91B%2BdZTSA96JFKRasp6HXQXmnwcDXjnGP3sdGiHpdM&qid=1663938140&ref=sr_ex_n_1']

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('.a-size-base-plus::text').extract()
        product_price = response.css('.a-size-base-plus').css('::text').extract()
        product_image = response.css('.s-height-equalized .s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_image'] = product_image

        yield  items
```
# Items:
```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazontutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_author = scrapy.Field()
    product_price = scrapy.Field()
    product_imagelink = scrapy.Field()
    pass
```
<a href="https://drive.google.com/uc?export=view&id=19MTAIuZF44TeHRvJCGRPDwd0Qwc4gQku"><img src="https://drive.google.com/uc?export=view&id=19MTAIuZF44TeHRvJCGRPDwd0Qwc4gQku" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>
