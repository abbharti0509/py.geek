'''
Name : Anand Bharti
Intern id : 4045
'''
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
port = 587 
smtp_server = "smtp.gmail.com"
sender_email = input('Type senders email address and press enter\n') #you can directly enter Senders the email address elclosed in single quotes
password = input("Type your password and press enter:\n") #you can directly enter the password elclosed in single quotes
receiver_email = input('Type Receivers email address and press enter\n') #you can directly enter the receivers email address elclosed in single quotes
msg=MIMEMultipart()
msg['Subject'] = input('Enter the subject\n') #you can directly enter the subject elclosed in single quotes
content=input('Enter the body of mail\n') #you can directly enter the Body if the mail elclosed in single quotes
msg.attach(MIMEText(content))
'''
Or you can directly enter subject and body of the mail in following format
message = """\
Subject: Hi there

This message is sent from Python."""
'''
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo() 
    server.starttls(context=context)
    server.ehlo()  
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
print('Email Sent.....')
