from .general_part import GeneralPart
import config
import time
from utils.db_init import db_con, cur



class Log_in (GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=config.LOG_IN['name']):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        # self.user_name = user_name
        cur.execute("SELECT data FROM test_data WHERE test_name='LogedIn'; ")
        elem = cur.fetchone()[0]
        # print(elem.get('user_pass'))
        # print(elem.get('user_mail'))
        self.user_email = elem.get('user_mail')
        self.user_password = elem.get('user_pass')


    def __call__(self, *args, **kwargs):
        self.test_log_in()

    @classmethod
    def __repr__(cls):
        return 'log_in'

    def test_log_in(self):

        login_tag = self.driver.find_elements_by_css_selector(self.get_division_xpath_log_in)
        login_tag[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('email')
        username.send_keys(self.user_email)
        time.sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.user_password)
        time.sleep(2)
        form = self.driver.find_element_by_class_name('submit-form')
        form.submit()

        logedIn = self.driver.find_elements_by_css_selector("*[pr_test='LogOut']")[0].text
        # print(logedIn)

        assert 'Log out' == logedIn, "Can't Log In"

        # assert self.user_name in self.driver.find_element_by_xpath(self.get_division_xpath_drop_menu).text,\
        #     'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)

