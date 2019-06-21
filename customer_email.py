#coding=utf-8

###send email from custom domain
###
###
import smtplib
import time, traceback, sys, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pymongo import MongoClient
import logging
import multiprocessing
import random
from email.utils import formatdate


content = '''hi,\n
    I sent you email yesterday , did you get it? Its very important anyway.Reply me back to confirm that you already got this email.\n
    The email is about \n
    \n
    \n
    \n


Sent from my iPhone
    '''


content1 = '''hi,\n
    I sent you email few days ago , did you get it?.Reply me back to confirm that you already got this email.\n
    The email is about \n
    \n
    \n
    \n


Sent from my iPhone
    '''


content2 = '''hello,\n
    I sent you email last week ago , did you get it?.Reply me back to confirm that you already got this email.\n
    It is about \n
    \n
    \n
    \n


Sent from my iPhone
    '''

content3 = '''hi,\n
    I sent you email last week , did you get it?.It's important.Reply me back to confirm that you already got this email.\n
    It is about \n
    \n
    \n
    \n


Sent from my iPhone
    '''

content4 = '''hi,\n
    I sent you email yesterday , did you get it?.It's important.Reply me back to confirm that you already got this email.\n
    This email is about \n
    \n
    \n
    \n


Sent from my iPhone
    '''




f = open("t5_2.html",'r')
html_content = f.read()
f.close()
send_from = "kate@gameandroid.info"
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'txt'
MONGO_USER_COLL = 'email'
MONGO = MongoClient(MONGO_HOST,MONGO_PORT)

def send_mail(mail_from, password, mail_to, subject, content):
    handle = smtplib.SMTP('mail.gameandroid.info', 25)
    handle.ehlo()
    handle.starttls()

    handle.login(mail_from, password)
    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = mail_to
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)

    msg.attach(MIMEText(content, 'plain'))

    handle.sendmail(send_from, mail_to, msg.as_string())
    handle.close()
    if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':mail_to}):
       MONGO[MONGO_DB][MONGO_USER_COLL].insert_one({'_id':mail_to})
    print ("Email send")


def send_html(mail_from, password, mail_to, subject, content):
    handle = smtplib.SMTP('mail.gameandroid.info', 25)
    handle.ehlo()
    handle.starttls()

    handle.login(mail_from, password)
    msg = MIMEMultipart('alternative')

    msg["From"] = send_from
    msg["To"] = mail_to
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(content, 'html'))

    handle.sendmail(send_from, mail_to, msg.as_string())
    handle.close()
    if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':mail_to}):
       MONGO[MONGO_DB][MONGO_USER_COLL].insert_one({'_id':mail_to})
    print ("Email send")

def split_list(lines):
    global content
    num = 0
    for line in lines:
        line = line.strip()
        if not (line.find("@") != -1):
            continue

        if MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': line}):
            continue

        line_list = line.split("@")
        username,mailserver = line_list[0],line_list[1]
        #if mailserver in ["aol.com"]:
        #    continue
        if username.find(".") != -1:
            username = username.split(".")[0]

        #d[mailserver] = d.get(mailserver,0)+1
        content = random.choice([content,content1,content2,content3,content4])
        #content = content.format(name=username)
        #html_content = html_content
        print ("Email send to %s" % line)
        #html_content = html_content

        send_mail('kate', 'password123',line, 'Hi ', content)
        num = num +1
        rtime = random.randomint(240,400)
        time.sleep(rtime)

if __name__ == '__main__':
    num = 0
    lines = [line.rstrip('\n') for line in open('F://500px_photos-master//contacts_0610.csv')]
    lines = lines[7542:]
    d = {}
    clean_email = []
    for line in lines:
        line = line.strip()

        if MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': line}):
            continue
        mail = line.split("@")[1].strip()
        d[mail] = d.get(mail, 0) + 1
        clean_email.append(line)


    l = []
    for k,v in d.items():
        #if v>100:
        l.append(k.strip())

    process_list = []
    print len(l)
    for mail in l:
        split_mail = [line for line in clean_email if line.split("@")[1].strip() == mail.strip()]
        #print split_mail
        p = multiprocessing.Process(target=split_list, args=(split_mail,))
        process_list.append(p)

    for process in process_list:
        process.start()

