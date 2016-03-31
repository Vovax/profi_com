import config


class GeneralPart(object):

    def __init__(self, driver):
        self.driver = driver
        self.get_division_xpath_log_in = self.division_xpath_log_in()
        self.get_division_xpath_log_out = self.division_xpath_log_out()
        # self.get_division_xpath_drop_menu = self.division_xpath_drop_menu()
        self.get_division_xpath_my_profile = self.division_xpath_my_profile()
        self.get_division_xpath_login_by_google = self.division_xpath_login_by_google()
        self.get_division_xpath_login_by_facebook = self.division_xpath_login_by_facebook()
        self.get_division_xpath_login_by_linkedin = self.division_xpath_login_by_linkedin()
        self.get_division_xpath_login_by_microsoft = self.division_xpath_login_by_microsoft()
        self.get_division_xpath_logination = self.division_xpath_logination()
        self.get_division_xpath_subscriptions = self.division_xpath_subscriptions()
        self.get_division_xpath_readline = self.division_xpath_readline()
        self.get_division_xpath_help_page = self.division_xpath_help_page()
        self.get_division_select_registration = self.division_select_registration()
        self.get_division_select_confirm_link = self.division_select_confirm_link()

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
    def division_xpath_logination():
        return "//div[@class='container widewrapper']/div[@class='auth-form ng-scope']/div\
        [@class='content-block']/div[@class='ng-scope']/div[@class='via-social']/a"

    @staticmethod
    def division_xpath_drop_menu():
        return "//div[@class='container']/div[@class='row']/\
        div[@class='col-lg-offset-2 col-md-offset-1 col-lg-6 col-md-7 col-sm-8 col-xs-12 menu-site']/\
        div[@id='bs-example-navbar-collapse-1']/ul/li[@class='menu-profile']/a[@class='ng-binding']"

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
    #     return self.driver.find_element_by_xpath("//div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav']"
    #                                              "/li/a[@id='navigation_selected_division']").text

