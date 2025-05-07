# condition to validate email adress
# a-z
# 0-9
# . _ time 1
# @ time 1
# . on 2nd or 3rd position






import re
email_condition = r"^[a-z0-9]+[\._]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,3}$"
user_email=input("Enter your email address: ");


if re.search(email_condition,user_email):
    print("Valid email address")
else:
    print("Invalid email address")