import random
import smtplib
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("siddharthkadu2001@gmail.com", "qkjwtopzuwysroij")
random_no=random.randint(11111,999999)
message="Your OTP is:"+ str(random_no)
server.sendmail("siddharthkadu2001@gmail.com", "chambhare007@gmail.com", message)
server.close()
