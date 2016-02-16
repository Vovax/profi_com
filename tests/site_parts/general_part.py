import config


class GeneralPart(object):

    def __init__(self, driver):
        self.driver = driver
        self.get_division_xpath_log_in = self.division_xpath_log_in()
        self.get_division_xpath_log_out = self.division_xpath_log_out()
        self.get_division_xpath_header = self.division_xpath_header()
        self.get_division_xpath_drop_menu = self.division_xpath_drop_menu()
        self.get_division_xpath_my_profile = self.division_xpath_my_profile()
        self.get_division_xpath_login_by_google = self.division_xpath_login_by_google()
        self.get_division_xpath_login_by_facebook = self.division_xpath_login_by_facebook()
        self.get_division_xpath_login_by_linkedin = self.division_xpath_login_by_linkedin()
        self.get_division_xpath_login_by_microsoft = self.division_xpath_login_by_microsoft()


    def get_testing_page(self, elem_number=0):
        self.driver.get(config.PROFIREADER_URL)
        testing_page = self.driver.find_elements_by_xpath(
            "//nav[@class='navbar navbar-default widewrapper  ng-scope']/div[@class='container']/div\
        [@class='collapse navbar-collapse']/ul[@class='top-menu']/li/a")[elem_number].get_attribute('href')
        # testing_page = self.driver.find_elements_by_css_selector("div.well > div[class$='collaps'] > ul > li > a")
        return testing_page

    # def get_current_division_name(self):
    #     return self.driver.find_element_by_xpath("//div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav']"
    #                                              "/li/a[@id='navigation_selected_division']").text


    @staticmethod
    def division_xpath_header():
        return "//nav[@class='navbar navbar-default widewrapper  ng-scope']/div[@class='container']/div\
        [@class='container-fluid']/div[@class='collapse navbar-collapse']/ul[@class='top-menu']/a[@class='read_btn']"


    @staticmethod
    def division_xpath_log_in():
        return "//div[@class='container']/div[@class='container-fluid']/div[@class='collapse navbar-collapse']/\
        ul[@class='nav navbar-nav navbar-right']//ul[@class='user-auth']/li/a[@class='ng-binding']"
        # return "//div[@class='container widewrapper']/div[@class='auth-form ng-scope']/div[@class='content-block']/\
        #         div[@class='ng-scope']/form[@class='ng-pristine ng-valid']/input[@id='email']"

    @staticmethod
    def division_xpath_drop_menu():
        return "//div[@class='container']/div[@class='container-fluid']/div[@class='collapse navbar-collapse']/\
        ul[@class='nav navbar-nav navbar-right']//ul/li[@class='dropdown']/a[@class='ng-binding']"

    @staticmethod
    def division_xpath_my_profile():
        return "//nav[@class='navbar navbar-default widewrapper  ng-scope']/div[@class='container']/\
        div[@class='container-fluid']/div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav navbar-right']/\
        li[@class='dropdown']/ul/li[@class='dropdown open']/ul[@class='dropdown-menu']/li/a[@class='ng-binding']"

    def click_my_profile_or_logout(self, profile_or_logout='profile'):
        # self.driver.get(self.driver.find_element_by_xpath(self.division_xpath_drop_menu).href)
        href_click = None
        for href in self.driver.find_elements_by_xpath(
            "//nav[@class='navbar navbar-default widewrapper  ng-scope']/div[@class='container']/\
        div[@class='container-fluid']/div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav navbar-right']/\
        li[@class='dropdown']/ul/li[@class='dropdown open']/ul[@class='dropdown-menu']/li/a"):
            if profile_or_logout in href.get_attribute('href'):
                href_click = href
        href_click.click()

    @staticmethod
    def division_xpath_log_out():
        return "//nav[@class='navbar navbar-default widewrapper  ng-scope']/div[@class='container']/\
        div[@class='container-fluid']/div[@class='collapse navbar-collapse']/ul[@class='nav navbar-nav navbar-right']/\
        li[@class='dropdown']/ul/li[@class='dropdown open']/ul[@class='dropdown-menu']/li/a[text()='Log Out']"

    @staticmethod
    def division_xpath_login_by_google():
        return "//div[@class='container widewrapper']/div[@class='auth-form ng-scope']/div\
        [@class='content-block']/div[@class='ng-scope']/div[@class='via-social']/a[@class='login-by login-by-google']"

    @staticmethod
    def division_xpath_login_by_facebook():
        return "//div[@class='container widewrapper']/div[@class='auth-form ng-scope']/div\
        [@class='content-block']/div[@class='ng-scope']/div[@class='via-social']/a[@class='login-by login-by-facebook']"

    @staticmethod
    def division_xpath_login_by_linkedin():
        return "//div[@class='container widewrapper']/div[@class='auth-form ng-scope']/div\
        [@class='content-block']/div[@class='ng-scope']/div[@class='via-social']/a[@class='login-by login-by-linkedin']"
    @staticmethod
    def division_xpath_login_by_microsoft():
        return "//div[@class='container widewrapper']/div[@class='auth-form ng-scope']/div\
        [@class='content-block']/div[@class='ng-scope']/div[@class='via-social']/\
        a[@class='login-by login-by-microsoft']"