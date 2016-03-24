from .general_part import GeneralPart
import config
import time
from selenium.webdriver.common.keys import Keys
import unittest



class My_profile(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_my_profile()
        self.test_edit_profile()
        self.test_saving_text_changes()

    @classmethod
    def __repr__(cls):
        return 'my_profile'

    def test_my_profile(self, elem=0):

        self.driver.find_elements_by_css_selector(self.get_division_xpath_my_profile)[0].click()
        # self.click_my_profile_or_logout(profile_or_logout='profile')
        time.sleep(2)
        user_header_name = self.driver.find_elements_by_css_selector("*[pr_test='UserProfile']")[0].text
        # print(name)
        user_profile_name = self.driver.find_elements_by_css_selector("*[pr-test='UserProfiName']")[0].text
        # print(profile_name)

        assert user_profile_name == user_header_name, "User header name {header_name} isn't equal to user profile " \
                                                      "name {profile_name}, page {page}"\
            .format(page=self.driver.current_url, header_name=user_header_name, profile_name=user_profile_name)

        assert 'User Profile' in self.driver.page_source, 'Can"t find "User Profile" , page {page}'\
            .format(page=self.driver.current_url)

        # Edit Profile

    def test_edit_profile(self):

        edit_profile = self.driver.find_elements_by_css_selector("*[pr_test='EditProfile']")
        edit_profile[0].click()

        edit_title = self.driver.find_elements_by_css_selector("*[pr-test='EditProfileTitle']")[0].text

        assert edit_title == 'Edit profile', "Can't move to edit profile page {page}"\
            .format(page=self.driver.current_url)

    def test_saving_text_changes(self):

        about_me = self.driver.find_element_by_name('about')
        time.sleep(5)
        about_me.clear()
        text_input = "Brave girl from Ukraine:)"
        about_me.send_keys(text_input)
        time.sleep(5)

        save_profile = self.driver.find_elements_by_css_selector("*[pr-test='SaveProfileButton']")
        save_profile[0].click()

        assert 'your profile was saved' in self.driver.page_source, "Can't save profile changes {changes}"\
            .format(changes=text_input)

        return_to_profile = self.driver.find_elements_by_css_selector("*[pr-test='ReturnToProfile']")
        return_to_profile[0].click()

        assert text_input in self.driver.page_source, "Can't find changes {changes} after profile edition"\
            .format(changes=text_input)

        print(text_input)

        edit_profile = self.driver.find_elements_by_css_selector("*[pr_test='EditProfile']")
        edit_profile[0].click()

        upload_btn = self.driver.find_elements_by_css_selector("*[pr-test='UploadImageBtn']")
        print(upload_btn)
        upload_btn.send_keys("home/apple/desktop/test.jpg")

        self.driver.find_elements_by_css_selector("*[pr-test='UploadImageBtn']").click()
        self.driver.switchTo().activeElement().sendKeys( "/home/test.jpg")


