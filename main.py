from datetime import datetime as dt
import smtplib
import random 
import pandas as pd

EMAIL = "Your Email"
PASSWORD = "Your Password"

now = dt.now()
now_t = (now.month,now.day)

data = pd.read_csv("projects/smtp/wish.csv")
birthday = {(birth["month"],birth["day"]) : birth for (index,birth) in data.iterrows()}
if now_t in birthday:
    person = birthday[now_t]
    file = f"projects/smtp/letter{random.randint(1,3)}.txt"
    with open(file) as letter:
        info = letter.read()
        info = info.replace("[NAME]",person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=EMAIL, password=PASSWORD)
        connect.sendmail(from_addr=EMAIL,to_addrs=person["email"],msg=f"Subject : HAPPY BIRTHDAY! \n\n {info}")

