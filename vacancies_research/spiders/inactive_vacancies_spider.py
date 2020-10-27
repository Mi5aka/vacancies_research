from os import path
import scrapy


class InactiveVacanciesSpider(scrapy.Spider):
    name = "inactive_vacancies"

    def get_clear_data(self):
        clear_data = []
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, '..', '..', 'vacancies_count.csv'))
        with open(filepath, 'r') as f:
            companies = f.readlines()
            for company in companies[1:]:
                data = company[:-1].split(',')
                if '' not in data:
                    clear_data.append(data)
        return clear_data

    def start_requests(self):
        data = self.get_clear_data()
        for obj in data:
            pages = round(int(obj[2]) / 25) + 2
            for page in range(1, pages):
                yield scrapy.Request(
                    url=f'https://career.habr.com/companies/{obj[0]}/vacancies/inactive?page={page}',
                    callback=self.parse
                )

    def parse(self, response):
        for obj in response.css('div.vacancy-card__inner'):
            yield {
                'date': obj.css('time::attr(datetime)').get()[0:10],
                'title': obj.css('div.vacancy-card__title a::text').get(),
                'skills': obj.css('div.vacancy-card__skills a::text').getall()
            }