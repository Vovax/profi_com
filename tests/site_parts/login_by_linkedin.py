from .general_part import GeneralPart
import config
import time


class Login_by_linkedin(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_login_by_linkedin()

    @classmethod
    def __repr__(cls):
        return 'login_by_linkedin'


    def test_login_by_linkedin(self):

        self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)[0].click()
        linkedin_login = self.driver.find_elements_by_xpath(self.get_division_xpath_login_by_linkedin)
        linkedin_login[0].click()
        time.sleep(2)

        username = self.driver.find_element_by_name('session_key')
        username.send_keys('profireader.service@gmail.com')
        password = self.driver.find_element_by_name('session_password')
        password.send_keys('f8ne0Yy@fF^ixy')
        form = self.driver.find_element_by_name('authorize')
        form.submit()

