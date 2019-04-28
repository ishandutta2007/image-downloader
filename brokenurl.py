#coding=utf-8
import os,xlrd,csv,whois
from xlrd import open_workbook, cellname
from tld import get_tld
from tld import get_fld
import tldextract

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
    domain_file = open("domain.txt", "a")

    for f in file_list:
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
                        try:
                            w = whois.whois(domain)

                        except Exception,e:
                            try:
                                s = str(e)
                            except:
                                continue
                            print s
                            if s.find("timed out") != -1:
                                continue

                            if s.find("[Errno") !=-1:
                                continue

                            print "unregisted domain:%s" % domain
                            domain_file.write(domain + "\n")

    domain_file.close()

if __name__ == "__main__":
    do_filter()