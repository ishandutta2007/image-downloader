#coding=utf-8
import os,sys,requests
from bs4 import BeautifulSoup
import os
#MySQLdb
import logging

from random import randrange
from datetime import datetime,timedelta

logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='replica0605_2.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################



d1 = datetime.strptime('2017-09-1 1:30', "%Y-%m-%d %H:%M")
d2 = datetime.strptime('2019-06-1 4:50', "%Y-%m-%d %H:%M")

category_list = ['Balenciaga','Bottega Veneta','Burberry','Bvlgari','Céline','Chanel','Chloé','Dior','Fendi','Givenchy','Goyard','Gucci','Hermès','Louis Vuitton','Moschino','Parada','Rimowa','Tory Burch',	'Valentino','YSL']
def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def insert_db(code, image,price,description,tag):
    date_add =   random_date(d1, d2)
    exist_sql = "select product_id from oc_product where model='%s'" % code
    print (exist_sql)
    insert_sql = """insert into oc_product (model,image,price,shipping,stock_status_id,quantity,isbn,sku,date_available,status,date_added,date_modified)
        values ('%s','%s',%f,1,7,20,'%s','%s','%s',1,'%s','%s' ) """ % (code,image[0].encode('utf-8'),price,code,code,date_add,date_add,date_add)
    results = None

    insert_desc_sql = """insert into oc_product_description 
	(product_id,
	language_id,
	name,
	description,
	meta_title,
	tag,
	meta_description,
	meta_keyword,
	seo_keyword,
	seo_h1,
	seo_h2,
	seo_h3,
	image_title,
	image_alt) values (%d,1,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""

    insert_product_store = """insert into oc_product_to_store(product_id,store_id) values (%d,0) """
    insert_product_image = """insert into oc_product_image(product_id,image) values(%d,'%s')"""

    select_tag_sql = 'select category_id from oc_category_description where name="%s"' % tag
    insert_prod_cate = '''insert into oc_product_to_category values(%d,%d)'''

    insert_seo = "insert oc_seo_url(store_id,language_id,query,keyword) values(0,1,'%s','%s')"
    try:
        conn = MySQLdb.connect(host= "localhost",user="opencart",passwd="password", db="replica")
        cur = conn.cursor()
        cur.execute(exist_sql)
        results = cur.fetchone()

        cur.execute(select_tag_sql)
        tag_results = cur.fetchone()
        print (select_tag_sql)
        print (tag_results)
        print ("---------------")
        cur.close()
        conn.close()
        if not results:
            conn = MySQLdb.connect(host= "localhost",user="opencart",passwd="password", db="replica")
            conn.escape_string(insert_desc_sql)
            cur = conn.cursor()
            cur.execute(insert_sql)
            conn.commit()
            product_id = cur.lastrowid

            print (insert_desc_sql % (product_id,code,description,code,code,code,code,code,code,code,code,code,code))
            cur.execute(insert_desc_sql % (product_id,code,description,code,code,code,code,code,code,code,code,code,code))
            conn.commit()
            print ("=====================")
            cur.execute(insert_product_store % product_id)
            conn.commit()
            print ("1111111111111111111")
            for ima in image:
                cur.execute(insert_product_image % (product_id,ima.encode('utf-8')))
                conn.commit()
            print ("22222222222222222222")
            cur.execute(insert_prod_cate % (product_id,tag_results[0]))
            conn.commit()

            cur.execute(insert_seo % ('product_id=%s' % str(product_id),code))
            conn.commit()
            print ("3333333333")
            print (product_id)
            cur.close()
            conn.close()
    except Exception,e:
        logging.error("code %s,error %s" % (code,str(e)))


def category_loop():
    for i in range(1):
        i = i +1
        page = "http://designer-discreet.ru/product-category/replica-bags/page/%s/"
        page = "http://designer-discreet.ru/product-category/celine-replica/page/%s"
        page = "http://designer-discreet.ru/product-category/chloe-replica/page/%s"
        page = "http://designer-discreet.ru/product-category/hermes-replica/page/%s"
        page = "http://designer-discreet.ru/product-category/replica-watches/page/%s"
        page = "http://designer-discreet.ru/product-category/replica-accessories/replica-belts/page/%s"
        page = "http://designer-discreet.ru/product-category/prada-replica/page/%s"
        page = "http://perfectcclub.ru/product-category/chanel/page/%s"
        #page = "http://designer-discreet.ru/product-category/versace-replica/page/%s"
        #page = "http://designer-discreet.ru/product-category/delvaux-replica/"
        resp = requests.get(page % str(i+1))
        content = resp.content
        soup = BeautifulSoup(content,'html.parser')
        products = soup.findAll("li",{"class":"product_item"})
        for product in products:
            text = product.find("a")['href']
            scrape(text)
	
def scrape(url):

    req = requests.get(url)
    content = req.content
    soup = BeautifulSoup(content,'html.parser')
    images = soup.find_all("div",{"class":"woocommerce-product-gallery__image"})

    price = soup.find("span",{"class":"woocommerce-Price-amount"}).text.strip("$")

    desc_tag = soup.find_all( "div",{"class":"tab-content"})[0]
    print (desc_tag.text)
    # desc = None
    # desc_list = []
    # for tag in desc_tag:
    #     print (tag)
    #     desc_list.append(tag)
    #
    # desc = ''.join(desc_list)
    # print (desc)
    # print ("----")

    code = url.split("/")[-2]
    image_url = []
    tags = soup.find("span",{"class":"posted_in"})
    tag_list = []
    category_tag = None
    category_tag = 'Chanel'
   # for tag in tags.find_all("a",href=True):
   #     try:
   #         print (tag.text.strip())
   #     except:
   #         logging.error("tag error %s" % url)
   #         continue
   #     print ("============")
   #     if tag.text.strip() in category_list:
   #         tag_list.append(tag.text)
   #         category_tag = tag.text.strip()
   #         continue
   #
    for image_tmp in images:
        for image in image_tmp.find_all("a",href=True):
            image_url.append(image['href'])
    #if not len(tag_list) :
    #    logging.error("logging tag not exits %s" % url)	
    #    return	
    

   # print (tag_list[0])
    relative_path = []
    for index,image in enumerate(image_url):
        try:
            r = requests.get(requests.Request('GET',image).prepare().url ,stream=True)
        except:
            logging.error("logging tag not exits,%s" % url)
            continue
        if r.status_code == 200:
            path = "catalog/images/bag/%s_%s.jpg" % (code,index)
            full_path = os.path.join("/var/www/html/replica/upload/image", path)
            print (full_path)
            if not os.path.exists(os.path.dirname(full_path)):
                print (os.path.dirname(full_path))
                os.makedirs(os.path.dirname(full_path))
            try:
                with open(full_path, 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                relative_path.append(path)
            except:
                logging.error("error get image,%s" % url)
                continue
    price = price.replace(",","")
    print (price,desc_tag.text,relative_path,code)
    #insert_db(code.encode('utf-8'),relative_path,float(price),desc.encode('utf-8'),category_tag)
if __name__ == "__main__":

    category_loop()	
    #url = "http://designer-discreet.ru/product/louis-vuitton-clunny-bb-bag-11/"
    #url = "http://designer-discreet.ru/product/dior-shoulder-bags-2/"
    #scrape(url)
