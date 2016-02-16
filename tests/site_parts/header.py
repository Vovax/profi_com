import random as rand
from .general_part import GeneralPart
import config
import time


class Header(GeneralPart):
    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_top_navbar(random=False)


    @classmethod
    def __repr__(cls):
        return 'header'

    def test_top_navbar(self, random=False):
        hrefs = self.driver.find_elements_by_xpath(self.get_division_xpath_header)
        if random:
            hrefs = rand.choice(hrefs)            #string = rand.choice(hrefs).text    #object = rand.choice(hrefs)
            assert type(hrefs) is str, "Can't find href for division"
            hrefs.click()
            assert 'Not Found' not in self.driver.page_source, \
                'Page {page} Not Found'.format(page=self.driver.current_url)
            assert self.driver.current_url != self.testing_page, "Can't move to {url}".format(url=hrefs)
        else:
            a_length = 1
            count = 0
            while count < a_length:
                # print(hrefs)
                hrefs = self.driver.find_elements_by_xpath(self.get_division_xpath_header)[count:]
                a_length = len(hrefs) if count == 0 else a_length
                count += 1
                hrefs[0].click()
                time.sleep(2)


                # if '_c' not in self.driver.current_url and \
                #         self.driver.find_elements_by_xpath(
                #             "//div[@class='col-md-9']/div[@class='block-item list-elements']"):
                #     assert self.get_number_of_current_page() == 1, 'Page number is not 1(first), ' \
                #                                                    'when switch to {division}'.format(
                #         division=self.get_current_division_name())
                # if '_c' not in self.driver.current_url and not \
                #         self.driver.find_elements_by_xpath(
                #             "//div[@class='col-md-9']/div[@class='block-item list-elements']"):
                #     assert not self.driver.find_elements_by_class_name('pager'), \
                #         'Show pages, but there are no articles on page {page}'.format(page=self.driver.current_url)
                #
                # self.driver.get(self.testing_page)
                # assert self.driver.current_url == self.testing_page or self.driver.current_url == self.testing_page+'/'
                # time.sleep(1)
                # print('header')