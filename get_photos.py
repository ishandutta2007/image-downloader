# -*- coding: utf-8 -*-

# requirements
import re, json
import requests
from bs4 import BeautifulSoup
import time
import urllib
import cPickle
from pymongo import MongoClient


MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = '500px'
MONGO_USER_COLL = 'photos'
MONGO = MongoClient(MONGO_HOST, MONGO_PORT)


headers = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"
}
rq = requests.Session()
rq.headers = headers

def _get_popular_token():
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    rq = requests.Session()
    rq.headers = headers
    url = "https://500px.com/popular"
    r = rq.get(url, allow_redirects=False)
    status_code = int(r.status_code)
    if status_code != 200:
        print "ERROR!"
        return
    
    soup = BeautifulSoup(r.content, "html.parser")
    csrf_token = soup.find("meta", attrs={'name': 'csrf-token'})["content"]
    return csrf_token

def _get_search_token():
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    rq = requests.Session()
    rq.headers = headers
    url = "https://api.500px.com/v1/messenger/token"
    r = rq.get(url, allow_redirects=False)
    status_code = int(r.status_code)
    if status_code != 200:
        print "ERROR!"
        return
    
    soup = BeautifulSoup(r.content, "html.parser")
    csrf_token = soup.find("meta", attrs={'name': 'csrf-token'})["content"]
    return csrf_token    

def download_photos(user_dict):
    # check session
    print "begin"

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    rq = requests.Session()
    rq.headers = headers
    url = "https://500px.com/popular"
    r = rq.get(url, allow_redirects=False)
    status_code = int(r.status_code)
    if status_code != 200:
        print "ERROR!"
        return
    
    soup = BeautifulSoup(r.content, "html.parser")
    csrf_token = soup.find("meta", attrs={'name': 'csrf-token'})["content"]
        
    if user_dict.get('popular') == False:
        print "run search"
        keyword_list = user_dict.get("keyword")
        for keyword in keyword_list:
            url = "https://api.500px.com/v1/photos/search?type=photos&term="+keyword+"&image_size%5B%5D=1"   \
                "&image_size%5B%5D=2&image_size%5B%5D=32&image_size%5B%5D=31&image_size%5B%5D=33"   \
                "&image_size%5B%5D=34&image_size%5B%5D=35&image_size%5B%5D=36"                      \
                "&image_size%5B%5D=2048&image_size%5B%5D=4&image_size%5B%5D=14&include_states=true" \
                "&formats=jpeg%2Clytro&include_tags=true&exclude_nude=true&rpp=50&page=" 
            csrf_word = 'X-CSRF-Token'
            csrf = csrf_token
            host = 'api.500px.com'
            
    if False:
        print "run popular"
        category_name = user_dict.get("category_name")
        category_name = "wedding"
        url = 'https://api.500px.com/v1/photos?rpp=50&feature=popular&image_size%5B%5D=1&image_size%5B%5D=2' \
                    '&image_size%5B%5D=32&image_size%5B%5D=31&image_size%5B%5D=33&image_size%5B%5D=34&image_size%5B%5D=35' \
                    '&image_size%5B%5D=36&image_size%5B%5D=2048&image_size%5B%5D=4&image_size%5B%5D=14&sort=' \
                    '&include_states=true&include_licensing=false&formats=jpeg%2Clytro&only='+category_name+'&rpp=50&page='
        csrf_word = 'X-CSRF-Token'
        csrf = csrf_token
        print csrf_word,csrf_token
        host = 'api.500px.com'
      
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        'Host': host,
        'Origin':"https://500px.com",
        'Referer': "https://api.500px.com",
        csrf_word:csrf
    }
    print header   

        
    category_id_list = user_dict.get("category")
    username = user_dict.get('username')
        
    for round in xrange(50):
        r_post = rq.get(url+str(round+1), headers=header)
        print r_post
        for p in r_post.json()['photos']:
            id = p['id']
                
            if p['watermark'] or p['favorites_count'] < 85 or p['highest_rating'] < 90 :
                continue
            name = p['name'].encode('utf-8','ignore')
            description = p['description'].encode('utf-8','ignore')
            category = p['category']
            photo_url = p["url"]
            if name.find('@') != -1 or name.find('http://') != -1 or name.find('https://') != -1:
                continue

            if description.find('@') != -1 or description.find('http://') != -1 or description.find('https://') != -1:
                continue
            if category not in category_id_list:
                continue
            if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': id,'username':username}):
                
                for i in p['images']:
                    if i['size']==2048:
                        print "---"
                        print i['url']
                        try:
                            filename = 'D:/500px/'+str(id)+'.jpg'
                            urllib.urlretrieve(i['url'],filename)
                            f = open('D:/500px/500px_name/'+str(id)+'.txt','a+')
                            f.writelines([filename+"\n",'.'.join([name,description])+'\n',photo_url])
                            f.close()
                        except Exception,e:
                            print e
                            break
                        item = { '_id':id, 'name':name, 'url':photo_url, 'username':username,'description' :description}
                        MONGO[MONGO_DB][MONGO_USER_COLL].insert_one(item)
                        time.sleep(5)
            else:
                print str(id)+' dulplicate!'



if __name__ == '__main__':
    while True:
        username_dog = {"username":"kate_dog23","popular":False,"category":[11],"keyword":["cute+dog"]}
        username_yoga = {"username":"amy_yoga23","popular":False,"category":[17,7],"keyword":["yoga"]}
        username_wedding = {"username":"amber_wedding23","popular":True,"category":[25],"category_name":"Wedding"}
        username_healthy = {"username":"ada_healthy","popular":False,"category":[23],"keyword":["healthy+diet"]}
        username_car = {"username":"lily_car23","popular":False,"category":[26,21],"keyword":["sport car"]}
        username_list = [username_dog,username_yoga,username_wedding,username_healthy,username_car]
        
        for user_dict in [username_dog]:
            download_photos(user_dict)
            print "Sleeping..."
            time.sleep(86400)

