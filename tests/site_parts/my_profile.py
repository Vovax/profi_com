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
        self.test_edit_profile()
        self.test_saving_text_changes()
        # self.upload_file()

    @classmethod
    def __repr__(cls):
        return 'my_profile'

    def test_my_profile(self):

        self.click_header_menu_item(header_menu_item='UserProfile')
        time.sleep(2)

        user_header_name = self.driver.find_elements_by_css_selector("*[pr_test='UserProfile']")[0].text
        user_profile_name = self.driver.find_elements_by_css_selector("*[pr-test='UserProfiName']")[0].text

        assert user_profile_name == user_header_name, "User header name {header_name} isn't equal to user profile " \
                                                      "name {profile_name}, page {page}"\
            .format(page=self.driver.current_url, header_name=user_header_name, profile_name=user_profile_name)

        assert 'User Profile' in self.driver.page_source, 'Can"t find "User Profile" , page {page}'\
            .format(page=self.driver.current_url)

    def test_edit_profile(self):

        edit_profile = self.driver.find_elements_by_css_selector("*[pr_test='EditProfile']")
        edit_profile[0].click()

        edit_title = self.driver.find_elements_by_css_selector("*[pr-test='EditProfileTitle']")[0].text

        assert edit_title == 'Edit profile' or edit_title == 'Редагувати профіль',\
            "Can't move to edit profile page {page}".format(page=self.driver.current_url)

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

        self.driver.get(self.testing_page)
        time.sleep(3)













    # def upload_file(self):
    #     upload_btn = self.driver.find_elements_by_css_selector("*[pr-test='UploadImageBtn']")
    #     print(upload_btn)
    #     time.sleep(5)
    #     upload_btn.send_keys("/Users/apple/Desktop/test.jpg")

        # self.driver.find_elements_by_css_selector("*[pr-test='UploadImageBtn']").click()
        # self.driver.switchTo().activeElement().send_keys("/Users/apple/Desktop/test.jpg")


