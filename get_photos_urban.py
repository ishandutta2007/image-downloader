# -*- coding: utf-8 -*-

# requirements
import re, json
import requests
from bs4 import BeautifulSoup
import time,os
import urllib,pymongo

from pymongo import MongoClient
from datetime import datetime
from hashtag import get_hashtag
from multiprocessing import freeze_support,Pool
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = '500px'
MONGO_USER_COLL = 'photos'
MONGO = MongoClient(MONGO_HOST, MONGO_PORT)

proxies = {
    "http": "127.0.0.1:10000",
    "http": "127.0.0.1:10001",
    "http": "127.0.0.1:10002",
    "http": "127.0.0.1:10003",
    "http": "127.0.0.1:10004",
    "http": "127.0.0.1:10005",
    "http": "127.0.0.1:10006"

}
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"
}
rq = requests.Session()
rq.headers = headers

import sys,time  

reload(sys)  
sys.setdefaultencoding('utf8')


def change_md5(file_path,username,id):
    file = open(file_path, 'rb').read()
    filepath = 'F:/500px3/%s' % username
    filename = 'F:/500px3/%s/%s.jpg' % (username, str(id))

    if not os.path.exists(filepath):
        os.makedirs(filepath)
    with open(filename, 'wb') as new_file:
        new_file.write(file+'\0')  #here we are adding a null to change the file content
    return new_file.name

def download_photos(user_dict):
    # check session
    print "begin"

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    rq = requests.Session()
    rq.headers = headers
    url = "https://500px.com/popular"
    r = rq.get(url, allow_redirects=False, proxies=proxies)
    status_code = int(r.status_code)
    if status_code != 200:
        print "ERROR!"
        return

    soup = BeautifulSoup(r.content, "html.parser")
    csrf_token = soup.find("meta", attrs={'name': 'csrf-token'})["content"]

    popular =   user_dict.get('popular')
    if not popular:
        keyword = user_dict.get("keyword")
    else:
        keyword = user_dict.get("category_name")
    if popular == False:
        print "run search"
        url = "https://api.500px.com/v1/photos/search?type=photos&term="+keyword+"&image_size%5B%5D=1&image_size%5B%5D=2&image_size%5B%5D=32&image_size%5B%5D=31&image_size%5B%5D=33&image_size%5B%5D=34&image_size%5B%5D=35&image_size%5B%5D=36&image_size%5B%5D=2048&image_size%5B%5D=4&image_size%5B%5D=14&include_states=true&formats=jpeg%2Clytro&include_tags=true&exclude_nude=true&rpp=50&page="
        csrf_word = 'X-CSRF-Token'
        csrf = csrf_token
        host = 'api.500px.com'

    else:
        print "run popular"
        category_name = user_dict.get("category_name")
        url = 'https://api.500px.com/v1/photos?rpp=50&feature=editors&image_size%5B%5D=1&image_size%5B%5D=2&image_size%5B%5D=32&image_size%5B%5D=31&image_size%5B%5D=33&image_size%5B%5D=34&image_size%5B%5D=35&image_size%5B%5D=36&image_size%5B%5D=2048&image_size%5B%5D=45B%5D=14&sort=&include_states=true&include_licensing=true&formats=jpeg%2Clytro&only='+category_name+'&exclude=&personalized_categories=&rpp=50&page='

        csrf_word = 'X-CSRF-Token'
        csrf = csrf_token
        host = 'api.500px.com'

    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        'Host': host,
        'Origin':"https://500px.com",
        'Referer': "https://api.500px.com",
        csrf_word:csrf
    }

    zero_fav_enable= ['amy_yoga23',]
    category_id_list = user_dict.get("category",[])
    username = user_dict.get('username')
    print 'zzzzzzzzzzzzzzzzz'

    for round in xrange(1,2):
        try:
            r_post = rq.get(url+str(round+1), headers=header, proxies=proxies)

        except Exception,e:
            print e
            time.sleep(10)
            continue

        print url+str(round+1)

        for p in r_post.json()['photos']:
            print 'request images'
            id = p['id']
            name = p['name'].encode('utf-8','ignore')
            description = p['description'].encode('utf-8','ignore') if p['description'] else ""
            category = p['category']
            photo_url = p["url"]

            if  p['watermark']:
                continue
            print username,popular,p['watermark'], p['highest_rating'] ,  p['url'],p['rating']
            if username not in zero_fav_enable:
                if not popular and (p['watermark'] or ( p['favorites_count'] < 85 and  p['highest_rating'] < 92 )):
                    continue
            elif   username in zero_fav_enable:
                if not popular and (p['watermark'] or (0< p['favorites_count'] < 85 and  p['highest_rating'] < 92 )):
                    continue

            if popular and (username not in ["ann_nature23"] and  p['rating'] < 80):
                continue

            if name.find('@') != -1 or name.find('http://') != -1 or name.find('https://') != -1 or name.find('www') != -1:
                continue
            if len(description) > 500:
                continue
            if description.find('@') != -1 or description.find('http://') != -1 or description.find('https://') != -1 or description.find('www') !=-1 or description.lower().find('sale') !=-1:
                description = ""
            if category_id_list and category_id_list[0] != ''  and str(category) not in category_id_list:
                continue
            if (name+ description).lower().startswith("Untitled") :
                continue
            if not check_tags(photo_url, id, host):
                continue
            if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': id}):
                print ' download image'
                for i in p['images']:
                    if i['size']==2048:
                        try:
                            txt_path = "F:/500px3/%s" % username
                            if not os.path.exists(txt_path):
                                os.makedirs(txt_path)
                            keyword1 = keyword.split("+")[0]
                            tag = get_hashtag(keyword1)

                            print '.'.join([name.strip(), description.strip(), tag])
                            f1 = open('F:/500px3/%s/%s.txt' % (username, str(id)), 'w')
                            f1.writelines(['.'.join([name.strip(), description.strip(), tag.strip()])])
                            f1.close()

                            filepath = 'F:/500px3/tmp/%s' % username
                            filename = 'F:/500px3/tmp/%s/%s.jpg' % (username,str(id))
                            if not os.path.exists(filepath):
                                os.makedirs(filepath)
                            urllib.urlretrieve(i['url'], filename)
                            change_md5(filename,username,str(id))


                        except Exception,e:
                            import traceback
                            traceback.print_exc()
                            continue

                        item = { '_id':id, 'name':name, 'url':photo_url, 'username':username,'description' :description,"time":datetime.now()}
                        #try:
                        #    MONGO[MONGO_DB][MONGO_USER_COLL].insert_one(item)
                        #except pymongo.errors.DuplicateKeyError,e:
                        #    print e
                        time.sleep(3)
                        
            else:
                print str(id)+' dulplicate!'




def check_tags(url,id,host):
    print 'begin check tags'

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    rq = requests.Session()
    rq.headers = headers
    r = rq.get( "https://500px.com"+url, allow_redirects=False, proxies=proxies)
    status_code = int(r.status_code)
    if status_code != 200:
        print "ERROR!"
        return

    soup = BeautifulSoup(r.content, "html.parser")
    csrf_token = soup.find("meta", attrs={'name': 'csrf-token'})["content"]

    csrf_word = 'X-CSRF-Token'
    host = 'api.500px.com'

    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        'Host': host,
        'Origin':"https://500px.com",
        'Referer': "https://500px.com"+url,
        csrf_word:csrf_token
    }
    detail_url = "https://api.500px.com/v1/photos?image_size%5B%5D=1&image_size%5B%5D=2&image_size%5B%5D=32&image_size%5B%5D=31&image_size%5B%5D=33&image_size%5B%5D=34&image_size%5B%5D=35&image_size%5B%5D=36&image_size%5B%5D=2048&image_size%5B%5D=4&image_size%5B%5D=14&expanded_user_info=true&include_tags=true&include_geo=true&include_equipment_info=true&vendor_photos=true&include_licensing=true&include_releases=true&liked_by=1&following_sample=100&ids="+str(id)
    r_post = rq.get(detail_url, headers=header, proxies=proxies)

    photos =  r_post.json()['photos']
    tags = photos[str(id)]['tags']
    print tags
    if 'topless' in tags:
        return False
    return True

if __name__ == '__main__':
    f = open("F:/instagram/niches/niches_new2.csv","r")
    lines = f.readlines()
    user_list = []
    for line in lines[:]:
        if not line.strip():
            continue

        user_dict = {}
        str_list = line.split(",")

        username = str_list[0]
        popular = True if str_list[1] =="TRUE" else False
        category = str_list[2].split('_')

        keyword = str_list[3].replace('"',"")
        hashtag = str_list[5]
        category_name = str_list[4]
        user_dict.update({"username":username,"popular":popular,"category":category,"keyword":keyword,"tag":hashtag,"category_name":category_name})
        user_list.append(user_dict)

    #for user_dict in [username_dog,username_healthy,username_car]:
    pool = Pool(1)
    for user_dict in user_list:

        username = user_dict.get("username")
        user_list = ["diann_look"]
        print username
        if username in user_list:
            pool.apply_async(func=download_photos,args=(user_dict,))

    pool.close()
    pool.join()


