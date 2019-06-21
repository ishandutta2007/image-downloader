import smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time,numpy
import multiprocessing
import logging.handlers
import datetime
from pymongo import MongoClient
import logging

#email = 'augustwu23@gmail.com'
#password = 'qq263020776'
subject = 'hello %s,we provide fashion clothes and fine arts for you.Please check.'
f = open("t5_2.html",'r')
messageHTML = f.read()
f.close()

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'send'
MONGO_USER_COLL = 'email'
MONGO = MongoClient(MONGO_HOST,MONGO_PORT)

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

#rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
#rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('google_mail2.log')
f_handler.setLevel(logging.INFO)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

#logger.addHandler(rf_handler)
logger.addHandler(f_handler)



def send_email(email,password,send_to_email,lock):
    msg = MIMEMultipart('alternative')
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject % send_to_email.split("@")[0]
    
    # Attach both plain and HTML versions
    #msg.attach(MIMEText(messagePlain, 'plain'))
    msg.attach(MIMEText(messageHTML, 'html'))
    try:
        if  MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':send_to_email}):
            return
        logger.info("from email is %s send email to %s" % (email,send_to_email))
        print ("from email is %s send email to %s" % (email,send_to_email))
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email,text)
        server.close()

        #if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':send_to_email}):
         #   MONGO[MONGO_DB][MONGO_USER_COLL].insert_one({'_id':send_to_email})

    except Exception as e:
        if str(e).find("Daily user sending") != -1:
            return 1

        logger.error("send error,send to %s,exception is %s,from email is %s" % (send_to_email,str(e),email))
        return 2
    return 0

def read_files(lines,from_email,password,lock):
    count = 0
    start = time.time() 	
    for line in lines:
       	
      line = line.strip() 
      print (from_email,line)	
      if  MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':line}):
        continue 
      if line.find("@") == -1:
        print ("-----")
        continue
      #if count >100:
      # 	continue
      start = time.time() 	
      ret = send_email(from_email,password,line,lock)
      if ret == 1:
	end = time.time()
	time.sleep(86400 - (end -start) + 10)
      if ret == 2:
	continue  	
		
      count += 1
      time.sleep(864)	
      #print ("from email is %s to email is %s,count now is %s" % (from_email,line,str(count)))
    
if __name__ == "__main__":
    from_email1 = "hdkak6382@gmail.com"
    password1 = "ys7722882"


    lock = multiprocessing.Lock()


    lines = [line.rstrip('\n') for line in open('/home/august/amazon-review/google/contacts_0519.csv')]

    read_files(lines[:3000],from_email1,password1,lock)
