import scrapy

from scrapy.loader import ItemLoader
from ..items import BancadelpiemonteItem
from itemloaders.processors import TakeFirst


class BancadelpiemonteSpider(scrapy.Spider):
	name = 'bancadelpiemonte'
	start_urls = ['https://www.bancadelpiemonte.it/la-banca/news/']

	def parse(self, response):
		post_links = response.xpath('//div[@class="post-content-text"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@class="next page-numbers"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="post-content-text"]//p//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=BancadelpiemonteItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		return item.load_item()
