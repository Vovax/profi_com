from .general_part import GeneralPart
import config
import time


class Login_by_social(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_login_by_social()

    @classmethod
    def __repr__(cls):
        return 'login_by_social'


    def test_login_by_social(self):

        self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)[0].click()
        google_login = self.driver.find_elements_by_xpath(self.get_division_xpath_login_by_social)
        google_login[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('Email')
        username.send_keys('profireader.service')
        form = self.driver.find_element_by_id('signIn')
        form.submit()
        password = self.driver.find_element_by_name('Passwd')
        password.send_keys('f8ne0Yy@fF^ixy')
        form = self.driver.find_element_by_id('signIn')
        form.submit()
        # drop_menu = self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)
        # drop_menu[0].click()
        # self.click_my_profile_or_logout(profile_or_logout='logout')
        # time.sleep(2)


