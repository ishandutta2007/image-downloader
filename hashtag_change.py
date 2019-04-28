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
    top = random.sample(l, 13)
    return top

def get_hashtag(keyword):
    data.update({"keyword":keyword,"filter":"random"})
    resp = requests.post(url, data=data, headers=headers,verify=False)
    soup = BeautifulSoup(resp.content, 'html.parser')
    tag = soup.find("div", {"id": "copy-hashtags"})
    print tag,tag.text
    l = tag.text.split("#")
    l= [tmp.strip()+" " for tmp in l if tmp.strip() != ""]
    rad = random.sample(l,1)
    top = get_toptag(keyword)
    print rad
    print top
    print  '========'
    s = "#"+"#".join(list(set((rad+top))))
    value = random.randint(1, 2)
    if value == 1:
        s+=" #newyork #chicago #losangeles #ootdshare #ootd"
    else:
        s += " #newyork #paris #ootdshare #ootd"
    return s

if __name__ == "__main__":
    f = open("F://instagram//niches//niches_new21.csv","r")
    lines = f.readlines()
    user_list = []

    from os import walk
    import  os

    for line in lines[5:8]:
        if not line:
            continue
        str_list = line.split(",")
        keyword = str_list[3].replace('"', "")

        if not keyword:
            keyword = str_list[4].replace('"', "")
        keyword = keyword.split("+")[0]

        if not keyword:
            continue

        username = str_list[0]
        if username != "emma_accessories23":
            continue
        #
        print "----"
        f = []
        for (dirpath, dirnames, filenames) in walk("F://500px3_2//%s" % username):
            for filename in filenames:
                if filename.endswith('txt'):
                    f.append(os.path.join(dirpath,filename))

        for file  in f:
            #try:
            #    text = get_hashtag(keyword)
            #except:
            #    continue
            content = ''
            text = ''

            with open(file,'r') as tmp_f:
                try:
                    line = tmp_f.readline()
                    print line
                    content = line.split("#")[0]
                    text = line.split("#")[1:-1]
                except:
                    pass

            text1 = " #".join(text) + "#ootdshare #ootd #fashion #clothing #woman"
            print  '==========='
            print content
            print content+text1
            print "----"
            with open(file,'w') as tmp_f:
                try:
                    print  content+text1
                    tmp_f.writelines(content+text1)
                except:
                    pass






