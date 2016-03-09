from .general_part import GeneralPart
import config
import time
from utils.db_init import cur
from utils.db_init import db_con




class News(GeneralPart):
    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page


    def __call__(self, *args, **kwargs):
        self.test_news()


    @classmethod
    def __repr__(cls):
        return 'news'


    def test_news(self, elem=0, old_pos=0):

        title = self.driver.find_elements_by_css_selector("*[pr-test='Grid-portal_name']")
        # print(title)
        subs_article = title[elem].get_attribute("title")
        # print(subs_article)
        self.driver.find_elements_by_css_selector("*[pr_test='UserNews']")[0].click()

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            new_Height = self.driver.execute_script("return document.body.scrollHeight")
            if old_pos != new_Height:
                old_pos = new_Height
            else:
                return False
            print(new_Height)
            # request = new_Height.Timer("requests.get('return document.body.scrollHeight')", "import requests")
            # print(request)
            self.get_articles(subs_article)


    def get_articles(self, subs_article, elem=0):
        a_length = 1
        count = 0
        while count < a_length:
            article = self.driver.find_elements_by_css_selector("*[pr-test='ArticlePortal']")[count:]
            # print(article)
            a_length = len(article) if count == 0 else a_length
            news_article = article[elem].get_attribute("text")
            print(news_article, 'Z')
            print(subs_article, 'Q')
            count += 1

            assert news_article == subs_article, 'Portal Name {subs_article} from "Subsciptions" does not equal to ' \
                                                 'Article Portal {news_article} from "News", in page {page}'\
                .format(subs_article=subs_article, news_article=news_article, page=self.driver.current_url)


