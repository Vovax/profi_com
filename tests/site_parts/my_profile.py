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

    def test_my_profile(self, elem=0):
        self.driver.find_elements_by_css_selector(self.get_division_xpath_my_profile)[0].click()
        # self.click_my_profile_or_logout(profile_or_logout='profile')
        time.sleep(2)
        # self.driver.get(self.testing_page)
        name = self.driver.find_elements_by_css_selector("*[pr_test='UserProfile']")[0].text
        # print(name)
        profile_name = self.driver.find_elements_by_css_selector("*[pr-test='UserProfiName']")[0].text
        # print(profile_name)

        assert profile_name == name, "Can't move to 'User Profile' page {page}".format(page=self.driver.current_url)
        # print(self.driver.current_url)
        assert 'User Profile' in self.driver.page_source, 'Can"t find "User Profile" , page {page}'\
            .format(page=self.driver.current_url)










        #
        # drop_menu = self.driver.find_elements_by_xpath(self.get_division_xpath_drop_menu)
        # drop_menu[0].click()
        # time.sleep(5)


        # assert 'profile' in self.driver.current_url, 'Can"t find My Profile page'.format(page=self.driver.current_url)
