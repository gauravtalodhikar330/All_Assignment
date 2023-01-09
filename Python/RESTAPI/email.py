import smtplib


smtp_server = "smtp.gmail.com"
sender_email = "gauravtalodhikar2108@gmail.com"  # Enter your address
receiver_email = "gauravtalodhikar62@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
#message 
message = """\
Subject: Hi there

'https://realpython.com/python-send-email/'


This message is sent from Python."""


#connecting with smtplib

with smtplib.SMTP_SSL(smtp_server) as server:
    server.login(sender_email, password)
    print("login Successfully...")
    server.sendmail(sender_email, receiver_email, message)
    print("Mail Send Successfully...")