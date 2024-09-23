# Code to reconnect through another instance with email verification

import os
import subprocess
import smtplib
from email.mime.text import MIMEText

# Function to send verification email

def send_verification_email(email):
    msg = MIMEText('Please verify your email for SSH access.')
    msg['Subject'] = 'Email Verification'
    msg['From'] = 'your_email@example.com'
    msg['To'] = email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_email_password')
        server.send_message(msg)

# Function to reconnect to the server

def reconnect_to_server(user='formidablepencil', host='your_host', port=22, encryption_key='your_encryption_key', email='your_email@example.com'):
    send_verification_email(email)
    # Command to connect to the server
    command = f'ssh -i {encryption_key} {user}@{host} -p {port}'
    os.system(command)  # Execute the command

if __name__ == '__main__':
    reconnect_to_server()