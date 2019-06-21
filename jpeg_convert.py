#coding=utf-8
import os

def convert(name):
    print name
    print name.split(".")[0]+".jpg"
    os.rename(name, name.split(".")[0]+".jpg")


if __name__ == "__main__":
    for (dirpath, dirnames, filenames) in os.walk("C://Users//wu//Documents//catalog//clothing//dresses"):
        for filename in filenames:
            if filename.endswith('jpeg'):
                convert(os.path.join(dirpath,filename))
