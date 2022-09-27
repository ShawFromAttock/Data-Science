We can use ``https://quotes.toscrape.com/`` to scrap the quotes within using the following code:

`Code:`
```python
import scrapy
class Quote_spider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {"Titletext" : title }
```
Now we can use both `css` and `xpath` to extract data from the website.

`using xpath`

<a href="https://drive.google.com/uc?export=view&id=13OiksEjDQ7fnF5lQvkoOIuEohvlXuUt_"><img src="https://drive.google.com/uc?export=view&id=13OiksEjDQ7fnF5lQvkoOIuEohvlXuUt_" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

`using css`

<a href="https://drive.google.com/uc?export=view&id=1BKh2n8ruKR-ZAz4h2jcWQp6tGOnLrSWu"><img src="https://drive.google.com/uc?export=view&id=1BKh2n8ruKR-ZAz4h2jcWQp6tGOnLrSWu" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>
