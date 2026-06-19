
# # import smtplib
# # from email.mime.text import MIMEText
# # from random import*

# # sender = 'jasilmuhammed25@gmail.com'
# # password = 'nrna bdij rdge bbdr'
# # reciever = 'rishanafathim22@gmail.com'

# # num = randint(1,999999)
# # otp = f'{num:06d}'


# # Html = f"""
# #     <div style="font-family: Arial, sans-serif; text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea, #764ba2);color: rgb(255, 255, 255)">
# #         <p>
# #         Dear User,<br>
# #         Your One-Time Password (OTP) is : <br><br>

# #          {otp} <span>

        
# #         Please use this OTP to complete your login process. Do not share this code with anyone.<br>
# #         Thank you for using Email OTP!</p>

# #     </div>
# # """



# '.....................................'




# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr

# sender = "jasilmuhammed25@gmail.com"
# password = "nrna bdij rdge bbdr"
# receiver = "muhjasil974@gmail.com"

# message = MIMEText("Congratulations! You are hired.", "plain")

# message["Subject"] = "Congratulations!"
# message["From"] = formataddr(("HR Team", sender))
# message["To"] = receiver

# with smtplib.SMTP("smtp.gmail.com", 587) as server:
#     server.starttls()
#     server.login(sender, password)
#     server.send_message(message)

# print("Email sent successfully ✅")



