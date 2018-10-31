# -*- coding: utf-8 -*-

# requirements
import re, json
import requests
from bs4 import BeautifulSoup
import time,os
import urllib
import cPickle
from pymongo import MongoClient
from datetime import datetime
from hashtag import get_hashtag

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = '500px'
MONGO_USER_COLL = 'photos'
MONGO = MongoClient(MONGO_HOST, MONGO_PORT)

proxies = {
    "http": "127.0.0.1:8008",
    "http": "127.0.0.1:8009",
    "http": "127.0.0.1:8010",
    "http": "127.0.0.1:8011",
    "http": "127.0.0.1:8012",
    "http": "127.0.0.1:8013",
    "http": "127.0.0.1:8014",
    "http": "127.0.0.1:8015",
    "http": "127.0.0.1:8016",
    "http": "127.0.0.1:8017",
    "http": "127.0.0.1:8018",
    "http": "127.0.0.1:8019",
    "http": "127.0.0.1:8020",
    "http": "127.0.0.1:8021",
    "http": "127.0.0.1:8022",
    "http": "127.0.0.1:8023",
    "http": "127.0.0.1:8024",
    "http": "127.0.0.1:8025",  
    "http": "127.0.0.1:8026",
    "http": "127.0.0.1:8027",
    "http": "127.0.0.1:8028",
    "http": "127.0.0.1:8029",
    "http": "127.0.0.1:8030",
    "http": "127.0.0.1:8031",
    "http": "127.0.0.1:8033",
    "http": "127.0.0.1:8034",
    "http": "127.0.0.1:8035",
    "http": "127.0.0.1:8036",
    "http": "127.0.0.1:8037",
    "http": "127.0.0.1:8038",
    "http": "127.0.0.1:8039",
    "http": "127.0.0.1:8040",
    "http": "127.0.0.1:8041",
    "http": "127.0.0.1:8042",
    "http": "127.0.0.1:8043",
    "http": "127.0.0.1:8045",
    "http": "127.0.0.1:8046",
    "http": "127.0.0.1:8047",
    "http": "127.0.0.1:8047",
    "http": "127.0.0.1:8049"
}
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"
}
rq = requests.Session()
rq.headers = headers

import sys,time  

reload(sys)  
sys.setdefaultencoding('utf8')


def gen_hashtag():

    1

def change_md5(file_path,username,id):
    file = open(file_path, 'rb').read()
    filepath = 'D:/500px/%s' % username
    filename = 'D:/500px/%s/%s.jpg' % (username, str(id))

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
    print keyword
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

    for round in xrange(5):
        try:
            r_post = rq.get(url+str(round+1), headers=header, proxies=proxies)
        except Exception,e:
            print e
            time.sleep(10)
            continue
            
        print url+str(round+1)

        for p in r_post.json()['photos']:
            id = p['id']
            name = p['name'].encode('utf-8','ignore')
            description = p['description'].encode('utf-8','ignore') if p['description'] else ""
            category = p['category']
            photo_url = p["url"]
            
            if not p['watermark']:
                try:
                    f1 =open("D:/500px/%s.txt" % username,"a")
                    f1.write("%s-%s-%s--%s--%s--%s--%s--%s\n" % (popular,p['favorites_count'] ,p['rating'],p['highest_rating'] ,p["url"],p['category'],name,description))
                    f1.close()
                except Exception,e:
                    print "%s--%s--%s--%s\n" % (p['favorites_count'] ,p['highest_rating'] ,p["url"],p['category'])
                    print e
            print username,popular,p['watermark'], p['highest_rating'] ,  p['url']

            if username not in zero_fav_enable:
                if not popular and (p['watermark'] or ( p['favorites_count'] < 80 and  p['highest_rating'] < 92 )):
                    continue
            elif   username in zero_fav_enable:
                if not popular and (p['watermark'] or (0< p['favorites_count'] < 80 and  p['highest_rating'] < 92 )):
                    continue

            print popular,p['rating']
            if popular and (username not in ["ann_nature23"] and  p['rating'] < 50):
                continue

            if name.find('@') != -1 or name.find('http://') != -1 or name.find('https://') != -1 or name.find('www') != -1:
                print '33333'
                continue

            if len(description) > 500:
                continue
            if description.find('@') != -1 or description.find('http://') != -1 or description.find('https://') != -1 or description.find('www') !=-1 or description.lower().find('sale') !=-1:
                description = ""
            if category_id_list and str(category) not in category_id_list:
                continue

            if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': id,'username':username}):
                for i in p['images']:
                    if i['size']==2048:
                        try:
                            filepath = 'D:/500px/tmp/%s' % username
                            filename = 'D:/500px/tmp/%s/%s.jpg' % (username,str(id))
                            if not os.path.exists(filepath):
                                os.makedirs(filepath)
                            urllib.urlretrieve(i['url'], filename)
                            new_file = change_md5(filename,username,str(id))

                            txt_path = "D:/500px/%s/500txt" % username
                            if not os.path.exists(txt_path):
                                os.makedirs(txt_path)
                            keyword = keyword.replace("+", '')
                            tag = get_hashtag(keyword)
                            print tag
                            print new_file+"\n",'.'.join([name.strip(),description.strip(),tag])
                            f = open('D:/500px/%s/500txt/%s.txt' % (username,str(id)),'w')
                            f.writelines([new_file+"\n",'.'.join([name.strip(),description.strip(),tag.strip()])])
                            f.close()
                            
                        except Exception,e:
                            print e
                            import traceback
                            traceback.print_exc()

                            break
                        item = { '_id':id, 'name':name, 'url':photo_url, 'username':username,'description' :description,"time":datetime.now()}
                        MONGO[MONGO_DB][MONGO_USER_COLL].insert_one(item)
                        time.sleep(3)
                        
            else:
                print str(id)+' dulplicate!'



if __name__ == '__main__':
    #dog_tag = "#dog #dogsofinstagram #dogs #puppy #love #instadog #dogstagram #cute #pet #animal #puppiesofinstagram #doggy #doglover #bully #frenchbulldog #westie #hund #doglovers #pets #like #cutedog #frenchie #instagram #puppylove #chien #of #instagood #doggo #like4like #follow4follow"
    #yoga_tag="#yoga #love #fitness #yogainspiration #yogaeverydamnday #health #yogi #yogalife #yogachallenge #namaste #spiritual #meditation #yogalove #yogateacher #happiness #yogaeverywhere #nature #happy #gym #inspiration #healthy #motivation #goodvibes #yogajourney #like4like #follow4follow"
    #wedding_tag = "#wedding #love #weddingdress #matrimonio #bride #weddingphotography #weddingday #weddingplanner #sposa #fashion #weddinginspiration #weddingphotographer #bomboniere #hairstyle #clothing #party #groom #weddingideas #bombonierematrimonio #bombonierelaurea #wedding #love #weddingdress #matrimonio #bride #weddingphotography #weddingday #sposi #nozze #weddingplanner #photography #like4like #fashion #bodas #weddinginspiration #boda #weddingphotographer #bomboniere #hairstyle #clothing #party #groom #bombonierebattesimo #battesimo #napoli #weddingideas #bombonierematrimonio #bombonierelaurea #like4like #follow4follow"
    #healthy_tag = "#healthyfood #healthylifestyle #healthy #foodporn #food #foodie #instafood #health #vegan #fitness #yummy #diet #breakfast #veganfood #healthyeating #nutrition #foodphotography #healthyrecipes #smoothie #love #lunch #cleaneating #delicious #instagood #healthandfitness #livehealthy #foodpic #fitgirl #dinner #follow4follow"
    #car_tag ="#sportcar #car #cars #bmw #supercar #instacar #porsche #carporn #supercars #luxury #audi #lamborghini #ferrari #speed #luxurycars #mercedes #racecar #auto #hypercar #carspotting #fastcar #carsofinstagram #sportcars #automotive #luxurycar #instacars #race #like #follow4follow"

    
    #travel_tag ="#travel #photography #love #nature #photooftheday #instatravel #travelgram #travelphotography #instagood #travelling #trip #travelblogger #wanderlust #picoftheday #photo #sky #france #holiday #voyage #europe #like #art #follow #italy #vacation #sun #instagram #instapic #traveler #follow4follow"
    
    #username_dog = {"username":"kate_dog23","popular":False,"category":[11],"keyword":["dog","dogs"],"tag":dog_tag}
    #username_yoga = {"username":"amy_yoga23","popular":False,"category":[17,7,19],"keyword":["yoga"],"tag":yoga_tag}
    #username_wedding = {"username":"amber_wedding23","popular":True,"category":[25],"category_name":"Wedding","tag":wedding_tag}
    #username_healthy = {"username":"ada_healthy","popular":False,"category":[23],"keyword":["diet"],"tag":healthy_tag}
    #username_car = {"username":"lily_car23","popular":False,"category":[26,21],"keyword":["car"],"tag":car_tag}

    #username_travel = {"username":"jany_travel","popular":True,"category":[13],"keyword":["travel"],"tag":travel_tag,"category_name":"travel"}
    f = open("C://Users/wu/Desktop/instagram/niches/niches_new1.csv","r")
    lines = f.readlines()
    user_list = []
    for line in lines[:40]:
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
    for user_dict in user_list:
        username = user_dict.get("username")
        if username == "andrea_baw23":
            download_photos(user_dict)


