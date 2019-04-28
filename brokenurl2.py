#coding=utf-8
import os,xlrd,csv,whois
from xlrd import open_workbook, cellname
from tld import get_tld
from tld import get_fld
import tldextract
import pythonwhois

proxy = {"http":"localhost:10110"}
ua_string = {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3'}

import urllib,pymongo

from pymongo import MongoClient

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'brokenurl2'
MONGO_USER_COLL = 'urls2'
MONGO_ERROR_COLL = 'domains2'

MONGO = MongoClient(MONGO_HOST, MONGO_PORT)

def do_filter(f):

    url_list  = []

    if f.find("brokenlinks") != -1:
        with open(f, 'r') as csvFile:
            reader = csv.reader((line.replace('\0','') for line in csvFile))
            for row in reader:
                content =  row[6]
                if content.find("http") != -1:
                    #domain = content.split("//")[-1].split("/")[0]
                    ext = tldextract.extract(content)
                    domain = ext.registered_domain
                    url_list.append(domain)
                    #try:
                    #    w =  pythonwhois.get_whois(domain)
                     #   if 'No match for' in str(w):
                    if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': domain}):
                        print "No match for domain %s" % domain
                        try:
                            MONGO[MONGO_DB][MONGO_USER_COLL].insert_one({'_id': domain})
                        except pymongo.errors.DuplicateKeyError, e:
                            print e
                   # except Exception,e:
                    #    print str(e)


                        #domain_file.write(domain + "\n")

    #domain_file.close()

if __name__ == "__main__":
    from multiprocessing import Process, Lock

    file_list = []
    for dirpath, dnames, fnames in os.walk("C://Users//wu//Downloads//links"):
        for f in fnames:
            if f.endswith(".csv"):
                csv_file = os.path.join(dirpath, f)
                file_list.append(csv_file)

    for csv_file in file_list:
        Process(target=do_filter, args=(csv_file, )).start()