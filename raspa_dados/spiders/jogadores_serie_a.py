import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class PalmeirasSpider(scrapy.Spider):
    name = "sep"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/palmeiras',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 1
            }


class FlamengoSpider(scrapy.Spider):
    name = "fla"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/flamengo-rio-janeiro',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 2
            }


class CruzeiroSpider(scrapy.Spider):
    name = "cec"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/cruzeiro-belo-horizonte',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 3
            }


class InterSpider(scrapy.Spider):
    name = "inter"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/internacional',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 4
            }


class FluminenseSpider(scrapy.Spider):
    name = "flu"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/fluminense-rio-janeiro',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 5
            }


class CorinthiansSpider(scrapy.Spider):
    name = "sccp"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/corinthians-sao-paulo',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 6
            }


class CapSpider(scrapy.Spider):
    name = "cap"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/atletico-paranaense',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 7
            }


class CamSpider(scrapy.Spider):
    name = "cam"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/atletico-mineiro',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 8
            }


class FortalezaSpider(scrapy.Spider):
    name = "fortaleza"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/fortaleza-ec',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 9
            }


class SaoPauloSpider(scrapy.Spider):
    name = "spfc"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/sao-paulo-fc',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 10
            }


class AmericaSpider(scrapy.Spider):
    name = "america"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/america-mineiro',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 11
            }


class BotafogoSpider(scrapy.Spider):
    name = "bfr"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/botafogo-rio-janeiro',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 12
            }


class SantosSpider(scrapy.Spider):
    name = "sfc"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/santos-fc',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 13
            }


class GoiasSpider(scrapy.Spider):
    name = "goias"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/goias-goiania',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 14
            }


class RBSpider(scrapy.Spider):
    name = "rb"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/bragantino',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 15
            }


class CoritibaSpider(scrapy.Spider):
    name = "coxa"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/coritiba-fbc',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 16
            }


class CuiabaSpider(scrapy.Spider):
    name = "cuiaba"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/cuiaba',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 17
            }


class GremioSpider(scrapy.Spider):
    name = "gremio"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/gremio-porto-alegre',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 18
            }


class VascoSpider(scrapy.Spider):
    name = "vasco"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/vasco-da-gama',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 19
            }


class BahiaSpider(scrapy.Spider):
    name = "bahia"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/ec-bahia',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 20
            }


if __name__ == '__main__':
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(PalmeirasSpider)
    process.crawl(FlamengoSpider)
    process.crawl(CruzeiroSpider)
    process.crawl(InterSpider)
    process.crawl(FluminenseSpider)

    process.crawl(CorinthiansSpider)
    process.crawl(CapSpider)
    process.crawl(CamSpider)
    process.crawl(FortalezaSpider)
    process.crawl(SaoPauloSpider)

    process.crawl(AmericaSpider)
    process.crawl(BotafogoSpider)
    process.crawl(SantosSpider)
    process.crawl(GoiasSpider)
    process.crawl(RBSpider)

    process.crawl(CoritibaSpider)
    process.crawl(CuiabaSpider)
    process.crawl(GremioSpider)
    process.crawl(VascoSpider)
    process.crawl(BahiaSpider)

    process.start()
