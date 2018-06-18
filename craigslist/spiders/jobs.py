# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://seattle.craigslist.org/d/creative-services/search/crs']
    # start_urls = ['https://seattle.craigslist.org/d/creative-services/search/crs/']
    start_urls = ['https://seattle.craigslist.org/sno/crs/d/professional-affordable/6618543409.html']


    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        print(titles)
