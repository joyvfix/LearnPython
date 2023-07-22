import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Set up the email server
        smtp_server = "smtp.gmail.com"
        port = 587
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()

        # Log in to the email server
        server.login(sender_email, sender_password)

        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Quit the server
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred while sending the email:", str(e))


# Example usage
sender_email = "your_email@gmail.com"
sender_password = "your_email_password"
recipient_email = "recipient_email@example.com"
subject = "Test Email"
message = "This is a test email sent from Python."

send_email(sender_email, sender_password, recipient_email, subject, message)
