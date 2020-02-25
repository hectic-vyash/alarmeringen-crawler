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
        filename = 'alarmeringen.txt'
        with open(filename, 'ab') as f:
            meldingen = response.xpath('//*[@class="msgtitle"]//a/text()').get().strip()
            output = meldingen + "\n"

            f.write(output.encode())            