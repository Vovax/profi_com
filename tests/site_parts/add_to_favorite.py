from .general_part import GeneralPart
import config
import time


class Add_to_favorite(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_add_to_favorite()

    @classmethod
    def __repr__(cls):
        return 'add_to_favorite'

    def test_add_to_favorite(self, elem=0, old_pos=0):

        self.driver.find_elements_by_css_selector("*[pr_test='UserNews']")[0].click()

        # like_btn = self.driver.find_elements_by_css_selector("*[pr-test='AddToFavoriteButton']")
        # for i in like_btn:
        #     print(i)
        #     i.click()

        favorite_btn = self.driver.find_element_by_css_selector("*[pr-test='AddToFavoriteButton']")
        print(favorite_btn.get_attribute("pr-like"))
        print(favorite_btn)

        # user_favorites = self.driver.find_element_by_css_selector("*[pr-test='UserFavorites']")[0].click()



        favorite_btn.click()

        # like = favorite_btn[0].get_attribute("pr-like")
        # print(like)





