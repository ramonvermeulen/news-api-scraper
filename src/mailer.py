import smtplib


class Mailer:
    def __init__(self, sender_mail, sender_password, smtp_server_address='smtp.gmail.com', smtp_port=587):
        self.sender_mail = sender_mail
        self.sender_password = sender_password
        self.smtp_server_address = smtp_server_address
        self.smtp_port = smtp_port

    def send_mail(self, recipients, subject, body):
        server = smtplib.SMTP(self.smtp_server_address, self.smtp_port)
        server.ehlo()
        server.starttls()
        server.login(self.sender_mail, self.sender_password)
        try:
            body = '\r\n'.join(['To: %s' % recipients,
                                'From: %s' % self.sender_mail,
                                'Subject: %s' % subject,
                                '', body])
            server.sendmail(self.sender_mail, recipients, body)
            print('email sent')
        except Exception as e:
            print('error sending mail')
            print(e)
