# '''
# Birthday Email Sender
# -------------------------------------------------------------
# pip install pandas openpyxl
# excel file cols:
# Name, Email, Birthday (MM/DD/YYYY), Last Sent (YYYY)
# '''


# import pandas as pd
# from datetime import datetime
# import smtplib
# from email.message import EmailMessage


# def send_email(recipient, subject, msg):
#     GMAIL_ID = 'your_email_here'
#     GMAIL_PWD = 'your_password_here'

#     email = EmailMessage()
#     email['Subject'] = subject
#     email['From'] = GMAIL_ID
#     email['To'] = recipient
#     email.set_content(msg)

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_obj:
#         gmail_obj.ehlo()
#         gmail_obj.login(GMAIL_ID, GMAIL_PWD)
#         gmail_obj.send_message(email)
#     print('Email sent to ' + str(recipient) + ' with Subject: \''
#           + str(subject) + '\' and Message: \'' + str(msg) + '\'')


# def send_bday_emails(bday_file):
#     bdays_df = pd.read_excel(bday_file)
#     today = datetime.now().strftime('%m-%d')
#     year_now = datetime.now().strftime('%Y')
#     sent_index = []

#     for idx, item in bdays_df.iterrows():
#         bday = item['Birthday'].to_pydatetime().strftime('%m-%d')
#         if (today == bday) and year_now not in str(item['Last Sent']):
#             msg = 'Happy Birthday ' + str(item['Name'] + '!!')
#             send_email(item['Email'], 'Happy Birthday', msg)
#             sent_index.append(idx)

#     for idx in sent_index:
#         bdays_df.loc[bdays_df.index[idx], 'Last Sent'] = str(year_now)

#     bdays_df.to_excel(bday_file, index=False)


# if __name__ == '__main__':
#     send_bday_emails(bday_file='your_bdays_list.xlsx')
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
import smtplib
import datetime

# Email configuration
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@example.com"
SENDER_PASSWORD = "your_password"

# List of recipients with their birthdays
birthdays = {
    "John": "1990-05-15",
    "Jane": "1988-12-10",
    "David": "1995-03-22"
}


def send_birthday_email(name, recipient_email):
    subject = f"Happy Birthday, {name}!"
    body = f"Dear {name},\n\nWishing you a very happy birthday! May all your dreams come true.\n\nBest regards,\nYour Name"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, message)


# Get the current date
today = datetime.date.today().strftime("%Y-%m-%d")

# Check if any birthdays match the current date
for name, birthday in birthdays.items():
    if birthday == today:
        # Replace with the recipient's email address
        recipient_email = "recipient_email@example.com"
        send_birthday_email(name, recipient_email)
        print(f"Sent birthday email to {name} at {recipient_email}")
