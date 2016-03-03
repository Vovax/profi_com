import argparse
from tests.pages.index import IndexPage
from utils.email import SendEmail
from tests.pages.division import Division
import config
from selenium.webdriver import Firefox
from tests.pages.loged_in_user import Loged_in_user
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

parser = argparse.ArgumentParser(description='Test for profireader')
parser.add_argument("site")
parser.add_argument("device")
args = parser.parse_args()


def start_test(device):
    send_email = SendEmail().send_email
    testing_page = config.PROFIREADER_URL
    driver = Firefox(capabilities=DesiredCapabilities.FIREFOX)

    try:
        IndexPage(device=device, driver=driver)
        Division(device=device, driver=driver)
        Loged_in_user(device=device, driver=driver)
    except AssertionError as e:
        send_email(exception=e)


if __name__ == '__main__':
    if 'profireader' in args.site:
        # print(args.device.split("'"))
        start_test(device=args.device.split("'")[-2])
