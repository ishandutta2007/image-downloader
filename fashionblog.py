#coding=utf-8
import xml,requests
from lxml import html
from bs4 import BeautifulSoup

def begin():
    r = requests.get("https://www.blogmetrics.org/fashion")
    content = r.content
    f = open("fashion.txt",'w')
    soup = BeautifulSoup(content,'lxml')
    for p in soup.find_all("td",{"class":"blog_content_cellb-white"}):
        for href in p.find_all("a", href=True):
            print href['href']
            f.write(href['href']+"\n")
    f.close()

if __name__ == "__main__":
    begin()

