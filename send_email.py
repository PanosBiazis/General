import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define email sender and receiver
sender_email = ""
receiver_email = ""
password = ""  # Ensure it's secure!

# Create the email message
subject = "Your Subject Here"
body = "Your email body description goes here."

# Create the MIMEText object and attach subject, sender, and receiver
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Set up the SMTP server for Gmail
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
