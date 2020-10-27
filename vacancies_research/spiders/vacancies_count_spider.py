from os import path
import scrapy


class VacanciesCountSpider(scrapy.Spider):
    name = "vacancies_count"

    def start_requests(self):
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, '..', '..', 'companies.csv'))
        with open(filepath, 'r') as f:
            companies = f.readlines()
            for company in companies:
                yield scrapy.Request(
                    url=f'https://career.habr.com/companies/{company}/vacancies',
                    callback=self.parse
                )

    def parse(self, response):
        for obj in response.css('div.subtabs'):
            yield {
                'company_name': obj.css('a::attr(href)').get().split('/')[2],
                'active_vacancies': obj.css('span.vacancies_active_count::text').get(),
                'inactive_vacancies': obj.css('span.vacancies_inactive_count::text').get()
            }