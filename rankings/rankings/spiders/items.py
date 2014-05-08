# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class rankItem(Item):
    name = Field()
    rank = Field()
    overallScore = Field()
    teachingScore = Field()
    internationalOutlook = Field()
    industryIncome = Field()
    research = Field()
    citations = Field()
    textBelow = Field()


    
