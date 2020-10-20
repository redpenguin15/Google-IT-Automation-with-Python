import smtplib
import  os.path
import mimetypes
import email.message
from email.message import EmailMessage



def generate_email(sender, recipient, subject, body, attachment_path = None):
    message = email.message.EmailMessage()
    message["From"]= sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path != None:
        attachment_name = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/',1)
        with open(attachment_path,'rb') as f:
            message.add_attachment(f.read(),
                                   maintype = mime_type,
                                   subtype = mime_subtype,
                                   filename = os.path.basename(attachment_path)
                                   )

    return message


def send_email():
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(package)
    mail_server.quit()