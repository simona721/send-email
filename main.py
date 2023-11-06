import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password"
subject = "SMTP email test"
body = "This is a test email message."

message = f"""From: {sender}
To: {receiver}
Subject: {subject} /n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    print("Email has been send!")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
