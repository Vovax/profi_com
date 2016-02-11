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
        print('aaaaaaaa')
        time.sleep(2)

        # self.driver.get(config.PROFIREADER_URL)
