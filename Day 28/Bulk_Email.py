#  python | Day 28
# Bulk E-mail.
# Using the built-in SMTP module, write a function
# that takes a list of emails as input, and sends each
# of them an(any) email message.


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


email_list = []     # list of email addresses you want to send to.


def bulk_email_sender(receivers):
    """A function to send bulk emails using the SMTP module."""

    sender = "your_email_account"
    password = "your_email_password "

    message = MIMEMultipart()

    message['From'] = sender
    message['To'] = ",".join(receivers)
    message['Subject'] = "your mail subject"

    body = "your message body"
    
    message.attach(MIMEText(body, 'plain'))

    for address in receivers:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.ehlo()
        s.login(sender, password)
        text = message.as_string()
        s.sendmail(sender, address, text)
        s.close()
        print("Successfully sent mail.")


bulk_email_sender(email_list)
