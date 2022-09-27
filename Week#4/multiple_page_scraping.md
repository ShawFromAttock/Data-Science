# Using next button:

`Code:`
```python
import scrapy
from ..items import QuotetItem


class Quotes_to_scrape(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]
    def parse(self, response):
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

            next_page = response.css('li.next a::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback = self.parse)
```
 
# Pagination:
The process of pagination, commonly referred to as paging, involves separating a document into distinct pages, putting a collection of material on each page. Each of these unique pages has a unique url. Therefore, we must scrape these sites one by one using each of these urls. However, you should be aware of when to halt pagination. In most cases, pages have a next button. When a page is done, this button is disabled. When the next page button is active, this technique is utilised to obtain the URL of each page, and when it is disabled, no pages are left for scraping.

`Code:`
```python
import scrapy
from ..items import QuotetItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/page/1/"
    ]
    def parse(self, response):
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

            next_page = "https://quotes.toscrape.com/page/" + str(QuoteSpider.page_number) + '/'
            print(next_page)
            if QuoteSpider.page_number < 11:
                QuoteSpider.page_number += 1
                yield response.follow(next_page, callback = self.parse)
 ```
 
 
