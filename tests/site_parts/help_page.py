from .general_part import GeneralPart
from selenium.webdriver.common.keys import Keys
import random as rand
import config
import time


class Help_page(GeneralPart):
    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page


    def __call__(self, *args, **kwargs):
        self.test_help_page()


    @classmethod
    def __repr__(cls):
        return 'help_page'


    def test_help_page(self, elem=0, old_pos=0):

        self.driver.find_elements_by_css_selector(self.get_division_xpath_help_page)[0].click()

        assert 'Help page' in self.driver.page_source, 'Can"t find Help page, in page {page}'\
            .format(page=self.driver.current_url)



        msg_text = ['Яка година?', 'Питання чи побажання?', 'Доброго дня!']
        msg_text = rand.choice(msg_text)
        time.sleep(3)

        send_btn = self.driver.find_element_by_css_selector("*[pr-test='SendMessage']")
        email = self.driver.find_element_by_css_selector("*[pr-test='EmailInput']")
        # email.send_keys(email_text)
        message = self.driver.find_element_by_css_selector("*[pr-test='TextInput']")
        message.send_keys(msg_text)
        send_btn.send_keys(Keys.RETURN)



        # assert 'Надішліть нам повідомлення' in self.driver.page_source,
