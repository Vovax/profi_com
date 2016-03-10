from .general_part import GeneralPart
from selenium.webdriver.common.keys import Keys
import config
import time
from utils.db_init import db_con, cur



class Registration(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=config.USER['name']):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        # cur.execute("SELECT data FROM test_data WHERE test_name='Registration'; ")
        # elem = cur.fetchone()[0]
        # print(elem.get('user_pass'))
        # print(elem.get('user_mail'))
        # self.user_email = elem.get('user_mail')
        # self.user_password = elem.get('user_pass')


    def __call__(self, *args, **kwargs):
        self.test_registration()

    @classmethod
    def __repr__(cls):
        return 'registration'


    def test_registration(self, elem=0):

        login_tag = self.driver.find_elements_by_css_selector(self.get_division_xpath_log_in)
        login_tag[0].click()
        reg_tag = self.driver.find_elements_by_css_selector(self.get_division_select_registration)
        reg_tag[0].click()

        reg_title = self.driver.find_elements_by_css_selector("*[pr-test='TabSignUp']")
        title = reg_title[elem].get_attribute("text")
        print(title)

        assert 'Реєстрація'== title, 'Can"t find registration page {page}'.format(page=self.driver.current_url)

        # email = self.driver.find_elements_by_css_selector("*[pr-test='RegEmail']")
        email = self.driver.find_element_by_name('email')
        email.send_keys('1@1.com')
        time.sleep(1)

        # display_name = self.driver.find_elements_by_css_selector("*[pr-test='RegName']")
        display_name = self.driver.find_element_by_name('display_name')
        display_name.send_keys(self.user_name)
        time.sleep(1)

        # password = self.driver.find_elements_by_css_selector("*[pr-test='RegPass']")
        password = self.driver.find_element_by_name('password')
        password.send_keys('1')
        time.sleep(1)

        # repeat_password = self.driver.find_elements_by_css_selector("*[pr-test='RegRepeatPass']")
        verify_password = self.driver.find_element_by_name('password1')
        verify_password.send_keys('1')
        time.sleep(1)

        # reg_btn = self.driver.find_elements_by_css_selector("*[pr-test='RegSubmit']")
        reg_btn = self.driver.find_element_by_class_name('sabmit-form')
        reg_btn.submit()


