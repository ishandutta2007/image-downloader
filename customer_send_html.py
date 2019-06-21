#coding=utf-8

###send email from custom domain
###
###
import smtplib
import time, traceback, sys, os,re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pymongo import MongoClient
import logging
import multiprocessing

content = '''hello {name},<br/>
    Hey i sent you email yesterday , did you get it? Its very important anyway.Reply me back to confirm that you already got this email.<br/>
    The email is about <br/>
    <br/>
    <br/>
    <br/>


Sent from my iPhone
    '''
f = open("t5_2.html",'r')
html_content = f.read()
f.close()
send_from = "kate@gameandroid.info"
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'send'
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
    msg.attach(MIMEText(content, 'html'))

    handle.sendmail(send_from, mail_to, msg.as_string())
    handle.close()
    if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':mail_to}):
       MONGO[MONGO_DB][MONGO_USER_COLL].insert_one({'_id':mail_to})
    print ("Email send")

BASE_DIR = "F:\mail\cur"
regex = r"<\S+@\S+>"


def check(send_to):
    for file in os.listdir(BASE_DIR):
        mail = os.path.join(BASE_DIR, file)
        f = open(mail,'r')
        content = f.read()
        f.close()
        r1 = re.findall(regex,content)
        for r in r1:
            send_email = r.strip("<").strip(">")
            if r != send_from and send_to == send_email:
                return True
    return False


def send_html(mail_from, password, mail_to, subject, content):
    handle = smtplib.SMTP('mail.gameandroid.info', 25)
    handle.ehlo()
    handle.starttls()

    handle.login(mail_from, password)
    msg = MIMEMultipart('alternative')

    msg["From"] = send_from
    msg["To"] = mail_to
    msg["Subject"] = subject
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
        if not (line.find("@") != -1):
            continue


        line = line.strip()

        line_list = line.split("@")
        username,mailserver = line_list[0],line_list[1]
        print line
        if check(line):
            continue

        if mailserver in ["aol.com"]:
            continue
        if username.find(".") != -1:
            username = username.split(".")[0]
        print num
        #if num > 50:
        #   sys.exit()
        content = content.format(name=username)
        print ("Email send to %s" % line)
        global html_content
        html_content = html_content

        send_html('kate', 'password123',line, 'Hi %s' % username, html_content)
        num = num +1
        time.sleep(1200)

if __name__ == '__main__':
    num = 0
    #lines = [line.rstrip('\n') for line in open('F://500px_photos-master//contacts_0610.csv')]
    lines = []
    db = MONGO.txt
    collection = db['email']
    cursor = collection.find({})
    d = {}


    for line in cursor:
        line = line.strip()
        line = line.get("_id")
        lines.append(line)
        if MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': line}):
            continue
        mail = line.split("@")[1].strip()
        d[mail] = d.get(mail, 0) + 1

    l = []
    print len(d.items())
    for k,v in d.items():
        l.append(k.strip())

    process_list = []
    print l
    for mail in l:
        split_mail = [line for line in lines if line.split("@")[1].strip() == mail.strip()]
        p = multiprocessing.Process(target=split_list, args=(split_mail,))
        process_list.append(p)

    for process in process_list[:1]:
        process.start()

