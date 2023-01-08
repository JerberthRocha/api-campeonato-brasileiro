# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class RaspaDadosPipeline:
    def __init__(self):
        #Cria/Conecta ao DB
        self.conexao = sqlite3.connect('db.sqlite3')

        #Cria o cursor usado para executar comandos no DB
        self.cursor = self.conexao.cursor()

    #CLUBES SERIE A E B
    def process_item(self, item, spider):
        self.cursor.execute("""
            INSERT INTO jogadores_time (nome, divisao_id) VALUES (?, ?)
        """,
        (
            item['nome'],
            item['divisao_id']
        ))

        ## Execute o comando de inserção no DB
        self.conexao.commit()
        return item
