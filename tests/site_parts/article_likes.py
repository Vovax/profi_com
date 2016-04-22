from .general_part import GeneralPart
import config
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ArticleLikes(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_article_likes()

    @classmethod
    def __repr__(cls):
        return 'article_likes'

    def test_article_likes(self):

        self.click_news_or_mark_or_subs(news_or_mark_or_subs='UserNews')

        selector = self.driver.find_elements_by_css_selector("*[pr-like]")
        get_likes = selector[0].get_attribute('pr-like')
        print(get_likes)
        count_likes = self.driver.find_elements_by_css_selector("*[pr-like='Like']")
        # print(count_likes[0].text)





        # for like in count_likes[0].text:
            # print(count_likes[0].text)
            # print(like)

            # print(len(str(count_likes[0].text)))
            # time.sleep(3)
        #
        # if count_likes[0].click():
        #     time.sleep(3)





        # a_length = 1
        # count = 0
        # while count < a_length:
        #     likes = self.driver.find_elements_by_css_selector("*[pr-like='Like']")[0][count:]
        #     a_length = len(likes) if count == 0 else a_length
        #     count_likes = likes[0].text
        #     print(count_likes)
        #     count += 1





