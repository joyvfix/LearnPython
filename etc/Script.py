# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# def send_email(sender, recipient, subject, message, smtp_server, smtp_port, username, password):
#     # Create message container
#     msg = MIMEMultipart()
#     msg['From'] = sender
#     msg['To'] = recipient
#     msg['Subject'] = subject

#     # Attach message to the container
#     msg.attach(MIMEText(message, 'plain'))

#     # Connect to SMTP server and send email
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()
#         server.login(username, password)
#         server.send_message(msg)

#     print("Email sent successfully.")


# # Usage example
# send_email(
#     sender='sender@example.com',
#     recipient='recipient@example.com',
#     subject='Hello',
#     message='This is a test email.',
#     smtp_server='smtp.example.com',
#     smtp_port=587,
#     username='your_username',
#     password='your_password'
# )
# ('''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''')
from PIL import Image
import os


def resize_images(input_dir, output_dir, size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = os.listdir(input_dir)

    for file in files:
        if file.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(input_dir, file)
            image = Image.open(image_path)
            resized_image = image.resize(size)
            output_path = os.path.join(output_dir, file)
            resized_image.save(output_path)

    print("Image resizing completed.")


# Usage example
resize_images("input_directory", "output_directory", (800, 600))


def generate_fibonacci_sequence(length):
    sequence = [0, 1]

    if length <= 2:
        return sequence[:length]

    while len(sequence) < length:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


# Usage example
fibonacci_sequence = generate_fibonacci_sequence(10)
print(fibonacci_sequence)
