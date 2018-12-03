#coding=utf-8
import requests
from bs4 import BeautifulSoup
import random
import logging
logging.captureWarnings(True)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = "https://www.all-hashtag.com/library/contents/ajax_generator.php"
data = {}

def get_toptag(keyword):
    data.update({"keyword": keyword, "filter": "top"})
    resp = requests.post(url, data=data, headers=headers, verify=False)
    soup = BeautifulSoup(resp.content, 'html.parser')
    tag = soup.find("div", {"id": "copy-hashtags"})

    l = tag.text.split("#")
    l = [tmp.strip()+" " for tmp in l if tmp.strip() != ""]
    top = random.sample(l, 12)
    return top

def get_hashtag(keyword):
    data.update({"keyword":keyword,"filter":"random"})
    resp = requests.post(url, data=data, headers=headers,verify=False)
    soup = BeautifulSoup(resp.content, 'html.parser')
    tag = soup.find("div", {"id": "copy-hashtags"})
    print tag,tag.text
    l = tag.text.split("#")
    l= [tmp.strip()+" " for tmp in l if tmp.strip() != ""]
    rad = random.sample(l,2)
    top = get_toptag(keyword)
    print rad
    print top
    print  '========'
    s = "#"+"#".join(list(set((rad+top))))
    return s

if __name__ == "__main__":
    f = open("C://Users/wu/Desktop/instagram/niches/niches_new1.csv","r")
    lines = f.readlines()
    user_list = []

    from os import walk
    import  os

    for line in lines[89:99]:
        str_list = line.split(",")
        keyword = str_list[3].replace('"', "")
        print  keyword

        username = str_list[0]
        f = []
        for (dirpath, dirnames, filenames) in walk("D:/500px2/%s" % username):
            for filename in filenames:
                if filename.endswith('txt'):
                    f.append(os.path.join(dirpath,filename))

        for file  in f:
            text = get_hashtag(keyword)
            content = ''
            with open(file,'r') as tmp_f:
                line = tmp_f.readline()
                content = line.split("#")[0]
            print  '==========='
            print file
            print  text
            with open(file,'w') as tmp_f:
                try:
                    tmp_f.writelines(content+text)
                except:
                    pass






