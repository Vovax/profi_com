from .general_part import GeneralPart
import config
import time
from utils.db_init import db_con, cur



class Log_in (GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=config.LOG_IN['name']):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        cur.execute("SELECT data FROM test_data WHERE test_name='LogedIn'; ")
        elem = cur.fetchone()[0]
        print(elem.get('password'))
        print(elem.get('email'))
        self.user_email = elem.get('email')
        self.user_password = elem.get('password')


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
        login_tag = self.driver.find_elements_by_css_selector(self.get_division_xpath_log_in)
            # a_length = len(login_tag) if count == 0 else a_length
            # print(login_tag)
            # count += 1
        login_tag[0].click()
        time.sleep(2)
        username = self.driver.find_element_by_name('email')
        username.send_keys(self.user_email)
        time.sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.user_password)
        time.sleep(2)
        form = self.driver.find_element_by_id('submit_login')
        form.submit()

        assert self.user_name in self.driver.find_element_by_xpath(self.get_division_xpath_drop_menu).text,\
            'Can"t find {user}, in {page}'.format(user=self.user_name, page=self.driver.current_url)
