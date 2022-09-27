# Middleware:
The spider middleware is a set of hooks into Scrapy's spider processing system that you can use to include custom code to handle replies given to spiders for processing as well as requests and objects produced by spiders.
```python
SPIDER_MIDDLEWARES = {
    'myproject.middlewares.CustomSpiderMiddleware': 543,
}
```

# User_Agents:
User Agents are strings that help the website you are scraping know what application, operating system (OSX/Windows/Linux), browser (Chrome/Firefox/Internet Explorer), etc. the user using their website is using to make a request to them. They are transmitted with the request headers to the server.

Here is an example User agent sent when you visit a website with a Chrome browser:
```python
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36
```
You must also establish user-agents on each request while scraping a website because if you don't, the website may reject your requests since it believes you aren't a legitimate user. In the case of Scrapy. When you use Scrapy with the default settings, the user-agent your spider sends is the following by default:
```python
Scrapy/VERSION (+https://scrapy.org)
```
This user agent will make it easy for the website to simply prohibit you from scraping the site by identifying your requests as originating from a web scraper.
Because of this, we must control the user-agents that Scrapy sends along with our requests.
