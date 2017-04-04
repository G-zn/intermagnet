# -*- coding: utf-8 -*-

# Scrapy settings for nasa project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'nasa'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

SPIDER_MODULES = ['nasa.spiders']
NEWSPIDER_MODULE = 'nasa.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nasa (+http://www.yourdomain.com)'
