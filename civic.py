import scrapy


class QuotesSpider(scrapy.Spider):
    name = "civic"
    start_urls = [
        'https://www.autodeft.com/tags/honda-civic/',
    ]

    def parse(self, response):
        for quote in response.css('div.row'):
            yield {
                'title': quote.css('a::text').get(),
                'news': quote.css('p::text').get(),
                'director': quote.css('a ::text').get(),
                'date': quote.css('<li class="date"><a href="#">30 ต.ค. 2565</a></li>::text').get(),
            }

        next_page = response.css('a./tags/honda-civic/3').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        df = pd.DataFrame(zip(title.article), columns = ['Title','Article'])
        print(df)
