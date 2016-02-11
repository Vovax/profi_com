import config
import smtplib
from email.mime.text import MIMEText
import sys
import traceback


class SendEmail:
    def __init__(self, username=config.MAIL_GMAIL, password=config.MAIL_PWD,
                 send_to=None):
        self.username = username
        self.password = password
        self.send_to = send_to or [config.MAIL_GMAIL]
        self.send_email()

    def send_email(self, subject='Test Error', text='Test Error', exception=None):

        if exception:
            _, _, tb = sys.exc_info()
            traceback.print_tb(tb)
            tb_info = traceback.extract_tb(tb)
            filename_, line_, func_, text_ = tb_info[-1]
            message = 'An error occurred on File "{file}" line {line}\n {assert_message}'.format(
                line=line_, assert_message=exception.args, file=filename_)
            print(message)
            text = message
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = ','.join(self.send_to)
        server = smtplib.SMTP('smtp.gmail.com:587')

        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.username, self.send_to, msg.as_string())
        server.quit()
