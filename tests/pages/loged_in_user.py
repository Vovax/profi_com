from .general import General
# from .general_part import GeneralPart
import config
import time


class Loged_in_user(General):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=config.LOG_IN['name'],
                 user_mail=config.LOG_IN['mail'], user_pass=config.LOG_IN['pass']):
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        self.user_mail = user_mail
        self.user_pass = user_pass
        super().__init__(device=self.device, driver=self.driver, testing_page=self.testing_page)

    # def __call__(self, *args, **kwargs):
    #     self.get_loged_in_user()
    #
    # @classmethod
    # def __repr__(cls):
    #     return 'loged_in_user'

    def get_loged_in_user(self):
        self.driver.get(config.PROFIREADER_URL)

        log_in = self.driver.find_elements_by_xpath("//div[@class='container']/div[@class='row']/\
        div[@class='col-lg-8 col-md-8 col-sm-8 col-xs-12 menu-site']/div[@id='bs-example-navbar-collapse-1']/ul/li\
                                                                [@class='menu-profile']/a[@class='login-profile']")
        log_in[0].click()
        # self.driver.find_elements_by_xpath(self.get_division_xpath_log_in)[0].click()
        username = self.driver.find_element_by_id('email')
        username.send_keys(self.user_mail)
        password = self.driver.find_element_by_id('password')
        password.send_keys(self.user_pass)
        form = self.driver.find_element_by_id('submit_login')
        form.submit()

        # loged_in =

