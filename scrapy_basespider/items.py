from scrapy.item import Item, Field

class JobItem(Item):
    title = Field()
    link = Field()

