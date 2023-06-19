# this program is used to crawl images from the web
# url is the url of the post

import os
import requests
import json
import sys

if __name__ == "__main__":
    print("Crawling images from posts")
    # args = sys.argv
    # district = args[1].split("=")[1]

    waiting_list = [
        # "quan-1",
        # "quan-2",
        # "quan-3",
        # "quan-4",
        # "quan-5",
        # "quan-6",
        # "quan-7",
        # "quan-8",
        # "quan-9",
        # "quan-10",
        # "quan-11",
        # "quan-12",
        # "quan-binh-tan",
        # "quan-binh-thanh",
        # "quan-go-vap",
        # "quan-phu-nhuan",
        # "quan-tan-binh",
        # "quan-tan-phu",
        # "thanh-pho-thu-duc",
        "hoc-moon"
    ]

    # get data from json file
    for district in waiting_list:
        print("Crawling images from " + district + " district")
        f = open("data/tp_hcm/" + district + "/data.json", "r")
        data = json.load(f)
        f.close()

        
        posts = data["data"]

        # create folder
        if not os.path.exists("data/tp_hcm/" + district + "/images"):
            os.mkdir("data/tp_hcm/" + district + "/images")

        for post in posts:
            # get images
            if "images" in post:
                images = post["images"]
                # mkdir for post
                if not os.path.exists("data/tp_hcm/" + district + "/images/" + str(post["ad_id"])):
                    os.mkdir("data/tp_hcm/" + district + "/images/" + str(post["ad_id"]))
                for image in images:
                    # get url
                    # get file name
                    file_name = image.split("/")[len(image.split("/")) - 1]
                    # download image
                    r = requests.get(image)
                    
                    # write image
                    f = open("data/tp_hcm/" + district + "/images/" + str(post["ad_id"]) + "/" + file_name, "wb")
                    f.write(r.content)
                    f.close()
                    print("Downloaded " + file_name)

