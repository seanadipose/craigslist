import scrapy
 
class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["craigslist.org"]
    start_urls = ['https://seattle.craigslist.org/d/creative-services/search/crs']
 
    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        for job in jobs:
          title = job.xpath('a/text()').extract_first()
          address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
          relative_url = job.xpath('a/@href').extract_first()
          absolute_url = "https://seattle.craigslist.org" + relative_url
          yield{'URL':absolute_url, Title: 'title', 'Address': address}
          