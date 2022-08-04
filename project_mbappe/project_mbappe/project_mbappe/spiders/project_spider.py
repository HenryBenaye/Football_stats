import scrapy


class ProjectMbappeSpider(scrapy.Spider):
    name = "project_mbappe"
    start_urls = ['https://fbref.com/en/players/42fd9c7f/Kylian-Mbappe']

    def parse(self, response):
        print(response.text)
