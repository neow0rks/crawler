import scrapy
import json
import os


class Crawler(scrapy.Spider):
    page = 2
    name = "crawler"
    base = "https://www.vieclamtot.com"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    list_data = []
    file_out = None
    file_in = None

    def __init__(self, file_in = None, file_out = None, **kwargs):
        print("Crawler init")
        if file_in is None or file_out is None:
            raise ValueError("File is None")
        else:
            urls = []
            self.file_in = file_in
            self.file_out = file_out
            with open(file_in, 'r') as f:
                for line in f.readlines():
                    urls.append(self.base + line.strip())
                    # if (len(urls) == 2):
                    #     break
            self.start_urls = urls
            # print("=====================")
            # print(file_in)
        super().__init__(file_in, **kwargs)

    def parse(self, response):
        print("Crawler parse", response.url, response.status)
        if response.status != 200:
            print("============================")
            print("ERROR")
            self.start_urls.remove(response.url)
                    
    def closed(self, reason):
        print("Crawler done")
        print(len(self.start_urls))
        # create folder
        # get folder name
        # folder_name = self.file_out.split("/")[0] + "/" + self.file_out.split("/")[1] + "/" + self.file_out.split("/")[2]
        # if not os.path.exists(folder_name):
        #     os.mkdir(folder_name)            
        # f = open(self.file_out, "wb")
        # # start json
        # f.write("{\n".encode("utf-8"))
        # # write data
        # # write total
        # f.write("\t\"total\": ".encode("utf-8"))
        # f.write(str(len(self.list_data)).encode("utf-8"))
        # f.write(",\n".encode("utf-8"))
        # # write data
        # f.write("\t\"data\": [\n".encode("utf-8"))
        # for i in range(len(self.list_data)):
        #     f.write("\t\t".encode("utf-8"))
        #     f.write(self.list_data[i].encode("utf-8"))
        #     if (i != len(self.list_data) - 1):
        #         f.write(",\n".encode("utf-8"))
        #     else:
        #         f.write("\n".encode("utf-8"))
        # f.write("\t]\n".encode("utf-8"))
        # # end json
        # f.write("}".encode("utf-8"))
        # f.close()
        # # move file_in from list_url to crawled
        # # get file name
        # file_name = self.file_in.split("/")[1]
        # # move file
        # os.rename(self.file_in, "crawled/" + file_name)

        
# Path: settings.py

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']

NEWSPIDER_MODULE = 'crawler.spiders'

ROBOTSTXT_OBEY = True

# Path: items.py
