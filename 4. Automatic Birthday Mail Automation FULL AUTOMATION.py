
# //! Automatic Birthday Wish Email Automation

import os
from dotenv import load_dotenv

load_dotenv()


import smtplib # module to send emails using SMTP


from email.mime.text import MIMEText # to format dynamic messages and to create properly formatted email messages with subject, body, etc..

# date and time so that we can send the mail at a particular time and date
from datetime import datetime
import time


# Next step is to make a sender ( a variable from which mail id the emails will be sent )
sender = os.getenv("GMAIL_ADDRESS")


# //! Need to create an app password
# go to your google account 
# then manage accounts
# then search for app password and enter the app name and copy the 16 character code here

password = os.getenv("GMAIL_APP_PASSWORD")


# Mail and Name of the Receivers along with their date of birth
receiver = input("Enter your email: ")
name = input("Enter your name: ")
dob = input("Enter your birthday (dd-mm): ")

# Set the time when you want the email to be sent in 24hr format
send_hour = 11
send_minute = 14

print("Waiting for the correct time to send the wish...")


# Loop to compare the date and time btw the receiver's and sender's
while True:
    now = datetime.now()
    today = now.strftime("%d-%m")  # converts the date into string
    
    
    if dob == today and now.hour == send_hour and now.minute == send_minute: # comparing the user's dob with today's date and the hours and minute
        
        # Create the mail body
        msg = MIMEText (f"🎂💐🥳Happy Birthday {name} Nigga🎉🎈🎁 \nHave a great day ahead")
        msg['Subject'] = "Happy Birthday Bish 🎂💐🥳"
        msg['From'] = sender
        msg['To'] = receiver
        
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.send_message(msg)
            server.quit()
            print("Email sent successfully!")
            
        except Exception as e:
            print("Failed to send the email", e)
        break

    time.sleep(30)
