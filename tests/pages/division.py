from .general import General
import config

# class Division(Footer):
#     def __init__(self, driver):
#         super(Footer, self).__init__(driver)
#         self.driver = driver


class GeneralDriver(General):
    testing_page = config.PROFIREADER_URL

    def __init__(self, driver, device='PC'):
        self.device = device
        self.set_config()
        self.driver = driver
        super().__init__(device=self.device, driver=self.driver, testing_page=self.testing_page)



class Division(General):

    def get_testing_page(self, elem_number=0):
        self.driver.get(config.PROFIREADER_URL)
        testing_page = self.driver.find_elements_by_xpath(
            "//div[@class='container']/div[@class='container-fluid']/div[@class='collapse navbar-collapse']/\
        ul[@class='nav navbar-nav navbar-right']/ul[@class='user-auth']/li/a[@class='ng-binding']/href")[
            elem_number].get_attribute('href')
        print('a')
        return testing_page

    # def __init__(self, driver, device='PC'):
    #     self.device = device
    #     # self.testing_page = self.get_testing_page()
    #     self.set_config()
    #     print('sssssss')
    #     self.driver = driver
    #     self.driver.close()
    #     super().__init__(device=self.device, driver=self.driver, testing_page=self.testing_page)



