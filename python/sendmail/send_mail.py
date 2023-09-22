#!/usr/bin/env python3
import datetime
import smtplib
import uuid
from collections import defaultdict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import localtime, strftime

get_current_time = lambda fmt_time: datetime.datetime.now().strftime(fmt_time)
_timezone        = lambda: strftime("%z", localtime())  # Timezone local

config = defaultdict(dict)  # Init config

with open('config.properties', 'r') as _file:
    for line in _file:
        line = line.strip() # Ignore comments and empty lines
        if line and not line.startswith('#'):
            key, value = line.split('=', 1)
            config[key.strip()] = value.strip()

# Email Config
# ------------
NUMBER_EMAIL                  = int(config['emailconfig.number'])
SENDER_EMAIL, SENDER_PASSWORD = config['emailconfig.sender'], config['emailconfig.password']
RECEIVER_EMAIL                = config['emailconfig.receiver']

# Server Config
# -------------
SMTP_HOST, SMTP_PORT = (config['serverconfig.smtp_host'], config['serverconfig.smtp_port'])

count = 0
while count < NUMBER_EMAIL:
    SUBJECT = f"[{get_current_time('%Y-%m-%d %H:%M:%S')}] {config['emailcontent.subject']}"
    BODY    = config['emailcontent.body']

    # Message
    # -------
    msg               = MIMEMultipart()
    msg['From']       = SENDER_EMAIL
    msg['To']         = RECEIVER_EMAIL
    msg['Subject']    = SUBJECT
    msg['Message-ID'] = str(uuid.uuid4())
    msg['Date']       = f"{_timezone()} {get_current_time('%a, %-d %b %Y %H:%M:%S')}"
    msg.attach(MIMEText(BODY, 'plain'))

    try:
        smtp_server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
        smtp_server.login(SENDER_EMAIL, SENDER_PASSWORD)                    # Login to your email account 
        smtp_server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string()) # Send the email
        smtp_server.quit()
    except Exception as e:
        print(f"Email sent failed {e}")        

    count -= -1
    print(f"> ({count}) Email sent successfully to: {RECEIVER_EMAIL}")
