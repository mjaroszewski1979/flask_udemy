import smtplib
from email.message import EmailMessage
from os import environ

email_address = environ.get('EMAIL_ADDRESS')
email_password = environ.get('EMAIL_PASSWORD')


def send_mail(name, email, message):
    new_message = message
    msg = EmailMessage()
    msg['Subject'] = email
    msg['From'] = name
    msg['To'] = 'mjaroherokuapp@gmail.com'
    msg.set_content(new_message)  

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)