from .general_part import GeneralPart
import random as rand
import config
import time


class Logination(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=config.USER['name'],
                 user_email=config.USER['mail'], user_password=config.USER['pass']):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def __call__(self, *args, **kwargs):
        self.test_logination(random=False)

    @classmethod
    def __repr__(cls):
        return 'logination'


    def test_logination(self, random=False):

        # GOOGLE
        self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)[0].click()
        google_login = self.driver.find_elements_by_xpath(self.get_division_xpath_login_by_google)
        google_login[0].click()
        time.sleep(2)
        useremail = self.driver.find_element_by_name('Email')
        useremail.send_keys(self.user_email)
        form = self.driver.find_element_by_id('signIn')
        form.submit()
        password = self.driver.find_element_by_name('Passwd')
        password.send_keys(self.user_password)
        form = self.driver.find_element_by_id('signIn')
        form.submit()

        assert self.user_name in self.driver.find_element_by_xpath(self.get_division_xpath_drop_menu).text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)[0].click()
        time.sleep(3)
        self.click_my_profile_or_logout(profile_or_logout='logout')
        time.sleep(3)

        # FACEBOOK
        self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)[0].click()
        facebook_login = self.driver.find_elements_by_xpath(self.get_division_xpath_login_by_facebook)
        facebook_login[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('email')
        username.send_keys(self.user_email)
        password = self.driver.find_element_by_name('pass')
        password.send_keys(self.user_password)
        form = self.driver.find_element_by_name('login')
        form.submit()

        assert self.user_name in self.driver.find_element_by_xpath(self.get_division_xpath_drop_menu).text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)[0].click()
        time.sleep(3)
        self.click_my_profile_or_logout(profile_or_logout='logout')
        time.sleep(3)

        # LINKEDIN
        self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)[0].click()
        linkedin_login = self.driver.find_elements_by_xpath(self.get_division_xpath_login_by_linkedin)
        linkedin_login[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('session_key')
        username.send_keys(self.user_email)
        password = self.driver.find_element_by_id('session_password-oauth2SAuthorizeForm')
        password.send_keys(self.user_password)
        form = self.driver.find_element_by_name('authorize')
        form.submit()

        assert self.user_name in self.driver.find_element_by_xpath(self.get_division_xpath_drop_menu).text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)[0].click()
        time.sleep(3)
        self.click_my_profile_or_logout(profile_or_logout='logout')
        time.sleep(3)

        # MICROSOFT
        self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)[0].click()
        microsoft_login = self.driver.find_elements_by_xpath(self.get_division_xpath_login_by_microsoft)
        microsoft_login[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('loginfmt')
        username.send_keys(self.user_email)
        password = self.driver.find_element_by_name('passwd')
        password.send_keys(self.user_password)
        form = self.driver.find_element_by_name('SI')
        form.submit()

        assert self.user_name in self.driver.find_element_by_xpath(self.get_division_xpath_drop_menu).text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)[0].click()
        time.sleep(3)

        self.click_my_profile_or_logout(profile_or_logout='logout')
        time.sleep(3)

