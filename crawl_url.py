import scrapy

# Path: crawler.py
# WEB CRAWLER
# url: https://www.vieclamtot.com/viec-lam-cong-nhan-may-sdjt25
def write_to_file(list, file_name):
        with open(file_name, 'w') as f:
            for item in list:
                f.write("%s\n" % item)

def append_to_file(list, file_name):
    with open(file_name, 'a') as f:
        for item in list:
            f.write("%s\n" % item)

class Crawler(scrapy.Spider):
    def __init__(self, district=None, **kwargs):
        if district is None:
            raise ValueError("District is None")
        else:
            self.base = "https://www.vieclamtot.com/viec-lam-" + str(district) + "-tp-ho-chi-minh?page="
            self.start_urls = [self.base + "1"]
            self.district = district
        super().__init__(district, **kwargs)

    page = 2
    district = None
    name = "crawler"
    base = None
    start_urls = []
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

    def parse(self, response):
        print("Crawling: ", response.url, "...")
        if response.status == 200:
            if response.css('.AdItem_wrapperAdItem__S6qPH') == []:
                print("No data ================")
                return

            for link in response.css('.AdItem_wrapperAdItem__S6qPH'):
                href = link.css('a::attr(href)').extract_first()
                append_to_file([href], 'list_url/list_url_job_' + self.district + '.txt')

            print("Processing next page...", self.page)
            #next page
            next_page_url = self.base + str(self.page)
            self.page += 1
            yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            print("Crawling will be stopped ================")

                   

        
# Path: settings.py

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']

NEWSPIDER_MODULE = 'crawler.spiders'

ROBOTSTXT_OBEY = True

# Path: items.py
