import scrapy

class QuotesCpider(scrapy.Spider):
    name = "cxy"

    def start_requests(self):
        urls =[
            'https://cxy521.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self, response, **kwargs):
        return None