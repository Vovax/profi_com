from .general_part import GeneralPart
import config
import time


class Drop_menu (GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_drop_menu()

    @classmethod
    def __repr__(cls):
        return 'drop_menu'

    def test_drop_menu(self):
        drop_menu = self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)
        drop_menu[0].click()
        time.sleep(3)

        # assert 'Profile' in self.driver.find_element_by_xpath(self.get_division_xpath_drop_menu).text, \
        # 'Can"t find My Profile, in {page}'.format(page=self.driver.current_url)
