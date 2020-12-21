import scrapy
from ..items import KannadamoviesItem


class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    start_urls = ['https://www.imdb.com/search/title/?title_type=feature&primary_language=kn&start=1&ref_=adv_prv']
    page_number = 2
    def parse(self, response):
        
        items = KannadamoviesItem()
        
        
        
        movie_name = response.css('.lister-item-header a::text').extract()
        genre = response.css('.genre::text').extract()
        rating = response.css('.ratings-imdb-rating strong::text').extract()
        
        
       
        
        for movies in zip(movie_name,genre,rating):
           
            
           items['movie_name'] = movies[0].strip()
           items['genre'] = movies[1].strip()
           items['rating'] = movies[2].strip()
            
           
           yield items

        next_page = 'https://www.imdb.com/search/title/?title_type=feature&primary_language=kn&start='+str(ImdbSpiderSpider.page_number)+'&ref_=adv_nxt'
        
        if ImdbSpiderSpider.page_number <= 100:
            ImdbSpiderSpider.page_number += 1
            yield response.follow(next_page,callback = self.parse)