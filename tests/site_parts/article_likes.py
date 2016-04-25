from .general_part import GeneralPart
import config
import time


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

        article_likes = self.driver.find_elements_by_css_selector("*[pr-like='Like']")
        article_likes[0].click()
        time.sleep(3)

        for count_likes in range(0, int(article_likes[0].text)):
            print(count_likes)

            assert count_likes + 1 or count_likes - 1

        self.driver.get(self.testing_page)
        time.sleep(3)

