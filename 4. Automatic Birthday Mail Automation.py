
# //! Automatic Birthday Wish Email Automation

import os
from dotenv import load_dotenv

load_dotenv()

import smtplib # module to send emails using SMTP


from email.mime.text import MIMEText # to format dynamic messages and to create properly formatted email messages with subject, body, etc..

# Next step is to make a sender ( a variable from which mail id the emails will be sent )
sender = os.getenv("GMAIL_ADDRESS")


# //! Need to create an app password
# go to your google account 
# then manage accounts
# then search for app password and enter the app name and copy the 16 character code here

password = os.getenv("GMAIL_APP_PASSWORD")


# Mail and Name of the Receivers
receiver = input("Enter your email: ")
name = input("Enter your name: ")


# Create the body of the email with dynamic (name, email) and normal data (body / content)
msg = MIMEText (f"🎂💐🥳Happy Birthday {name} Nigga🎉🎈🎁 \nHave a great day ahead")


# Set the subject of the email
msg['Subject'] = "Happy Birthday Bish 🎂💐🥳"


# Set the "from" email address in the email header
msg['From'] = sender


# Set the "to" email address in the email header
msg['To'] = receiver


# Connect securely to Gmail server using the SSL and port 465
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)


# Logs in to the Gmail server using sender's email and app password
server.login(sender, password)


# Sends the constructed message to the receiver
server.send_message(msg)


# Quit the server
server.quit()


print("Email sent successfully!")