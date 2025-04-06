import smtplib
import speech_recognition as sr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = ""
    receiver_email = ""
    password = "password"  # Make sure this is stored securely!

    subject = "Your Subject Here"
    body = "Your email body description goes here."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for the phrase: 'send email'...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {command}")
            if "send email" in command:
                send_email()
            else:
                print("Command not recognized.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("Speech recognition service is down.")

if __name__ == '__main__':
    recognize_voice()
