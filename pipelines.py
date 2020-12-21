# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import sqlite3


class KannadamoviesPipeline:
    
    def __init__(self):
        self.create_connection()
        self.create_table()
        pass
    
    def create_connection(self):
        self.conn = sqlite3.connect("movies.db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS movies_tb""")
        self.curr.execute("""create table movies_tb(
                        movie_name text,
                        genre text,
                        rating text
                        )""")
        
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""insert into movies_tb values (?,?,?)""",(
            item['movie_name'],
            item['genre'],
            item['rating']
            ))
        self.conn.commit()