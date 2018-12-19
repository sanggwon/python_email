import smtplib
from email.message import EmailMessage

import getpass
#비밀번호 보안
password = getpass.getpass('비밀번호 입력하세요')

# email_list = ['ck2570@hanmail.net, ck3929@gmail.com']

# for email in email_list : 
msg = EmailMessage()
msg['Subject'] = "제목"
msg['From'] = "ck2570@naver.com"
msg['TO'] = "ck2570@naver.com"
# msg.set_content('내용')

msg.add_alternative('''
<h1>안녕하세요!!!</h1>
<p>저는 차상권입니다.</p>
''', subtype = "html")

smtp_url = 'smtp.naver.com'
smtp_port = 465

s = smtplib.SMTP_SSL(smtp_url, smtp_port)
#보안연결에 필요

s.login('ck2570', password)
s.send_message(msg)