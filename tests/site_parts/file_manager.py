from .general_part import GeneralPart
import config
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class FileManager(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, company_name='Fest files'):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page
        self.company_name = company_name

    def __call__(self, *args, **kwargs):
        self.test_file_manager()
        # self.click()

    @classmethod
    def __repr__(cls):
        return 'file_manager'

    def test_file_manager(self):

        self.click_header_menu_item(header_menu_item='FileManager')
        time.sleep(5)
        self.click_file_manager_navigate(file_manager_navigate='DropDownMenuRoots')
        time.sleep(7)

        drop_down_item = self.driver.find_elements_by_css_selector("*[pr-test='DropDownMenuItem']")
        # own = self.driver.find_elements_by_xpath("//*[contains(text(),"+"'"+self.company_name+"'"+")]")
        print(drop_down_item)
        # print(own)
        # print(own[0].text)

        for item in drop_down_item:
            print(item.text)
            own = item.text














        # drop_down_item = self.driver.find_elements_by_css_selector("*[pr-test='DropDownMenuItem']")
        # drop_down_item[0].click()

        # time.sleep(3)
        # element_by = "//*[contains(text(),"+"'"+self.company_name+"'"+")]"
        # print(element_by)

    # def click(self):
    #     own = self.driver.find_elements_by_xpath("//*[contains(text(),"+"'"+self.company_name+"'"+")]")
        # try:
        #     self.wait_until_visible_then_click(own)
        # except WebDriverException:
        #     self.wait_until_visible_then_click(own)
        # time.sleep(3)

    # def wait_until_visible_then_click(self, element):
    #     element = WebDriverWait(self.driver, 5, poll_frequency=.2).until(EC.visibility_of(element))
    #     element.click()

        # self.driver.execute_script("arguments[0].scrollIntoView();", own)

        # actions = ActionChains(self.driver)
        # actions.move_to_element(own).click().perform()









