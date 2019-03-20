from scrapy import Spider
from scrapy.selector import Selector


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https: // stackoverflow.com /?tab = featured"
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = StackSItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question=hyperlink"]/@href').extract()[0]
