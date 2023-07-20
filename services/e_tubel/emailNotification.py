from schema.e-tubel.EmailNotifSchema import EmailNotificationSchema
from models.e-tubel.EmailNotification import EmailNotification
from app import db
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailNotificationService:
    @staticmethod
    def manual_send(schema:EmailNotificationSchema):
        email_notif=EmailNotification(
            email_notif_from=schema['email_notif_from'],
            email_notif_to=schema['email_notif_to'],
            email_notif_body=schema['email_notif_body'],
            email_notif_isRead=0
        )
        db.session.add(email_notif)
        db.session.commit()
        return email_notif
    
    def send_to_email(sender_email, receiver_emails, subject, body, password):
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ', '.join(receiver_emails)
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()

        # Log in to your account
        smtp_connection.login(sender_email, password)

        # Send the email
        smtp_connection.sendmail(sender_email, receiver_emails, message.as_string())

        # Close the SMTP connection
        smtp_connection.quit()