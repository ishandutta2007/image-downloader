import smtplib

gmail_user = 'aghand3x@gmail.com'  
gmail_user = '29jl6mwl@gmail.com'
gmail_password = "password!@23"

sent_from = gmail_user  
to = ['augustwu23@gmail.com']  
subject = 'OMG Super Important Message'  
body = 'Hey, what'

subject = 'hello %s,we provide fashion clothes and fine arts for you.Please check.'
f = open("t5_2.html",'r')
messageHTML = f.read()
f.close()

email_text = """\  
From: %s  
To: %s  
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, messageHTML)

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print 'Email sent!'
except Exception as e:
    print str(e)	  
    print 'Something went wrong...'

