from .general_part import GeneralPart
import config
import time
from utils.db_init import db_con, cur


class LogInViaSocial(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=config.USER['name']):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        cur.execute("SELECT data FROM test_data WHERE test_name='Logination'; ")
        elem = cur.fetchone()[0]
        # print(elem.get('user_pass'))
        # print(elem.get('user_mail'))
        self.user_email = elem.get('user_mail')
        self.user_password = elem.get('user_pass')

    def __call__(self, *args, **kwargs):
        self.test_google_login()
        self.test_facebook_login()
        self.test_linkedin_login()
        self.test_microsoft_login()

    @classmethod
    def __repr__(cls):
        return 'login_via_social'

    def test_google_login(self):

        self.click_login_or_logout(login_or_logout='LogIn')

        google_login = self.driver.find_elements_by_css_selector(self.get_division_xpath_login_by_google)
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

        # header_name = self.driver.find_elements_by_css_selector(self.get_division_xpath_my_profile)[0].text
        # print(header_name)

        assert self.user_name in self.driver.find_elements_by_css_selector(self.get_division_xpath_my_profile)[0].text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        self.click_login_or_logout(login_or_logout='LogOut')
        time.sleep(3)

    def test_facebook_login(self):

        self.click_login_or_logout(login_or_logout='LogIn')

        facebook_login = self.driver.find_elements_by_css_selector(self.get_division_xpath_login_by_facebook)
        facebook_login[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('email')
        username.send_keys(self.user_email)
        password = self.driver.find_element_by_name('pass')
        password.send_keys(self.user_password)
        form = self.driver.find_element_by_name('login')
        form.submit()

        assert self.user_name in self.driver.find_elements_by_css_selector(self.get_division_xpath_my_profile)[0].text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        self.click_login_or_logout(login_or_logout='LogOut')
        time.sleep(3)

    def test_linkedin_login(self):

        self.click_login_or_logout(login_or_logout='LogIn')

        linkedin_login = self.driver.find_elements_by_css_selector(self.get_division_xpath_login_by_linkedin)
        linkedin_login[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('session_key')
        username.send_keys(self.user_email)
        password = self.driver.find_element_by_id('session_password-oauth2SAuthorizeForm')
        password.send_keys(self.user_password)
        form = self.driver.find_element_by_name('authorize')
        form.submit()
        time.sleep(3)

        assert self.user_name in self.driver.find_elements_by_css_selector(self.get_division_xpath_my_profile)[0].text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        self.click_login_or_logout(login_or_logout='LogOut')
        time.sleep(3)

    def test_microsoft_login(self):

        self.click_login_or_logout(login_or_logout='LogIn')

        microsoft_login = self.driver.find_elements_by_css_selector(self.get_division_xpath_login_by_microsoft)
        microsoft_login[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('loginfmt')
        username.send_keys(self.user_email)
        password = self.driver.find_element_by_name('passwd')
        password.send_keys(self.user_password)
        form = self.driver.find_element_by_name('SI')
        form.submit()

        assert self.user_name in self.driver.find_elements_by_css_selector(self.get_division_xpath_my_profile)[0].text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        self.click_login_or_logout(login_or_logout='LogOut')
        time.sleep(3)

