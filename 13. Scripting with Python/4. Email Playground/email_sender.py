import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Dev Kumar Sen"
email["to"] = "devsen.358382@gmail.com"
email["subject"] = "Testing mail!"

email.set_content("Hii there, this is just the python scripting email")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("devksen.personal@gmail.com", "testingpass@123")
    smtp.send_message(email)
    print("Email sent successfully")
