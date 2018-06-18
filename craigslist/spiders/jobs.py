# -*- coding: utf-8 -*-
# import scrapy


# class JobsSpider(scrapy.Spider):
#     name = 'jobs'
#     allowed_domains = ['https://seattle.craigslist.org/d/creative-services/search/crs']
#     # start_urls = ['https://seattle.craigslist.org/d/creative-services/search/crs/']
#     start_urls = ['https://seattle.craigslist.org/d/creative-services/search/crs']


#     def parse(self, response):
#         titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
#         print(titles)

# -*- coding: utf-8 -*-
import scrapy
 
class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["craigslist.org"]
    start_urls = ['https://seattle.craigslist.org/d/creative-services/search/crs']
 
    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        print(titles)
        for title in titles:
          yield {'Title' : title}