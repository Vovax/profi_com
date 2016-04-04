import secret_data
import sys


PROFIREADER_URL = 'http://profireader.com'
WINDOW_SIZE = dict(PC=(1920, 1080),
                   PHONE=(500, 300))
MAIL_GMAIL = secret_data.MAIL_USERNAME
MAIL_PWD = secret_data.MAIL_PASSWORD

LOG_IN = {'name': secret_data.LOG_IN_NAME}
#           'mail': secret_data.LOG_IN_MAIL,
#           'pass': secret_data.LOG_IN_PASSWORD}
#

USER = {'name': secret_data.PROFI_USER_NAME}
#         'mail': secret_data.PROFI_USER_MAIL,
#         'pass': secret_data.PROFI_USER_PASSWORD}
#
# PROFIREADER_NAME = secret_data.PROFI_USER_NAME
# PROFIREADER_MAIL = secret_data.PROFI_USER_MAIL
# PROFIREADER_PASSWORD = secret_data.PROFI_USER_PASSWORD

CONFIRM = {'email': secret_data.SQUIRREL_EMAIL,
           'name': secret_data.SQUIRREL_NAME,
           'pass': secret_data.SQUIRREL_PASS}

SQUIRREL_FRAME = 'https://mail.ntaxa.com/src/right_main.php'

MAIL_LOGIN = 'https://accounts.google.com/login#identifier'
MAIL_INBOX = 'https://mail.google.com/mail/u/0/'
COMPANY_LIST = 'http://profireader.com/company/'
