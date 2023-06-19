# crawler
Chạy crawler để crawl post url trước:
scrapy runspider crawl_url.py -a district=thanh-pho-thu-duc


#crawl post trong list url
scrapy runspider crawl_posts.py -a file_in=list_url/list_url_job_thanh-pho-thu-duc.txt -a file_out=data/tp_hcm/thanh-pho-thu-duc/data.json

#crawl image
python crawl_img.py
