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
        self.create_folder()

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

        for item in drop_down_item:
            print(item.text)
            if item.text == self.company_name:
                item.click()
                time.sleep(5)

    def create_folder(self):
        self.driver.find_elements_by_css_selector("*[pr-test='CreateFolder']")[0].click()
        input_folder_name = self.driver.find_elements_by_css_selector("*[pr-test='InputFolderName']")
        new_folder_name = ('new one')
        input_folder_name[0].send_keys(new_folder_name)
        time.sleep(3)
        self.driver.find_elements_by_css_selector("*[pr-test='SubmitFolder']")[0].click()
        time.sleep(5)

        folder_title = self.driver.find_elements_by_css_selector("*[pr-test='FolderName']")[0].get_attribute('title')

        assert new_folder_name in folder_title, "Can't find just created folder {folder}".format(folder=new_folder_name)

        get_folders = self.driver.find_elements_by_css_selector("*[pr-test='FolderID']")

        new_folder_id = get_folders[0].get_attribute('id')
        # print(new_folder_id)
        # print(ids)

        ids = self.folder_ids()
        print(ids)
        assert new_folder_id in ids, "Can't find just created folder {folder}".format(folder=new_folder_id)

        self.delete_folder(new_folder_id)

    def delete_folder(self, new_folder_id):

        self.driver.find_elements_by_css_selector("*[pr-test='DeleteFolder']")[0].click()
        time.sleep(3)
        self.driver.find_elements_by_css_selector("*[pr-test='ConfirmRemove']")[0].click()
        time.sleep(3)

        self.folder_ids()

        # assert new_folder_id not in ids, "Can't delete just created folder {folder}".format(folder=new_folder_id)

    def folder_ids(self):

        get_folders = self.driver.find_elements_by_css_selector("*[pr-test='FolderID']")
        ids = []
        for folder in get_folders:
            ids.append(folder.get_attribute('id'))
            # print(ids)
        return ids



        # list = [id for id in get_folder_id]
        # print(get_folder_id)
        # for id in get_folder_id:
        #     print(id)
        #     time.sleep(5)

        # assert get_folder_id






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









