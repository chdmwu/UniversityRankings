# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'rankings'

SPIDER_MODULES = ['rankings.spiders']
NEWSPIDER_MODULE = 'rankings.spiders'

ITEM_PIPELINES = {
    'rankings.pipelines.CSVPipeline': 300,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
