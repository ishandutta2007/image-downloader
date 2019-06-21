#coding=utf-8
import os,re

BASE_DIR = "F:\mail\cur"

from_mail = "<kate@gameandroid.info>"
regex = r"<\S+@\S+>"


def check():
    for file in os.listdir(BASE_DIR):
        mail = os.path.join(BASE_DIR, file)
        f = open(mail,'r')
        content = f.read()
        f.close()
        r1 = re.findall(regex,content)
        for r in r1:
            if r != from_mail:
                print r.strip("<").strip(">")



if __name__ == "__main__":
    check()