# What are Selectors?
When we are scraping the web pages, we need to extract a certain part of the HTML source by using the mechanism called selectors, achieved by using either XPath or CSS expressions. Selectors are built upon the lxml library, which processes the XML and HTML in Python language.
```python
import scrapy


class MySpider(scrapy.Spider):
    name = "random quotes"
    url = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        title = response.css("title::text").extract()
        yield {"titletext" : title}
```

