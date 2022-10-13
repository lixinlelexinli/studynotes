# -*- coding: utf-8 -*-
import scrapy


class LjSpider(scrapy.Spider):
    name = 'lj'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/pg{}/'.format(num) for num in range(2,101)]
    # print(start_urls)

    def parse(self, response):

        urls = response.xpath('//div/div[@class="title"]/a/@href').extract()

        for info_url in urls:
            yield scrapy.Request(info_url,callback=self.parse_info)

    def parse_info(self,response):

        # 基本属性
        info_keys = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li/span/text()').extract()
        info_values = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li/text()').extract()

        # 交易属性
        transaction_keys = response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li/span[1]/text()').extract()
        transaction_values = response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li/span[2]/text()').extract()

        # 总价，单价
        total_price_key = ["总价（万元）"]
        total_price_value = response.xpath('//span[@class="total"]/text()').extract()
        unit_price_key = ["单价（元/平米）"]
        unit_price_value = response.xpath('//span[@class="unitPriceValue"]/text()').extract()

        # 小区
        communityName_key = response.xpath('//div[@class="aroundInfo"]/div[@class="communityName"]/span/text()').extract()
        communityName_value = response.xpath('//div[@class="aroundInfo"]/div[@class="communityName"]/a[1]/text()').extract()

        # 所在区域
        areaName_key = response.xpath('//div[@class="aroundInfo"]/div[@class="areaName"]/span[1]/text()').extract()
        areaName_value = response.xpath('string(//div[@class="aroundInfo"]/div[@class="areaName"]/span[@class="info"])').extract()

        # 链家编号
        houseRecord_key = response.xpath('//div[@class="aroundInfo"]/div[@class="houseRecord"]/span[1]/text()').extract()
        houseRecord_value = response.xpath('//div[@class="aroundInfo"]/div[@class="houseRecord"]/span[2]/text()').extract()

        keys = houseRecord_key + total_price_key + unit_price_key + communityName_key + areaName_key + info_keys + transaction_keys
        values =houseRecord_value + total_price_value + unit_price_value + communityName_value + areaName_value + info_values + transaction_values

        infos = {}
        for kkey, vvalue in zip(keys, values):
            # print(kkey,vvalue,"\n")
            infos[kkey] = vvalue

        yield infos
        # for k,v in zip(keys,values):
        #     print(k,v)