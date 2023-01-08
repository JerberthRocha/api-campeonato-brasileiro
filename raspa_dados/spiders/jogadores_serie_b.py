import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class AtlGoianienseSpider(scrapy.Spider):
    name = "dragao"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/atletico-go',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 21
            }


class MirassolSpider(scrapy.Spider):
    name = "mirassol"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/mirassol',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 22
            }


class AbcSpider(scrapy.Spider):
    name = "abc"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/abc',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 23
            }


class BotafogoSPSpider(scrapy.Spider):
    name = "botasp"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/botafogo-sp',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 24
            }


class VitoriaSpider(scrapy.Spider):
    name = "vit"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/vitoria',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 25
            }


class CearaSpider(scrapy.Spider):
    name = "ceara"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/ceara',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 26
            }


class AvaiSpider(scrapy.Spider):
    name = "avai"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/avai',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 27
            }


class JuventudeSpider(scrapy.Spider):
    name = "juve"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/juventude-caxias-do-sul',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 28
            }



class ChapecoenseSpider(scrapy.Spider):
    name = "chape"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/chapecoense',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 29
            }


class CRBSpider(scrapy.Spider):
    name = "crb"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/crb',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 30
            }


class CriciumaSpider(scrapy.Spider):
    name = "criciuma"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/criciuma-ec',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 31
            }


class GuaraniSpider(scrapy.Spider):
    name = "guarani"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/guarani-campinas',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 32
            }


class ItuanoSpider(scrapy.Spider):
    name = "ituano"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/ituano',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 33
            }


class LondrinaSpider(scrapy.Spider):
    name = "londrina"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/londrina',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 34
            }


class NovorizontinoSpider(scrapy.Spider):
    name = "novorizontino"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/novorizontino',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 35
            }


class PontePretaSpider(scrapy.Spider):
    name = "ponte"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/ponte-preta',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 36
            }


class SampaioSpider(scrapy.Spider):
    name = "sampaio"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/sampaio-correa-fc',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 37
            }


class SportSpider(scrapy.Spider):
    name = "sport"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/sport-recife',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 38
            }


class TombenseSpider(scrapy.Spider):
    name = "tombense"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/tombense',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 39
            }


class VilaNovaSpider(scrapy.Spider):
    name = "vila"

    start_urls = [
        'https://pt.besoccer.com/time/elenco/vila-nova',
    ]

    def parse(self, response):
        nome = response.xpath("*//td[@class='name']/a/text()").getall()
        foto = response.xpath("*//td[@class='player-img']/a/div/img").getall()
        for i in range(len(nome)):
            yield {
                'nome': nome[i],
                'foto': foto[i][25:85],
                'time_id': 40
            }


if __name__ == '__main__':
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(AtlGoianienseSpider)
    process.crawl(MirassolSpider)
    process.crawl(AbcSpider)
    process.crawl(BotafogoSPSpider)
    process.crawl(VitoriaSpider)

    process.crawl(CearaSpider)
    process.crawl(JuventudeSpider)
    process.crawl(AvaiSpider)
    process.crawl(ChapecoenseSpider)
    process.crawl(CRBSpider)

    process.crawl(CriciumaSpider)
    process.crawl(GuaraniSpider)
    process.crawl(ItuanoSpider)
    process.crawl(LondrinaSpider)
    process.crawl(NovorizontinoSpider)
    
    process.crawl(PontePretaSpider)
    process.crawl(SampaioSpider)
    process.crawl(SportSpider)
    process.crawl(TombenseSpider)
    process.crawl(VilaNovaSpider)

    process.start()
