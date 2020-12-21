# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KannadamoviesItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    genre = scrapy.Field()
    rating = scrapy.Field()
    
    
    
    
