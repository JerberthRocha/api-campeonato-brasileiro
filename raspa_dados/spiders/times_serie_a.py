import scrapy


class TimesSerieASpider(scrapy.Spider):
    name = "times_serie_a"

    start_urls = [
        'https://www.mg.superesportes.com.br/app/noticias/futebol/futebol-nacional/2022/11/13/noticia_futebol_nacional,3979697/campeonato-brasileiro-de-2023-veja-quem-sao-os-20-clubes-confirmados.shtml',
    ]

    def parse(self, response):
        times = response.xpath("*//div/ol/li/text()").getall()
        for time in times:
            yield {
                'nome': time,
                'divisao_id': 1,
            }