import requests
from bs4 import BeautifulSoup
import random
import logging
logging.captureWarnings(True)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = "https://www.all-hashtag.com/library/contents/ajax_generator.php"
data = {}
def get_hashtag(keyword):
    data.update({"keyword":keyword,"filter":"random"})
    resp = requests.post(url, data=data, headers=headers,verify=False)
    soup = BeautifulSoup(resp.content, 'html.parser')
    tag = soup.find("div", {"id": "copy-hashtags"})
    print keyword,tag
    l = tag.text.split("#")
    s=  '#'.join(random.sample(l, 10))
    return s




if __name__ == "__main__":
    get_hashtag("yoga")

