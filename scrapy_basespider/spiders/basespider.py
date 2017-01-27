from scrapy import Spider
from scrapy.selector import Selector
from scrapy_basespider.items import JobItem

class JobSpider(Spider):
    
    name = 'software_jobs'
    allowed_domains = ['seek.com.au']
    start_urls = ['https://www.seek.com.au/jobs?keywords=software+engineer']

    def parse(self, response):
        
        titles = response.xpath('//article')
        items = []

        for each in titles:
            item = JobItem()
            item['title'] = each.xpath('@aria-label').extract()
            item['link'] = each.xpath('h1/a/@href').extract()
            items.append(item)

            print item['title'], item['link']

        return items