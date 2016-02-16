from .general_part import GeneralPart
import config
import time



class Login_by_google(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=config.USER['name'],
                 user_email=config.USER['mail'], user_password=config.USER['pass']):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def __call__(self, *args, **kwargs):
        self.test_login_by_google()

    @classmethod
    def __repr__(cls):
        return 'login_by_google'


    def test_login_by_google(self):

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

        # print(self.driver.page_source)
        # print(self.driver.current_url)
        # print(self.get_division_xpath_drop_menu)

        assert self.user_name in self.driver.find_element_by_xpath(self.get_division_xpath_drop_menu).text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

        # self.get_division_xpath_drop_menu.get_attribute('text')
        # drop_menu = self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)
        # drop_menu[0].click()
        # self.click_my_profile_or_logout(profile_or_logout='logout')
        # time.sleep(2)


