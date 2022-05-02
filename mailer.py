import smtplib
from email.message import EmailMessage
from credentials import OVH_SMTP_ADDRESS, OVH_SMTP_PORT, OVH_EMAIL_ADDRESS, OVH_EMAIL_PASSWORD

def mail(sender: str, receiver: str, subject: str, message: str) -> None:
   msg = EmailMessage()
   msg['Subject'] = subject
   msg['From'] = sender
   msg['To'] = receiver
   msg.set_content(message, subtype='html')

   with smtplib.SMTP_SSL(OVH_SMTP_ADDRESS, OVH_SMTP_PORT) as smtp:
      smtp.login(OVH_EMAIL_ADDRESS, OVH_EMAIL_PASSWORD)
      smtp.send_message(msg)
