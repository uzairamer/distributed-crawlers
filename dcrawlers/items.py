import scrapy


class DcrawlersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HackerNewsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    item_id = scrapy.Field()
    pass
