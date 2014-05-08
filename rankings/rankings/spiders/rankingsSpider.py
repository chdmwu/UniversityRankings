from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from items import *
import time

class RankingsSpider(Spider):
    name = "rankings"
    allowed_domains = ["http://www.timeshighereducation.co.uk"]
    with open('./schools.txt') as f:
        start_urls = f.read().splitlines()


    def parse(self, response):
        sel = Selector(response)
        item = rankItem()
        item['name'] = sel.xpath('//h1/text()').extract();
        item['rank'] = sel.xpath('//span[@class="rank"]/text()').extract()
        item['overallScore'] = sel.xpath('//li[@class="over-score"]//span[@class="fig"]/text()').extract()
        item['teachingScore'] = sel.xpath('//li[@class="teaching"]//span[@class="fig"]/text()').extract()
        item['internationalOutlook'] = sel.xpath('//li[@class="inter-out"]//span[@class="fig"]/text()').extract()
        item['industryIncome'] = sel.xpath('//li[@class="ind-income"]//span[@class="fig"]/text()').extract()
        print(item['industryIncome'])
        item['research'] = sel.xpath('//li[@class="research"]//span[@class="fig"]/text()').extract()
        item['citations'] = sel.xpath('//li[@class="citations"]//span[@class="fig"]/text()').extract()
        item['textBelow'] = sel.xpath('//section[@class="infomation"]/p/text()').extract()
        return item
        
