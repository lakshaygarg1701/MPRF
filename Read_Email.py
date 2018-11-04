import time
import email
import smtplib
import imaplib
import mailparser
import sqlite3
from datetime import datetime as dt


conn=sqlite3.connect('../mprf/db.sqlite3')
crs=conn.cursor()
insert='insert into test values(null,?,?,?,?,?,?,?,?)'

def read_email_from_gmail(crs):
    try:
        user='garglakshay631@gmail.com'
        password="abcd@1234"
        serverimap = imaplib.IMAP4_SSL('imap.gmail.com')
        serverimap.login(user,password)
        serverimap.select('inbox')
        serversmtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        serversmtp.login(user, password)

        typ, data = serverimap.search(None, 'UnSeen')
        print("Connection",typ)
        print(data)
        mail_ids = data[0]
        
        id_list = mail_ids.split()
        if len(id_list)==0:
            print('Database is up to date')
            return
        first_email = int(id_list[0])
        latest_email = int(id_list[-1])
        for i in range(latest_email,first_email-1,-1):
            typ, data = serverimap.fetch(str(i), '(RFC822)' )
            for response_part in data:
                if isinstance(response_part, tuple):
                    mail = mailparser.parse_from_bytes(response_part[-1])
                    name=mail.subject
                    to=mail.to[-1][-1]
                    from_=mail.from_[-1][-1]
                    att=mail.attachments
                    body=mail.text_plain[-1]
                    b=body.split('\r\n')
                    contact=b[-1]
                    date=b[-3]
                    date=dt.strptime(date,'%d %B %Y, %I %p')
                    venue=b[-5]
                    reg=b[-7]
                    str1="\r\n".join(b[:-7])
                    crs.execute('insert into event values(null,?,?,?,?,?,?,?,?)',(name,from_,to,str1,date,venue,reg,contact))
        conn.commit()
        conn.close()

    except (Exception, e):
        print (str(e))