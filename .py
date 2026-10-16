'''
SMTP: Simple mail transfer protocol.:
--->This is used to send emails from server to another server.....

Note:
1.SMTP SSL Port
----------------
465
2. SMTP TLS port
----------------
587

import smtplib

EmailMessage Class
------------------
msg['Subject'] = 'SMTP ON MAIL'
msg['From']    = 'sender@mail.com'
msg['To']      =  'Receiver@mail.com'


import smtplib
from email.message import EmailMessage
sender ='bhavanajoseph84392@gmail.com'
password = 'lcwzjqprmsurevqq'
wps = EmailMessage()

wps['Subject'] = 'Welcome Mail'
wps['From'] = sender
wps['To'] = 'saranyasiri2005@gmail.com'

wps.set_content('Hello')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(wps)
server.quit()
'''
import smtplib
from email.message import EmailMessage
sender='bhavanajoseph84392@gmail.com'
password ='sryd bqal rsul izbx'
receiver_ = ['saranyasiri2005@gmail.com','chandinikandregula5@gmail.com']
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver_:
    wps =EmailMessage()
    wps ['Subject'] ='Welcome Mail'
    wps['From'] = sender
    wps['To'] = email
    wps.set_content('Hi buddy')
    server.send_message(wps)
server.quit()
