import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email_address = 'dallascassiem704@gmail.com'
receiver_email_address = 'aaliyahjar13@gmail.com', 'gafrica851', 'zaidflandorp4@gmail.com',
password = input("Enter password: ")
subject = "Hello world"
message = MIMEMultipart()
message['From'] = sender_email_address
message['To'] = ','.join(receiver_email_address)
message['Subject'] = subject
body = "HI!"
message.attach(MIMEText(body, 'plain'))
text = message.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_email_address, password)

s.sendmail(sender_email_address, receiver_email_address, text)
s.quit()

