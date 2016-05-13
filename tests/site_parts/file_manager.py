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
        # print(drop_down_item)

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

        # folders = self.driver.find_elements_by_css_selector("*[pr-test='FolderName']")
        # folder_title = folders[0].get_attribute('title')

        get_folders = self.driver.find_elements_by_css_selector("*[pr-test='FolderID']")

        for folder in get_folders:
            print(folder.text)
            if folder.text == new_folder_name:
                new_folder_id = folder.get_attribute('id')
                print(new_folder_id, '111111111')

                ids = self.folder_ids()

                assert new_folder_id in ids, "Can't find just created folder {folder}".format(folder=new_folder_id)

                folder.click()

                self.upload_img_into_folder(new_folder_id, get_folders)
                break

    def upload_img_into_folder(self, new_folder_id, get_folders):

        # folders[0].click()
        time.sleep(3)
        self.driver.find_elements_by_css_selector("*[pr-test='UploadFile']")[0].click()

        select_img = self.driver.find_elements_by_css_selector("*[pr-test='SelectUpload']")
        select_img[0].send_keys("/Users/apple/Desktop/test.jpg")
        time.sleep(3)

        self.driver.find_elements_by_css_selector("*[pr-test='UploadBtn']")[0].click()
        time.sleep(3)

        self.copy_img()
        self.delete_folder(new_folder_id)

    def copy_img(self):
        get_folders = self.driver.find_elements_by_css_selector("*[pr-test='FolderID']")
        for folder in get_folders:
            actions = ActionChains(self.driver)
            actions.context_click(folder).perform()
            time.sleep(3)
            copy = self.driver.find_elements_by_link_text("копіювати")
            copy[0].click()
            time.sleep(3)
            actions = ActionChains(self.driver)
            actions.context_click(folder).perform()
            time.sleep(3)
            paste = self.driver.find_elements_by_link_text("вставити")
            paste[0].click()
            time.sleep(3)

            # print(get_folders.text)
            print(folder.text)

    def delete_folder(self, new_folder_id):

        self.driver.find_elements_by_css_selector("*[pr-test='GoBackFolder']")[0].click()
        time.sleep(3)

        get_folders = self.driver.find_elements_by_css_selector("*[pr-test='FolderID']")
        new_folder_name = ('new one')

        for folder in get_folders:
            # print(folder.text)
            if folder.text == new_folder_name:

                actions = ActionChains(self.driver)
                actions.context_click(folder).perform()
                time.sleep(5)
                re = self.driver.find_elements_by_link_text("remove")
                re[0].click()
                time.sleep(5)
                self.driver.find_elements_by_css_selector("*[pr-test='ConfirmRemove']")[0].click()
                time.sleep(3)

                self.assertion(new_folder_id)
                break

    def assertion(self, new_folder_id):

        ids = self.folder_ids()
        print(new_folder_id, '2222222222')
        print(ids)
        assert new_folder_id not in ids, "Can't delete just created folder {folder}".format(folder=new_folder_id)

    def folder_ids(self):

        get_folders = self.driver.find_elements_by_css_selector("*[pr-test='FolderID']")
        ids = []
        for folder in get_folders:
            ids.append(folder.get_attribute('id'))
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









