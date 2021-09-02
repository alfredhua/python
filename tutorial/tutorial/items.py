# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StockstartItem(scrapy.Item):
    code = scrapy.Field()
    abbr = scrapy.Field()
    last_trade = scrapy.Field()
    chg_ratio = scrapy.Field()
    cha_amt = scrapy.Field()
    volumn = scrapy.Field()
    turn_over = scrapy.Field()