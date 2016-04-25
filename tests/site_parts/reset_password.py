from .general_part import GeneralPart
import random as rand
import config
import time


class ResetPassword(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_email=config.TEST_REGISTRATION['email'],
                 user_name=config.TEST_REGISTRATION['name'], user_pass=config.TEST_REGISTRATION['pass']):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        self.user_email = user_email
        self.user_pass = user_pass

    def __call__(self, *args, **kwargs):
        self.test_reset_password()
        self.squirell_mail_login()
        self.get_message_link()
        self.reset_pass_input()
        self.test_re_login()


    @classmethod
    def __repr__(cls):
        return 'reset_password'

    def test_reset_password(self):

        self.click_login_or_logout(login_or_logout='LogIn')

        self.driver.find_elements_by_css_selector("*[pr-test='PassResetRequest']")[0].click()

        email_input = self.driver.find_element_by_name('email')
        email_input.send_keys(self.user_email)

        reset_btn = self.driver.find_elements_by_css_selector("*[pr-test='SendMessage']")
        reset_btn[0].click()
        time.sleep(3)
        # assert 'An email with instructions to reset your password has been sent to you.' in self.driver.page_source

    def test_re_login(self):

        username = self.driver.find_element_by_name('email')
        username.send_keys(self.user_email)
        time.sleep(5)
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.reset_user_pass)
        time.sleep(2)
        form = self.driver.find_element_by_class_name('submit-form')
        form.submit()
        time.sleep(3)

        user_header_name = self.driver.find_elements_by_css_selector("*[pr_test='UserProfile']")[0].text
        print(user_header_name)
        print(self.user_name)
        assert user_header_name == self.user_name, "User header name {header_name} isn't equal to user profile name " \
                                                   "{profile_name}, page {page}"\
            .format(page=self.driver.current_url, header_name=user_header_name, profile_name=self.user_name)

        self.click_login_or_logout(login_or_logout='LogOut')


