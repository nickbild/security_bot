import smtplib
import configparser

config = configparser.RawConfigParser()
config.read('email.cfg')
creds = dict(config.items('AUTH'))

FROM = 'nick.bild@gmail.com'
TO = ['nick.bild@gmail.com']
SUBJECT = 'Security Camera Alert'
TEXT = 'Intruder detected on iRobot camera!'

message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP("smtp.sendgrid.net", 587)
server.starttls()
server.login('apikey', creds['apikey'])

server.sendmail(FROM, TO, message)
server.quit()
