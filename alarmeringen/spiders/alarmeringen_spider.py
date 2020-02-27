import scrapy


class AlarmeringenSpider(scrapy.Spider):
    name = "alarmeringen"

    def start_requests(self):
        urls = [
            'https://alarmeringen.nl/zuid-holland/haaglanden/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # print("reponse:" , response.selector.xpath('').get())

        filename = 'alarmeringen.txt'
        with open(filename, 'ab') as f:
            meldingen = response.xpath('//*[@class="msgtitle"]//a/text()').get().strip()
            datum = response.xpath('//span[@class="date"]/text()').get()
            output = datum[17:] + meldingen + "\n"

            f.write(output.encode())