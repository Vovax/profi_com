from .general import General
# from .general_part import GeneralPart
import config
import time
from utils.db_init import cur



class Loged_in_user(General):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=None,
                 user_mail=None, user_pass=None):
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        cur.execute("SELECT data FROM test_data WHERE test_name='LogedIn'; ")
        elem = cur.fetchone()[0]
        print(elem.get('password'))
        print(elem.get('email'))
        self.user_email = elem.get('email')
        self.user_password = elem.get('password')
        super().__init__(device=self.device, driver=self.driver, testing_page=self.testing_page)

    # def __call__(self, *args, **kwargs):
    #     self.get_loged_in_user()
    #
    # @classmethod
    # def __repr__(cls):
    #     return 'loged_in_user'

    def get_loged_in_user(self):
        self.driver.get(config.PROFIREADER_URL)
        print('loged_in_user')
        log_in = self.driver.find_elements_by_css_selector("*[pr_test='LogIn']")
        log_in[0].click()
        # self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)[0].click()
        username = self.driver.find_element_by_id('email')
        username.send_keys(self.user_email)
        password = self.driver.find_element_by_id('password')
        password.send_keys(self.user_password)
        form = self.driver.find_element_by_id('submit_login')
        print('loged_in_userII')
        form.submit()

        # loged_in =

