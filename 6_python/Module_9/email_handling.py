
' Email Handling'




# import smtplib

# s = smtplib.SMTP("smtp.gmail.com",587)
# s.starttls()

# s.login('jasilmuhammed25@gmail.com','nrna bdij rdge bbdr')
# msg = "This is a testing Mail"

# s.sendmail('jasilmuhammed25@gmail.com','muhjasil974@gmail.com',msg)
# s.quit()








'......................................................'

'HTML contents '



import smtplib
from email.mime.text import MIMEText

sender_email = 'jasilmuhammed25@gmail.com'

app_password = 'nrna bdij rdge bbdr'

reciever_email = 'muhjasil974@gmail.com'


Html = html = " <h2 style='color: blue;background-color: pink;'> Hello Welcome Jasil...</h2><br> <p style='color: green; background-color: lightgray;'> You are hired......</p>"

message = MIMEText(Html, "html")
message ["Subject"] = "Greeting"
message ['From'] = sender_email
message ['To'] = reciever_email

with smtplib.SMTP("smtp.gmail.com", 587)as server:
    server.starttls()
    server.login(sender_email,app_password)
    server.send_message(message)

print('successfull')