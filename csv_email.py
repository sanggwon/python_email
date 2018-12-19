import csv
import smtplib
from email.message import EmailMessage

import getpass

password = getpass.getpass('비밀')

f = open('pygj - email.csv', 'r', encoding = 'utf-8')
#r : 읽다
read_csv = csv.reader(f)

smtp_url = 'smtp.naver.com'
smtp_port = 465


s = smtplib.SMTP_SSL(smtp_url, smtp_port)
s.login('ck2570@naver.com', password)

for line in read_csv :
    msg = EmailMessage()
    msg['Subject'] = "차상권입니다"
    msg['From'] = "ck2570@naver.com"
    msg['TO'] = line[1]
    msg.set_content(line[0]+ '님 '+'배고파요')

        #보안연결에 필요
     
    s.send_message(msg)
f.close()
    