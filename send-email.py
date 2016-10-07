# from flask.ext.mail import Message
# from flask import *
# from flask.ext.mail import Mail
# app = Flask(__name__)
# mail = Mail(app)
# MAIL_SERVER = 'smtp.googlemail.com'
# MAIL_PORT = 465
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True
# MAIL_USERNAME = 'kimsalsan12@gmail.com'
# MAIL_PASSWORD = '11101999sal'


# msg = Message('test subject', sender='kimsalsan12@gmail.com', recipients='kimsalsan007@gmail.com')
# msg.body = 'text body'
# msg.html = '<b>HTML</b> body'
# # with app.app_context():
# mail.send(msg)

# from flask.ext.emails import Message

# message = Message(html='<html><p>Hi! ...',
#                   subject="Party today",
#                   mail_from=("John Brown", "kimsalsan12@gmail.com"))
# # message.attach(data=open('Event.ics', 'rb'), filename='Event.ics')

# r = message.send(mail_to=("Nick Jackson", "kimsalsan007@gmail.com"))

# if r.status_code not in [250, ]:
#     # message is not sent, deal with this
#     print "email error 250"


import smtplib
fromaddr = 'kimsalsan12@gmail.com'
toaddrs  = 'kimsalsan007@gmail.com'
msg = 'Why,Oh why!'
username = 'kimsalsan12@gmail.com'
password = '11101999sal'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

#https://support.google.com/mail/answer/14257?visit_id=1-636099305671462861-441156299&rd=1
# http://www.google.com/accounts/DisplayUnlockCaptcha