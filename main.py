import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


def send_email(email_recipient,
               email_subject,
               email_message,
               attachment_location = ''):
    
    """ Essa função cria a mensagem e depois conecta no servidor
    com o login e senha para enviar o e-mail."""

    email_sender = 'seu_email@exemplo.com'

    # Essa parte cria a mensagem
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message, 'plain'))

    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)


    # Essa parte faz a conexão com o servidor e envia o email.
    try:
        server = smtplib.SMTP('smtp.outlook.com', 25)
        server.ehlo()
        server.starttls()
        try:
            # Tenta fazer o login no servidor smtp.outlook.com
            server.login('login', 'senha') # ==== > login e senha coloca nessa parte
        except smtplib.SMTPException as e:
            print('SMTP error occurred: ' + str(e))
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True

send_email('email_destinatário@exemplo.com',
           'Funcionou?',
           'Texto texto texto')