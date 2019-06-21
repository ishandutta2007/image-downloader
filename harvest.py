#coding=utf-8

import xlrd,os,random

def add():
    f = open("C://Users//wu//Downloads//guest_post.txt")
    lines  = f.readlines()
    f.close()
    fk = open("C://Users//wu//Downloads//guest_keywords.txt")
    keywords = fk.readlines()
    fk.close()

    f_new = open("C://Users//wu//Downloads//guest_post2.txt","w")
    for k in list(set(keywords)):
        for line in lines:
            f_new.write(k.strip()+" "+line.strip()+"\n")
    f_new.close()

if __name__ =="__main__":
    add()

