
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



# import smtplib
# from email.mime.text import MIMEText

# sender_email = 'jasilmuhammed25@gmail.com'

# app_password = 'nrna bdij rdge bbdr'

# reciever_email = 'muhjasil974@gmail.com'


# Html = """
# <div style="font-family: Arial, sans-serif; text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea, #764ba2);">
    
#     <h1 style="color: white; margin-bottom: 20px;">
#         🎉 Congratulations Jasil!
#     </h1>
    
#     <div style="background-color: white; padding: 25px; border-radius: 15px; max-width: 500px; margin: auto;">
        
#         <h2 style="color: #4f46e5;">
#             Welcome to the Team 🚀
#         </h2>
        
#         <p style="color: #555; font-size: 18px; line-height: 1.6;">
#             We are excited to inform you that you have been selected.
#             Your skills and dedication have impressed us.
#         </p>
        
#         <p style="color: #16a34a; font-size: 22px; font-weight: bold;">
#             ✅ You Are Hired!
#         </p>
        
#         <p style="color: #777;">
#             We look forward to working with you.
#         </p>
        
#     </div>
# </div>
# """
# message = MIMEText(Html, "html")
# message ["Subject"] = "Greeting"
# message ['From'] = sender_email
# message ['To'] = reciever_email

# with smtplib.SMTP("smtp.gmail.com", 587)as server:
#     server.starttls()
#     server.login(sender_email,app_password)
#     server.send_message(message)

# print('Email sent successfull ✅')











'...................Attachment sending ...........................'





import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


sender = "jasilmuhammed25@gmail.com"
password = "nrna bdij rdge bbdr"
reciever = "muhjasil974@gmail.com"

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = reciever
msg['Subject'] = 'Test email with attachment'


Html =  """
    

    
    <div style="background-color: white; padding: 25px; border-radius: 10px; max-width: 500px; margin: auto;">
        
        <h2 style="color: #4f46e5;">
            This is test mail 🚀
        </h2>
        
        <p style="color: #555; font-size: 18px; line-height: 1.6;">
            This mail contain an attachment
        </p>
        
    </div>
"""

msg.attach(MIMEText(Html,"html"))

file_path = r"C:\Users\jasil\Documents\Quest\6_python\Module_9\portugal.avif"
file_name ="portugal.avif"


try:
    with open(file_path,'rb')as attachment:
        mime = MIMEBase('application','octet-stream')

        mime.set_payload(attachment.read())

        encoders.encode_base64(mime)

        mime.add_header("Content-Disposition",f"attachment; filename={file_name}")

        msg.attach(mime)

except Exception as e:
    print(f"An Excepation Occured {e}")



try:
    with smtplib.SMTP("smtp.gmail.com",587)as server:
        server.starttls()
        server.login(sender,password)
        server.send_message(msg)
    print("Message sent successfully")
except Exception as e:
    print("an exception occured")
