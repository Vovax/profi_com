from config import PROFIREADER_URL, WINDOW_SIZE
from utils.email import SendEmail
from ..site_parts.log_in import Log_in
from ..site_parts.logination import Logination
# from tests.pages.loged_in_user import Loged_in_user
from ..site_parts.subscriptions import Subscriptions
from ..site_parts.news import News
from ..site_parts.my_profile import My_profile
from ..site_parts.help_page import Help_page


class General(object):

    dependences = ('logination', 'log_in', 'my_profile', 'subscriptions', 'news', 'help_page', 'loged_in_user', 'header')

    def __init__(self, dependences=dependences, driver=None, device='PC', testing_page=PROFIREADER_URL):
        # print('general')
        self.device = device
        self.driver = driver
        self.testing_page = testing_page
        self.send_email = SendEmail().send_email
        self.call_dependences(dependences)

    def set_config(self):
        window_size = WINDOW_SIZE[self.device]
        self.driver.set_window_size(*window_size)
        self.driver.get(self.testing_page)
        self.driver.implicitly_wait(3)

    def call_dependences(self, dependences):
        classes = (Log_in, My_profile, Subscriptions, News, Help_page)

        [a() for a in map(lambda cls: cls(driver=self.driver),
                          filter(lambda cls: cls.__repr__() in dependences, classes))]
