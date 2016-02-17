from config import PROFIREADER_URL, WINDOW_SIZE
from utils.email import SendEmail
from ..site_parts.log_in import Log_in
from ..site_parts.header import Header
from ..site_parts.log_out import Log_out
from ..site_parts.drop_menu import Drop_menu
from ..site_parts.my_profile import My_profile
from ..site_parts.login_by_google import Login_by_google
from ..site_parts.login_by_facebook import Login_by_facebook
from ..site_parts.login_by_linkedin import Login_by_linkedin
from ..site_parts.login_by_microsoft import Login_by_microsoft
from ..site_parts.logination import Logination


class General(object):

    dependences = ('logination', 'log_in', 'drop_menu', 'my_profile', 'log_out', 'login_by_google', 'login_by_facebook',
                   'login_by_linkedin', 'login_by_microsoft', 'header')

    def __init__(self, dependences=dependences, driver=None, device='PC', testing_page=PROFIREADER_URL):
        print('general')
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
        classes = (Logination, Log_in)


# (Login_by_google, Drop_menu, Log_out, Login_by_facebook, Drop_menu, Log_out, Login_by_linkedin,
#                    Drop_menu, Log_out, Login_by_microsoft, Drop_menu, Log_out, Log_in, Drop_menu, My_profile,
#                    Header, Log_out)
        [a() for a in map(lambda cls: cls(driver=self.driver),
                          filter(lambda cls: cls.__repr__() in dependences, classes))]
