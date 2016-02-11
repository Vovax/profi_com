from .pages.index import IndexPage
from utils.email import SendEmail
from .pages.division import Division
import config
from selenium.webdriver import Firefox


def start_test(device):
    send_email = SendEmail().send_email
    testing_page = config.PROFIREADER_URL
    driver = Firefox()

    try:
        IndexPage(device=device, driver=driver)
        Division(device=device, driver=driver)
    except AssertionError as e:
        send_email(exception=e)
