# -*- coding: utf-8 -*-

# requirements
import re, json
import requests
from bs4 import BeautifulSoup
import time,os
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

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


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

    popular =   user_dict.get('popular')  
    if popular == False:
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
            
    else:
        print "run popular"
        category_name = user_dict.get("category_name")
        url = 'https://api.500px.com/v1/photos?rpp=50&feature=popular&image_size%5B%5D=1&image_size%5B%5D=2' \
                    '&image_size%5B%5D=32&image_size%5B%5D=31&image_size%5B%5D=33&image_size%5B%5D=34&image_size%5B%5D=35' \
                    '&image_size%5B%5D=36&image_size%5B%5D=2048&image_size%5B%5D=4&image_size%5B%5D=14&sort=' \
                    '&include_states=true&include_licensing=false&formats=jpeg%2Clytro&only='+category_name+'&rpp=50&page='
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
    category_id_list = user_dict.get("category")
    username = user_dict.get('username')
    tag = user_dict.get("tag")    
    for round in xrange(5):
        r_post = rq.get(url+str(round+1), headers=header)
        print url+str(round+1)
        print r_post
        for p in r_post.json()['photos'][:10]:
            id = p['id']
            name = p['name'].encode('utf-8','ignore')
            description = p['description'].encode('utf-8','ignore') if p['description'] else ""
            category = p['category']
            photo_url = p["url"]
            
            if not p['watermark']:
                try:
                    f1 =open("D:/500px/%s.txt" % username,"a")
                    f1.write("%s--%s--%s--%s--%s--%s\n" % (p['favorites_count'] ,p['highest_rating'] ,p["url"],p['category'],name,description))
                    f1.close()
                except Exception,e:
                    print "%s--%s--%s--%s\n" % (p['favorites_count'] ,p['highest_rating'] ,p["url"],p['category'])
                    print e
            print username,popular,p['watermark'], p['highest_rating'] < 92
            if username not in zero_fav_enable:
                if not popular and (p['watermark'] or ( p['favorites_count'] < 80 and  p['highest_rating'] < 92 )):
                    continue
            elif   username in         zero_fav_enable:
                if not popular and (p['watermark'] or (0< p['favorites_count'] < 80 and  p['highest_rating'] < 92 )):
                    continue
            if popular and p['rating'] < 85:
                continue
            

            if name.find('@') != -1 or name.find('http://') != -1 or name.find('https://') != -1:
                continue

            if len(description) > 250:
                continue
            if description.find('@') != -1 or description.find('http://') != -1 or description.find('https://') != -1 or description.find('www'):
                description = ""
            if category not in category_id_list:
                continue
            if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': id,'username':username}):
                
                for i in p['images']:
                    if i['size']==2048:
                        try:
                            filepath = 'D:/500px/%s' % username
                            filename = 'D:/500px/%s/%s.jpg' % (username,str(id))
                            if not os.path.exists(filepath):
                                os.mkdir(filepath)
                                
                            urllib.urlretrieve(i['url'],filename)
                            txt_path = "D:/500px/%s/500txt" % username
                            if not os.path.exists(txt_path):
                                os.mkdir(txt_path)
                            f = open('D:/500px/%s/500txt/%s.txt' % (username,str(id)),'w')
                            f.writelines([filename+"\n",'.'.join([name.strip(),description.strip(),tag])])
                            f.close()
                            
                        except Exception,e:
                            print e
                            break
                        item = { '_id':id, 'name':name, 'url':photo_url, 'username':username,'description' :description}
                        MONGO[MONGO_DB][MONGO_USER_COLL].insert_one(item)
                        time.sleep(3)
                        
            else:
                print str(id)+' dulplicate!'



if __name__ == '__main__':
    dog_tag = "#dog #dogsofinstagram #dogs #puppy #love #instadog #dogstagram #cute #pet #animal #puppiesofinstagram #doggy #doglover #bully #frenchbulldog #westie #hund #doglovers #pets #like #cutedog #frenchie #instagram #puppylove #chien #of #instagood #doggo #like4like #follow4follow"
    yoga_tag="#yoga #love #fitness #yogainspiration #yogaeverydamnday #health #yogi #yogalife #yogachallenge #namaste #spiritual #meditation #yogalove #yogateacher #happiness #yogaeverywhere #nature #happy #gym #inspiration #healthy #motivation #goodvibes #yogajourney #like4like #follow4follow"
    wedding_tag = "#wedding #love #weddingdress #matrimonio #bride #weddingphotography #weddingday #weddingplanner #sposa #fashion #weddinginspiration #weddingphotographer #bomboniere #hairstyle #clothing #party #groom #weddingideas #bombonierematrimonio #bombonierelaurea #wedding #love #weddingdress #matrimonio #bride #weddingphotography #weddingday #sposi #nozze #weddingplanner #photography #like4like #fashion #bodas #weddinginspiration #boda #weddingphotographer #bomboniere #hairstyle #clothing #party #groom #bombonierebattesimo #battesimo #napoli #weddingideas #bombonierematrimonio #bombonierelaurea #like4like #follow4follow"
    healthy_tag = "#healthyfood #healthylifestyle #healthy #foodporn #food #foodie #instafood #health #vegan #fitness #yummy #diet #breakfast #veganfood #healthyeating #nutrition #foodphotography #healthyrecipes #smoothie #love #lunch #cleaneating #delicious #instagood #healthandfitness #livehealthy #foodpic #fitgirl #dinner #follow4follow"
    car_tag ="#sportcar #car #cars #bmw #supercar #instacar #porsche #carporn #supercars #luxury #audi #lamborghini #ferrari #speed #luxurycars #mercedes #racecar #auto #hypercar #carspotting #fastcar #carsofinstagram #sportcars #automotive #luxurycar #instacars #race #like #follow4follow"

    
    travel_tag ="#travel #photography #love #nature #photooftheday #instatravel #travelgram #travelphotography #instagood #travelling #trip #travelblogger #wanderlust #picoftheday #photo #sky #france #holiday #voyage #europe #like #art #follow #italy #vacation #sun #instagram #instapic #traveler #follow4follow"
    
    username_dog = {"username":"kate_dog23","popular":False,"category":[11],"keyword":["cute+dog","dogs","doggy","doglover"],"tag":dog_tag}
    username_yoga = {"username":"amy_yoga23","popular":False,"category":[17,7,19],"keyword":["yoga","yogalife"],"tag":yoga_tag}
    username_wedding = {"username":"amber_wedding23","popular":True,"category":[25],"category_name":"Wedding","tag":wedding_tag}
    username_healthy = {"username":"ada_healthy","popular":False,"category":[23],"keyword":["healthy+diet"],"tag":healthy_tag}
    username_car = {"username":"lily_car23","popular":False,"category":[26,21],"keyword":["sport+car","race","drive","supercar"],"tag":car_tag}

    username_travel = {"username":"jany_travel","popular":True,"category":[13],"keyword":["travel"],"tag":travel_tag,"category_name":"travel"}

    username_list = [username_dog,username_yoga,username_wedding,username_healthy,username_car]
    
    #for user_dict in [username_dog,username_healthy,username_car]:
    for user_dict in [username_travel]:
        download_photos(user_dict)


