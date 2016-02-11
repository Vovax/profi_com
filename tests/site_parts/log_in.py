from .general_part import GeneralPart
import config
import time


class Log_in (GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_log_in()

    @classmethod
    def __repr__(cls):
        return 'log_in'

    def test_log_in(self):
        # print(self.get_division_xpath_log_in)
        # login_tag.send_keys(Keys.RETURN)
            # a_length = 1
            # count = 0
        login_tag = self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)
            # a_length = len(login_tag) if count == 0 else a_length
            # print(login_tag)
            # count += 1
        login_tag[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('email')
        username.send_keys('bravegirlua@yahoo.com')
        time.sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys('!')
        time.sleep(2)
        form = self.driver.find_element_by_id('submit_login')
        form.submit()
