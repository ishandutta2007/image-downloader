#coding=utf-8

import requests,os,csv,codecs

proxy = {"http":"localhost:10110"}
ua_string = {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}

def do_filter():
    file_list = []
    for dirpath, dnames, fnames in os.walk("C://Users//wu//Downloads//links"):
        for f in fnames:
            if f.endswith(".csv"):
                csv_file = os.path.join(dirpath, f)
                file_list.append(csv_file)

    url_list  = []
    for f in file_list:
        print f
        with open(f, 'r') as csvFile:
            reader = csv.reader((line.replace('\0','') for line in csvFile))
            for row in reader[:20000]:
                content =  row[2]
                if content.find("http") != -1:
                    url_list.append(content.strip())
                    print content.strip()

        csvFile.close()
    print len(url_list)
    clean_url = []
    for url in url_list:
        resp = requests.get(url,proxies=proxy,headers=ua_string)
        content = resp.content
        if content.find("comment") != -1 or content.find("review") !=-1:
            clean_url.append(url)

    print clean_url
    with open("clean_url.txt",'a') as f:
        for url in clean_url:
            f.write(url+"\n")


if __name__ == "__main__":
    do_filter()