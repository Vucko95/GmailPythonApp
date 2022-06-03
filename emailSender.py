import os
from re import sub
import yagmail
from dotenv import load_dotenv
load_dotenv()


sender = os.environ.get('email')
reciver = os.environ.get('remail')
email_password = os.environ.get('email_pass')
subject = "This is a test"
contets = " TestTESTSTST"
# yagmail.register(user=sender, password=email_password)
yag = yagmail.SMTP(user=sender, password=email_password)
yag.send(to=reciver, subject=subject, contents=contets)
print("Email Sent")
