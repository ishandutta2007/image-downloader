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

content = '''hello {name},\n
    Hey i sent you email yesterday , did you get it? Its very important anyway.Reply me back to confirm that you already got this email.\n
The email is about \n
    \n
    \n

Sent from my iPhone
    '''
f = open("sample0614.html",'r')
html_content = f.read()
f.close()
send_from = "kate@gameandroid.info"
# MONGO_HOST = '127.0.0.1'
# MONGO_PORT = 27017
# MONGO_DB = 'txt'
# MONGO_USER_COLL = 'email'
# MONGO = MongoClient(MONGO_HOST,MONGO_PORT)

def send_mail(mail_from, password, mail_to, subject, content):
    handle = smtplib.SMTP('mail.gameandroid.info', 25)
    handle.ehlo()
    handle.starttls()

    handle.login(mail_from, password)
    msg = MIMEMultipart()
    msg["From"] = send_from
    msg["To"] = mail_to
    msg["Subject"] = subject
    msg.attach(MIMEText(content, 'plain'))

    handle.sendmail(send_from, mail_to, msg.as_string())
    handle.close()
    #if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':mail_to}):
    #   MONGO[MONGO_DB][MONGO_USER_COLL].insert_one({'_id':mail_to})
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
    msg.attach(MIMEText(content, 'html'))

    handle.sendmail(send_from, mail_to, msg.as_string())
    handle.close()
    #if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':mail_to}):
    #   MONGO[MONGO_DB][MONGO_USER_COLL].insert_one({'_id':mail_to})
    print ("Email send")

def split_list(lines):
    global content
    num = 0
    for line in lines:
        if not (line.find("@") != -1):
            continue

        #if MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id': line}):
        #    continue

        line = line.strip()
        line_list = line.split("@")
        username,mailserver = line_list[0],line_list[1]
        if mailserver in ["aol.com"]:
            continue
        if username.find(".") != -1:
            username = username.split(".")[0]
        print num
        #if num > 50:
        #    sys.exit()
        #d[mailserver] = d.get(mailserver,0)+1
        content = content.format(name=username)
        global html_content
        #print ("Email send to %s" % line)
        html_content = html_content

        send_mail('kate', 'password123',line, 'Hi %s' % username, content)
        num = num +1
        #   time.sleep(200)

if __name__ == '__main__':
    num = 0
    lines = [line.rstrip('\n') for line in open('F://500px_photos-master//contacts_0610.csv')]
    d = {}
    for line in lines:
        mail = line.split("@")[1].strip()
        d[mail] = d.get(mail, 0) + 1


    l = []
    for k,v in d.items():
        l.append(k.strip())

    process_list = []

    split_mail = ["said_energizer@mail.ru"]
    #email_str = "ipm1kgb@glockapps.com; allanb@glockapps.awsapps.com; markb@glockapps.awsapps.com; ingridmejiasri@aol.com; caseywrighde@aol.de; baileehinesfr@aol.fr; brendarodgersuk@aol.co.uk; franprohaska@aol.com; garrettjacqueline@aol.com; leannamccoybr@aol.com; julia_g_76@icloud.com; gappsglock@icloud.com; zacheryfoleyrx@azet.sk; bcc@spamcombat.com; chazb@userflowhq.com; glock.julia@bol.com.br; carloscohenm@freenet.de; janefergusone@gmail.com; llionelcohenbr@gmail.com; bbarretthenryhe@gmail.com; louiepettydr@gmail.com; lenorebayerd@gmail.com; cierawilliamsonwq@gmail.com; silviacopelandqy@gmail.com; daishacorwingx@gmail.com; verify79@buyemailsoftware.com; joanyedonald@gmail.com; emilikerr@gmail.com; wandammorrison@gmail.com; lawrenceleddylr@gmail.com; alisonnlawrence@gmail.com; tinamallahancr@gmail.com; verifycom79@gmx.com; verifyde79@gmx.de; gd@desktopemail.com; jpatton@fastdirectorysubmitter.com; frankiebeckerp@hotmail.com; sgorska12@interia.pl; layneguerreropm@laposte.net; britnigrahamap@laposte.net; amandoteo79@libero.it; glocktest@vendasrd.com.br; b2bdeliver79@mail.com; verifymailru79@mail.ru; glockapps@mc.glockapps.com; verify79ssl@netcourrier.com; nsallan@expertarticles.com; evalotta.wojtasik@o2.pl; exosf@glockeasymail.com; krysiawal1@onet.pl; brendonosbornx@outlook.com; tristonreevestge@outlook.com.br; brittanyrocha@outlook.de; glencabrera@outlook.fr; christopherfranklinhk@outlook.com; kaceybentleyerp@outlook.com; meaghanwittevx@outlook.com; aileenjamesua@outlook.com; shannongreerf@outlook.com; gabrielharberh@outlook.com; candidobashirian@outlook.com; vincenzaeffertz@outlook.com; verify79@seznam.cz; sa79@justlan.com; amandoteo79@virgilio.it; verify79@web.de; sebastianalvarezv@yahoo.com.br; verifyca79@yahoo.ca; justynbenton@yahoo.com; testiotestiko@yahoo.co.uk; emailtester493@yahoo.com; loganbridgesrk@yahoo.com; rogertoddw@yahoo.com; darianhuffg@yahoo.com; andreablackburn@yandex.ru; verifynewssl@zoho.com; lamb@glockdb.com"
    #split_mail = email_str.split(";")
    split_list(split_mail)
    # for mail in l:
    #     split_mail = [line for line in lines if line.split("@")[1].strip() == mail.strip()]
    #     #print split_mail
    #     p = multiprocessing.Process(target=split_list, args=(split_mail,))
    #     process_list.append(p)
    #
    # for process in process_list:
    #     process.start()

