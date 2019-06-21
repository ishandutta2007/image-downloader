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

f_handler = logging.FileHandler('google_mail1.log')
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

        #server = smtplib.SMTP('smtp.gmail.com', 587)
	#server.ehlo()
        #server.starttls()
	#server.ehlo()
        #server.login(email, password)
        #text = msg.as_string()
        #server.sendmail(email, send_to_email, text)
        #server.quit()
        #if not MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':send_to_email}):
        #    MONGO[MONGO_DB][MONGO_USER_COLL].insert_one({'_id':send_to_email})
    	
	#f = open(filename,"a")
        #f.write(send_to_email+"\n")
        #f.close()
    except Exception as e:
	if str(e).find("Daily user sending") != -1:
	    return 1

	logger.error("send error,send to %s,exception is %s,from email is %s" % (send_to_email,str(e),email))
	return 2
    return 0

def read_files(lines,from_email,password,lock):
    import sys,os
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
    from_email1 = "augustwu23@gmail.com"
    password1 = "qq263020776"
    from_email2 = "raibraniby@gmail.com"
    password2 = "passworD!@23"

    from_email3 = "freemac.me@gmail.com"
    password3 = "263020776.com"
    from_email4 = "hendonagota@gmail.com"
    password4 = "password!@23"

    from_email4 = "62i55rfs@gmail.com"
    password4 = "password!23"
    from_email5 = "lovelyshanghai.com@gmail.com"
    password5 = "qq263020776"	 

    from_email6 = "88zbspqf@gmail.com"
    password6 = "password!23"	 

    from_email7 = "94inqmz3@gmail.com"
    password7 = "password!@23"
    from_email8 = "n0l29sty@gmail.com"
    password8 = "password!@23"

    from_email9 = "wx6a8iwe@gmail.com"
    password9 = "password!@23"

    from_email1 = "hdkak6382@gmail.com"
    password1 = "ys7722882"

    from_email11 = "a2pgyw7@gmail.com"
    password11 = "password!23"
   
    from_email12 = "q9d7w23r@gmail.com"
    password12 = "password!23"
    from_email13 = "zaz15x29kq@gmail.com"
    password13 = "password!23"


    from_email14 = "cq8n5icq@gmail.com"
    password14 = "password!23"
    from_email15 = "5fj4czzd@gmail.com"
    password15 = "password!23"


    lock = multiprocessing.Lock()


    lines = [line.rstrip('\n') for line in open('/home/august/amazon-review/google/contacts_0519.csv')]
    #clean_lines = []
    #for line in lines:
    #   	
    #  line = line.strip() 
    #  if not  MONGO[MONGO_DB][MONGO_USER_COLL].find_one({'_id':line}):
    #    clean_lines.append(line)
    read_files(['augustwu23@gmail.com'],from_email1,password1,lock)
    	
#    l = numpy.array_split(clean_lines,15);
#    print l
#    p1 = multiprocessing.Process(target=read_files, args=(l[0],from_email1,password1,lock))
#    p2 = multiprocessing.Process(target=read_files, args=(l[1],from_email2,password2,lock))
#    p3 = multiprocessing.Process(target=read_files, args=(l[2],from_email3,password3,lock))
#    p4 = multiprocessing.Process(target=read_files, args=(l[3],from_email4,password4,lock))
#    p4 = multiprocessing.Process(target=read_files, args=(l[4],from_email6,password6,lock))
#    p5 = multiprocessing.Process(target=read_files, args=(l[4],from_email8,password8,lock))
#    p6 = multiprocessing.Process(target=read_files, args=(l[5],from_email9,password9,lock))
#    p7 = multiprocessing.Process(target=read_files, args=(l[6],from_email10,password10,lock))
#    p8 = multiprocessing.Process(target=read_files, args=(l[7],from_email8,password7,lock))
#    p9 = multiprocessing.Process(target=read_files, args=(l[8],from_email9,password9,lock))
#    p10 = multiprocessing.Process(target=read_files, args=(l[9],from_email10,password10,lock))
#    p11 = multiprocessing.Process(target=read_files, args=(l[10],from_email11,password11,lock))
#    p12 = multiprocessing.Process(target=read_files, args=(l[11],from_email12,password12,lock))
#    p13 = multiprocessing.Process(target=read_files, args=(l[12],from_email13,password13,lock))
#    p14 = multiprocessing.Process(target=read_files, args=(l[13],from_email14,password14,lock))
#    p15 = multiprocessing.Process(target=read_files, args=(l[14],from_email15,password15,lock))
#    
#    process_list = []
#    process_list.append(p1)
#    process_list.append(p2)
#    process_list.append(p3)
#    process_list.append(p4)
#    process_list.append(p5)
#    process_list.append(p6)
#    process_list.append(p7)
#    process_list.append(p8)
#    process_list.append(p9)
#    process_list.append(p10)
#    process_list.append(p11)
#    process_list.append(p12)
#    process_list.append(p13)
#    process_list.append(p14)
#    process_list.append(p15)
#    for p in process_list:
#        import random	
#        #time.sleep(random.randint(1,10))
#	p.start()
#    for p in process_list:
#	p.join()
#
