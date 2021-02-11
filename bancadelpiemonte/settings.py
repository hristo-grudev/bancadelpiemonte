BOT_NAME = 'bancadelpiemonte'

SPIDER_MODULES = ['bancadelpiemonte.spiders']
NEWSPIDER_MODULE = 'bancadelpiemonte.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bancadelpiemonte.pipelines.BancadelpiemontePipeline': 100,

}