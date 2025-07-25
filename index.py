import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os 

load_dotenv()

Email_Address = os.getenv('EMAIL_ADDRESS')
Email_Password = os.getenv('EMAIL_PASSWORD')


with open('recipients.txt', 'r') as f:
    recipents = [line.strip() for line in f.readlines() if line.strip()]

msg = EmailMessage()
msg['Subject'] = 'Test python'
msg['From'] = Email_Address
msg.set_content('This is a test email send to the multipal emailS !')

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Email_Address, Email_Password)
        for recipent in recipents:
            msg['To'] = recipent
            smtp.send_message(msg)
            print(f'Email send to {recipent}')
            del msg['To']
except Exception as e:
    print(f'Error {e}')