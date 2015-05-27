import scrapy
from linkExtractor.items import Iframe

class MashableSpider(scrapy.Spider):
	name = "mashable"
	allowed_domains = ["mashable.com"]
	start_urls = [
		"http://mashable.com/2015/05/26/ecocapsule-pods/"
	]

	def parse(self, response):
		for selector in response.xpath('.//iframe'):
			item = Iframe()
			item['src'] = selector.xpath('@src').extract()
			yield item
