import pandas, random, smtplib
import datetime as dt

MYEMAIL = "CCCCCCCCCCC"
MYPW = "XXXXXXXXX"
##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
today = dt.datetime.now()
today_tuple = (today.month, today.day)
file = pandas.read_csv("birthdays.csv")
new_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in file.iterrows()}
# print(new_dict)


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
if today_tuple in new_dict:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    # HINT: https://www.w3schools.com/python/ref_string_replace.asp
    birthday_person = new_dict[today_tuple]
    num = random.randrange(1,3)
    with open(f"letter_templates/letter_{num}.txt")as ltr:
        ltr_file = ltr.read()
        wish = ltr_file.replace("[NAME]", birthday_person["name"])
    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(MYEMAIL, MYPW)
        connection.sendmail(from_addr=MYEMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday \n\n {wish}")







