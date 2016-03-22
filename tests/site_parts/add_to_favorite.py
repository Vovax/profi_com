from .general_part import GeneralPart
import config
import time
from selenium.webdriver.common.keys import Keys
import os, sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Add_to_favorite(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page


    def __call__(self, *args, **kwargs):
        self.test_add_to_favorite()
        # self.click_favorite()

    @classmethod
    def __repr__(cls):
        return 'add_to_favorite'

    def test_add_to_favorite(self, elem=0, old_pos=0):

        self.driver.find_elements_by_css_selector("*[pr_test='UserNews']")[0].click()

        favorite_btn = self.driver.find_element_by_css_selector("*[pr-test='AddToFavoriteButton']")
        print(favorite_btn)
        like = favorite_btn.get_attribute("pr-like")
        print(like)
        # favorite_btn.click()
        # user_favorites = self.driver.find_element_by_css_selector("*[pr-test='UserFavorites']")[0].click()

        # btn = self.driver.find_element_by_css_selector("*[pr-test='AddToFavoriteButton']")
        # print(btn)
        # btn.click()

        # actions = ActionChains(self.driver)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", favorite_btn)
        # actions.move_to_element(favorite_btn).click()
        # actions.perform()

        # el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]")))
        # el.click()

        # if favorite_btn is None:
        #     print('ValidateFileButton is not found')
        #     exit(0)
        # else:
        #     print('ValidateFileButton is found')
        #     favorite_btn.click()

    # def click_favorite(self):
    #     action = ActionChains(self.driver)
    #     favorite_btn = self.driver.find_element_by_css_selector("*[ng-click='add_to_favorite(article)']")
    #     action.move_to_element(favorite_btn).perform()
    #     favorite_btn.click()

        # like_btn = self.driver.find_elements_by_css_selector("*[pr-test='AddToFavoriteButton']")
        # for i in like_btn:
        #     print(i)
        #     i.click()

        # self.driver.execute_script("arguments[0].scrollIntoView(true);", favo)
        # favo.click()
        # favorite_btn.click()
        # if favorite_btn is None:
        #    print('SelectFileForValidation is not found')
        #    exit(0)
        # else:
        #   print('favorite_btn is found')
        #   favorite_btn.click()

        # Actions action  = new Actions(driver)
        # action.Click(elem).Perform()
        # ActionChains(favorite_btn).move_to_element_with_offset(favo, 0, 20).click().perform()

        # self.driver.actions().click(favo).perform()
        # favo.click()



