import config
import time


class GeneralPart(object):

    def __init__(self, driver, email_confirm=config.CONFIRM['email'], keypass_confirm=config.CONFIRM['pass'],
                 name_confirm=config.CONFIRM['name'], new_frame=config.SQUIRREL_FRAME,
                 user_email=config.TEST_REGISTRATION['email'], reset_user_pass=config.RESET_USER['pass']):
        self.frame = new_frame
        self.confirm = email_confirm
        self.keypass_confirm = keypass_confirm
        self.name_confirm = name_confirm
        self.user_email = user_email
        self.reset_user_pass = reset_user_pass
        self.driver = driver
        self.get_division_xpath_log_in = self.division_xpath_log_in()
        self.get_division_xpath_log_out = self.division_xpath_log_out()
        self.get_division_xpath_my_profile = self.division_xpath_my_profile()
        self.get_division_xpath_login_by_google = self.division_xpath_login_by_google()
        self.get_division_xpath_login_by_facebook = self.division_xpath_login_by_facebook()
        self.get_division_xpath_login_by_linkedin = self.division_xpath_login_by_linkedin()
        self.get_division_xpath_login_by_microsoft = self.division_xpath_login_by_microsoft()
        self.get_division_xpath_subscriptions = self.division_xpath_subscriptions()
        self.get_division_xpath_readline = self.division_xpath_readline()
        self.get_division_xpath_help_page = self.division_xpath_help_page()
        self.get_division_select_registration = self.division_select_registration()
        self.get_division_select_confirm_link = self.division_select_confirm_link()
        self.get_division_select_companies_list = self.division_select_companies_list()

    @staticmethod
    def division_select_confirm_link():
        return "/html/body/table[4]/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/pre/a"

    @staticmethod
    def division_xpath_log_in():
        return "*[pr_test='LogIn']"

    @staticmethod
    def division_select_registration():
        return "*[pr-test='TabSignUp']"

    @staticmethod
    def division_select_companies_list():
        return "*[pr_test='CompaniesList']"

    @staticmethod
    def division_xpath_my_profile():
        return "*[pr_test='UserProfile']"

    @staticmethod
    def division_xpath_log_out():
        return "*[pr_test='LogOut']"

    @staticmethod
    def division_xpath_login_by_google():
        return "*[pr_test='GoogleLogin']"


    @staticmethod
    def division_xpath_login_by_facebook():
        return "*[pr_test='FacebookLogin']"


    @staticmethod
    def division_xpath_login_by_linkedin():
        return "*[pr_test='LinkedinLogin']"


    @staticmethod
    def division_xpath_login_by_microsoft():
        return "*[pr_test='MicrosoftLogin']"

    @staticmethod
    def division_xpath_readline():
        return "*[pr_test='ReadLine']"

    @staticmethod
    def division_xpath_subscriptions():
        return "*[pr_test='UserSubscriptions']"

    @staticmethod
    def division_xpath_help_page():
        return "*[pr_test='UserInfo']"

    def click_login_or_logout(self, login_or_logout='LogOut'):
        pr_login_or_logout_click = None
        for pr_login_or_logout in self.driver.find_elements_by_css_selector("*[pr_test"):
            if login_or_logout in pr_login_or_logout.get_attribute('pr_test'):
                pr_login_or_logout_click = pr_login_or_logout
        pr_login_or_logout_click.click()

    def click_news_or_mark_or_subs(self, news_or_mark_or_subs='UserSubscriptions'):
        pr_news_or_mark_or_subs_click = None
        for pr_news_or_mark_or_subs in self.driver.find_elements_by_css_selector("*[pr_test"):
            if news_or_mark_or_subs in pr_news_or_mark_or_subs.get_attribute('pr_test'):
                pr_news_or_mark_or_subs_click = pr_news_or_mark_or_subs
        pr_news_or_mark_or_subs_click.click()

    def click_header_menu_item(self, header_menu_item='CompaniesList'):
        pr_header_menu_item_click = None
        for pr_header_menu_item in self.driver.find_elements_by_css_selector("*[pr_test"):
            if header_menu_item in pr_header_menu_item.get_attribute('pr_test'):
                pr_header_menu_item_click = pr_header_menu_item
        pr_header_menu_item_click.click()

    def click_file_manager_navigate(self, file_manager_navigate='UploadFile'):
        pr_file_manager_navigate_click = None
        for pr_file_manager_navigate in self.driver.find_elements_by_css_selector("*[pr-test"):
            if file_manager_navigate in pr_file_manager_navigate.get_attribute('pr-test'):
                pr_file_manager_navigate_click = pr_file_manager_navigate
        pr_file_manager_navigate_click.click()

    def scroll_all(self, old_pos=0):
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            new_Height = self.driver.execute_script("return document.body.scrollHeight")
            if old_pos != new_Height:
                old_pos = new_Height
            else:
                return False

    def squirell_mail_login(self):
        self.driver.get(self.confirm)

        name = self.driver.find_element_by_name('login_username')
        name.send_keys(self.name_confirm)
        time.sleep(2)
        keypass = self.driver.find_element_by_name('secretkey')
        keypass.send_keys(self.keypass_confirm)
        time.sleep(2)
        login = self.driver.find_element_by_xpath("//input[@value='Login']")
        login.submit()
        time.sleep(2)

    def get_message_link(self):

        self.driver.get(self.frame)
        link = self.driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/"
                                                  "tr[2]/td[5]/b/a")
        text = link[0].text
        print(text)
        message = link[0].get_attribute('href')
        print(message)

        # assert text == 'Confirm Your Account', "Can't find confirmation message {message}".format(message=message)

        time.sleep(2)
        link[0].click()

        confirm_link = self.driver.find_elements_by_xpath(self.get_division_select_confirm_link)[0].get_attribute("href")
        print(confirm_link)

        self.driver.get(confirm_link)

    def reset_pass_input(self):

        email_input = self.driver.find_element_by_name('email')
        email_input.send_keys(self.user_email)

        pass_input = self.driver.find_element_by_name('password')
        pass_input.send_keys(self.reset_user_pass)

        rep_pass_input = self.driver.find_element_by_name('password1')
        rep_pass_input.send_keys(self.reset_user_pass)

        reset_btn = self.driver.find_elements_by_css_selector("*[pr-test='RegSubmit']")
        reset_btn[0].click()
        time.sleep(7)





















    # def click_my_profile_or_logout(self, profile_or_logout='profile'):
    #     href_click = None
    #     for href in self.driver.find_elements_by_css_selector("*[pr_test='LogOut']"):
    #         if profile_or_logout in href.get_attribute('href'):
    #             href_click = href
    #     href_click.click()

    # def get_testing_page(self, elem_number=0):
    #     self.driver.get(config.PROFIREADER_URL)
    #     testing_page = self.driver.find_elements_by_xpath(
    #         "//nav[@class='navbar navbar-default widewrapper  ng-scope']/div[@class='container']/div\
    #     [@class='collapse navbar-collapse']/ul[@class='top-menu']/li/a")[elem_number].get_attribute('href')
    #     testing_page = self.driver.find_elements_by_css_selector("div.well > div[class$='collaps'] > ul > li > a")
        # return testing_page

    # def get_current_division_name(self):
    #     return self.driver.find_element_by_xpath
    # ("//div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav']"
    #                                              "/li/a[@id='navigation_selected_division']").text

        # @staticmethod
    # def division_xpath_drop_menu():
    #     return "//div[@class='container']/div[@class='row']/\
    #     div[@class='col-lg-offset-2 col-md-offset-1 col-lg-6 col-md-7 col-sm-8 col-xs-12 menu-site']/\
    #     div[@id='bs-example-navbar-collapse-1']/ul/li[@class='menu-profile']/a[@class='ng-binding']"

    #     @staticmethod
    # def division_xpath_logination():
    #     return "//div[@class='container widewrapper']/div[@class='auth-form ng-scope']/div\
    #     [@class='content-block']/div[@class='ng-scope']/div[@class='via-social']/a"

