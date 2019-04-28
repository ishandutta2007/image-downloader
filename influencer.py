#coding=utf-8
import requests
from bs4 import BeautifulSoup

url = "https://hypeauditor.com/top-instagram-beauty-fashion/?p=%s"
def get_username():


    for i in range(1,11):
        resp = requests.get(url % str(i))
        content = resp.content
        soup = BeautifulSoup(content,"lxml")
        f = open("influencers_%s.txt" % str(i), "a")
        for data in soup.find_all("td",attrs={'class':"bloggers-top-name"}):
            for a in data.find_all('a'):
                print a.text[1:]
                f.write(a.text[1:]+"\n")

        f.close()

if __name__ == "__main__":
    get_username()
