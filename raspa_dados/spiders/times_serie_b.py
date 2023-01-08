import scrapy


class TimesSerieBSpider(scrapy.Spider):
    name = "times_serie_b"

    start_urls = [
        'https://ge.globo.com/sp/tem-esporte/futebol/brasileirao-serie-b/noticia/2022/11/13/serie-b-de-2023-tem-todos-os-clubes-confirmados-veja-a-lista-completa.ghtml',
    ]

    def parse(self, response):
        times = response.xpath("*//li/a/text()").getall()[:19]
        for time in times:
            yield {
                'nome': time,
                'divisao_id': 2,
            }
