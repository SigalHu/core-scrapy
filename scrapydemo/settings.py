# -*- coding: utf-8 -*-

# Scrapy settings for scrapydemo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
# http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapydemo'
BOT_VERSION = '1.0.0'  # 蜘蛛版本号

SPIDER_MODULES = ['scrapydemo.spiders']
NEWSPIDER_MODULE = 'scrapydemo.spiders'
DEFAULT_ITEM_CLASS = 'scrapydemo.items.DmozItem'

ITEM_PIPELINES = {
    # 'scrapydemo.pipelines.FilterWordsPipeline': 1,
    # 'scrapydemo.pipelines.JsonWriterPipeline': 2,
    # 'scrapydemo.pipelines.JsonExportPipeline': 3,
    'scrapydemo.pipelines.PostgresPipeline': 4,
}
DOWNLOADER_MIDDLEWARES = {
    # 这里是下载中间件
}
SPIDER_MIDDLEWARES = {
    # 这是爬虫中间件， 543是运行的优先级
    # 'myproject.middlewares.UrlUniqueMiddleware': 543,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapydemo (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

DOWNLOAD_TIMEOUT = 15
DOWNLOAD_DELAY = 0.1
LOG_LEVEL = "INFO"
LOG_STDOUT = True
LOG_FILE = "log/spider.log"

DATABASE = {'drivername': 'postgres',
            'host': '10.0.0.154',
            'port': '5432',
            'username': 'root',
            'password': 'changeme',
            'database': 'postgres'}
