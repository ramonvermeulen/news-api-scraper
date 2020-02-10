import smtplib
import logging
import datetime
import sys


class Mailer:
    def __init__(self, sender_mail, sender_password, smtp_server_address='smtp.gmail.com', smtp_port=587):
        self.sender_mail = sender_mail
        self.sender_password = sender_password
        self.smtp_server_address = smtp_server_address
        self.smtp_port = smtp_port
        self._setup_logger()

    @staticmethod
    def _setup_logger():
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

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
            logging.info(f'[{datetime.datetime.now()}] - Email send to {recipients}')
        except Exception as e:
            logging.exception(f'[{datetime.datetime.now()}] - Error occurred while trying to send Email')
