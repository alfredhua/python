import scrapy
from ..items import DouBanBook

class douban_book(scrapy.Spider):

    name = 'douban'
    hds={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    
    def start_requests(self):
        url ='https://www.douban.com/tag/%E7%90%86%E8%B4%A2/book?start=0'
        yield scrapy.Request(url=url,headers=self.hds,callback=self.parse)

    def parse(self, response, **kwargs):
        dls=response.css('div.article dl')
        for dl in dls:
            book=DouBanBook()
            book['book_name'] =dl.css('dd a::text').get()
            book['desc'] =dl.css('dd .desc::text').get()
            url= dl.css('dd a::attr(href)').get()
            book['url']=url
            print(dl)
            yield scrapy.Request(url=url,callback=self.parse_detail,headers=self.hds,meta={"book": book})

        start=response.url.split('?')[1]
        current_start=int(start.split('=')[1])
        next_start=(current_start+15)
        if next_start>5000:
            return
        next_url=response.url.replace(start,"start={0}".format(next_start))
        yield scrapy.Request(url=next_url,headers=self.hds,callback=self.parse)

    
    def parse_detail(self,response,**kwargs):
        book = response.meta["book"]
        person_num=response.css('#interest_sectl .rating_sum a span::text').get()
        book['person_num']=person_num
        yield book
