

# import smtplib
# from email.mime.text import MIMEText

# sender_email = 'jasilmuhammed25@gmail.com'

# app_password = 'nrna bdij rdge bbdr'

# reciever_email = 'muhjasil974@gmail.com'


# Html = ' '

# message = MIMEText(Html, "html")
# message ["Subject"] = "Greeting"
# message ['From'] = sender_email
# message ['To'] = reciever_email

# with smtplib.SMTP("smtp.gmail.com", 587)as server:
#     server.starttls()
#     server.login(sender_email,app_password)
#     server.send_message(message)

# print('Email sent successfull ✅')




'----------------------------------------------------------------------------'


import smtplib
from email.mime.text import MIMEText

sender_email = 'jasilmuhammed25@gmail.com'

app_password = 'nrna bdij rdge bbdr'

reciever_email = 'muhjasil974@gmail.com'

html = "<h2>Hello!</h2><p>Python Loop Email</p>"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, app_password)

    for i in range(5):
        message = MIMEText(html, "html")
        message["Subject"] = f"helo {i+1}"
        message["From"] = sender_email
        message["To"] = reciever_email

        server.send_message(message)
        print(f"Email {i+1} sent ✅")

print("Done!")