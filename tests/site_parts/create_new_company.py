from .general_part import GeneralPart
import random as rand
import config
import time

class Create_new_company(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, company_list=config.COMPANY_LIST):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page
        self.company_list = company_list

    def __call__(self, *args, **kwargs):
        self.test_create_new_company()

    @classmethod
    def __repr__(cls):
        return 'create_new_company'

    def test_create_new_company(self):

        self.driver.get(self.company_list)
        self.driver.find_elements_by_css_selector("*[pr-test='CreateNewCompany']")[0].click()

        text = 'Fest'
        e_mail = 'we@1.com'
        # name = self.driver.find_elements_by_css_selector("*[pr-test='InputCompanyName']")
        name = self.driver.find_element_by_name('company_name')
        name.send_keys(text)
        # country = self.driver.find_elements_by_css_selector("*[pr-test='InputCompanyCountry']")
        country = self.driver.find_element_by_name('company_country')
        country.send_keys(text)
        region = self.driver.find_element_by_name("company_region")
        region.send_keys(text)
        city = self.driver.find_element_by_name("company_city")
        city.send_keys(text)
        email = self.driver.find_element_by_name("company_email")
        email.send_keys(e_mail)
        time.sleep(5)

        # upload_image = self.driver.find_elements_by_css_selector("*[pr-test='UploadImageBtn']")
        upload_image = self.driver.find_element_by_name('file')
        print(upload_image)
        upload_image.send_keys("/Users/apple/Desktop/test.jpg")
        time.sleep(5)

        create_company = self.driver.find_elements_by_css_selector("*[pr-test='CreateCompanyBtn']")
        create_company[0].click()
        time.sleep(10)

    def company_edit(self):

