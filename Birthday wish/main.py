import pandas
import random
import smtplib as smtp
import datetime as dt

mon = dt.datetime.now().month
day = dt.datetime.now().day
tup = (mon, day)

datas = pandas.read_csv("birthdays.csv")
birthday = {(data_r["month"], data_r["day"]): data_r for (index, data_r) in datas.iterrows()}
print(birthday)
if tup in birthday:
    file_path = f"letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        birthday_person = birthday[tup]
        content = letter.read()
        ss = content.replace("[NAME]", birthday_person["name"])
        go = ss.replace("Angela", "you can change your name")

    my_mail = YOUR_MAIL
    password = YOUR_PASSKEY
    connection = smtp.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail, to_addrs=birthday_person.email, msg=f"Subject: summa\n\n{go}")
    connection.close()



