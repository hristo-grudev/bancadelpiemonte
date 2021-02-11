import scrapy


class BancadelpiemonteItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()

