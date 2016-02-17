from .general_part import GeneralPart
import config
import time


class Log_out (GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_log_out()

    @classmethod
    def __repr__(cls):
        return 'log_out'

    def test_log_out(self):
        self.click_my_profile_or_logout(profile_or_logout='logout')
        time.sleep(3)

        # print(self.get_division_xpath_log_out)
        # logout_tag = self.driver.find_element_by_xpath(self.get_division_xpath_log_out).click()
        # print(logout_tag)
        # logout_tag.click()
        # assert 'LOG IN' in self.driver.find_element_by_xpath(self.get_division_xpath_log_in).text, \
        #     'Can"t Log Out from {page}'.format(page=self.driver.current_url)

