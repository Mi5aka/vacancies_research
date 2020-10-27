import scrapy


class CompaniesSpider(scrapy.Spider):
    name = "companies"

    def start_requests(self):
        for page in range(1, 31):
            yield scrapy.Request(
                url=f'https://career.habr.com/companies?page={page}&with_vacancies=1',
                callback=self.parse
            )

    def parse(self, response):
        for company in response.css('div.companies-item-name a::attr(href)'):
            name = str(company).split("data='/companies/")[1]
            yield {
                'name': name[0:-2]
            }
