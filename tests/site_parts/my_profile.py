from .general_part import GeneralPart
import config
import time


class My_profile(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_my_profile()


    @classmethod
    def __repr__(cls):
        return 'my_profile'

    def test_my_profile(self):
        self.click_my_profile_or_logout(profile_or_logout='profile')
        time.sleep(2)

        self.driver.get(config.PROFIREADER_URL)

        drop_menu = self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)
        drop_menu[0].click()
        time.sleep(5)