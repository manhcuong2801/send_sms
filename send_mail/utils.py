import smtplib
import os
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import twilio
from twilio.rest import Client

from send_mail import settings

MY_ADDRESS = settings.EMAIL_HOST
PASSWORD = settings.PASSWORD_HOST


def send_mail(email: str, name: str, mobile: str, code: str):
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email
    msg = MIMEMultipart()  # create a message

    message = f'Hello {name}' \
              f'Mobile: {mobile}' \
              f'Code: {code}'

    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "Oi ban oi"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message vuia the server set up earlier
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()


def send_sms(mobile: str, name: str, code: str):
    account_sid = 'ACa849796f9dd465d41d8a82031e4fbb33'
    auth_token = '3f9c7172caa070e2f13c4f47d108c5c2'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Go n share {name}, {code}",
        from_='+19282206136',
        to=mobile
    )
