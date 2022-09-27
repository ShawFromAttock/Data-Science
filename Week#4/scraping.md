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
# Robots.txt:
Robots.txt is just a text file that the robots respect, it cannot forbid you from doing anything. A good web spider will first read the robots. txt file and adhere to the rule, though it's not compulsory. Conducting a scrapy crawl command for a project will first look for the robots.
# Environment:
```python
PS C:\Users\zaina\PycharmProjects\sheesh> scrapy startproject gg
New Scrapy project 'gg', using template directory 'C:\Users\zaina\AppData\Local\Programs\Python\Python310\lib\site-packages\scrapy\templates\project', created in:

You can start your first spider with:
    cd gg
    scrapy genspider example example.com
```
