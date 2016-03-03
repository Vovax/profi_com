import random as rand
from .general_part import GeneralPart
import config
import time
from utils.db_init import cur
from utils.db_init import db_con



class Subscriptions(GeneralPart):
    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_subscriptions()
        # self.getfields()
        # self.fieldid()
        # self.result()
        self.get_title()
        # self.scroll()


    @classmethod
    def __repr__(cls):
        return 'subscriptions'

    def test_subscriptions(self):
        self.driver.find_elements_by_css_selector(self.get_division_xpath_readline)[0].click()
        self.driver.find_elements_by_css_selector(self.get_division_xpath_subscriptions)[0].click()

    # def getfields(self, **kwarg):
    #     d_ids = set()
    #     for item in self.driver.find_elements_by_css_selector("*[pr-test='Grid']"):
    #         d_ids.update({item.get_attribute("pr-id")})
    #     # print(d_ids)
    #     self.result(d_ids)
    #
    # # def fieldid(self, elem_number=0, **kwarg):
    # #     get_id = self.driver.find_elements_by_css_selector("*[pr-test='Grid']")[elem_number].get_attribute("pr-id")
    # #     self.result(get_id)
    # #     print('fadsfasfa')
    #
    # def result(self, d_ids):
    #     for i in d_ids:
    #         print(i)
    #         cur.execute(""" INSERT INTO test_data(test_name, result) VALUES ('Subscriptions','{"field": "%s"}');""" % i)
    #     self.db_con = db_con
    #     db_con.commit()

    def get_title(self, elem=0):
        title = self.driver.find_elements_by_css_selector("*[pr-test='Grid-portal_name']")
        # print(title)
        title[elem].get_attribute("title")
        # print(title)
        self.driver.find_elements_by_css_selector(self.get_division_xpath_readline)[0].click()

        # for article in self.driver.find_elements_by_css_selector("*[pr-test='ArticlePortal']"):
        #     # self.driver.execute_script("window.scrollTo(0, 10000);")
        #     # time.sleep(5)
        #     # self.driver.execute_script("window.scrollTo(0, 10000);")
        #     pi = article.get_attribute("text")
        #     print(pi)

    # def scroll(self):
    #     page_height = 0
    #     scroll_height_script = " return window.innerHeight + window.scrollY "
    #     self.driver.execute_script("window.scrollTo(0, 1000);")
    #     while page_height != self.driver.execute_script(scroll_height_script):
    #         page_height = self.driver.execute_script(scroll_height_script)
    #         print(page_height)
    #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         time.sleep(3)


        a_length = 1
        count = 0
        while count < a_length:
            # print('ewrwrwer')
            article = self.driver.find_elements_by_css_selector("*[pr-test='ArticlePortal']")[count:]
            a_length = len(article) if count == 0 else a_length
            # print(article[0].text)
            # print('qrtret')
            count += 1

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # time.sleep(1)
            # self.driver.execute_script("window.scrollTo(0, 0);")

        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     scroll = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     if count < a_length:
        #         self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #         count += 1
        #         time.sleep(1)
        # p = self.driver.find_elements_by_css_selector("*[pr-test='ArticlePortal']")[0].text
        # print(p)





        # for company in self.driver.find_elements_by_css_selector("*[pr-test='Grid-portal_name']"):
        #     title = company.get_attribute("title")
        #     print(title)
        #     break

        # id = self.driver.find_elements_by_xpath

        # ("//div[@class='ui-grid-contents-wrapper']/\
        # div[@class='ui-grid-contents-wrapper']/div[@class=''ui-grid-viewport ng-isolate-scope]/\
        # div[@class='ui-grid-canvas']/div[@class='ui-grid-row ng-scope _ss']/div[@class='ng-isolate-scope']/\
        # div[@class='ui-grid-cell ng-scope ui-grid-coluiGrid-0006']/\
        # div[@class='ui-grid-cell-contents pr-grid-cell-field-type-link pr-grid-cell-field-name-portal_name  ng-scope']")[0].click()
        # print(id)
            # .get_attribute("pr-id")
        # print(field_id)
