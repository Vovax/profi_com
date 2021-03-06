from .general_part import GeneralPart
import random as rand
import config
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException


class Create_edit_new_company(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, company_list=config.COMPANY_LIST,
                 company_name='Fest', e_mail='we@1.com', re_mail='qweqw@qe.com'):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page
        self.company_list = company_list
        self.company_name = company_name
        self.e_mail = e_mail
        self.re_mail = re_mail

    def __call__(self, *args, **kwargs):
        self.test_create_new_company()
        self.scroll_all()
        self.get_own_company()

    @classmethod
    def __repr__(cls):
        return 'create_edit_new_company'

    def test_create_new_company(self):

        self.driver.get(self.company_list)
        self.driver.find_elements_by_css_selector("*[pr-test='CreateNewCompany']")[0].click()

        # name = self.driver.find_elements_by_css_selector("*[pr-test='InputCompanyName']")
        name = self.driver.find_element_by_name('company_name')
        name.send_keys(self.company_name)
        # country = self.driver.find_elements_by_css_selector("*[pr-test='InputCompanyCountry']")
        country = self.driver.find_element_by_name('company_country')
        country.send_keys(self.text)
        region = self.driver.find_element_by_name("company_region")
        region.send_keys(self.text)
        city = self.driver.find_element_by_name("company_city")
        city.send_keys(self.text)
        email = self.driver.find_element_by_name("company_email")
        email.send_keys(self.e_mail)
        time.sleep(5)

        # upload_image = self.driver.find_elements_by_css_selector("*[pr-test='UploadImageBtn']")
        upload_image = self.driver.find_element_by_name('file')
        print(upload_image)
        upload_image.send_keys("/Users/apple/Desktop/test.jpg")
        time.sleep(5)

        create_company = self.driver.find_elements_by_css_selector("*[pr-test='CreateCompanyBtn']")
        create_company[0].click()
        time.sleep(10)

    def scroll_all(self, old_pos=0):
        self.driver.get(self.company_list)

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(10)
            new_Height = self.driver.execute_script("return document.body.scrollHeight")
            if old_pos != new_Height:
                old_pos = new_Height
            else:
                return False
            print(new_Height)

    def get_own_company(self):

        a_length = 1
        count = 0
        while count < a_length:
            own_company = self.driver.find_elements_by_css_selector("*[pr-test='CompanyTitle']")[count:]
            company = own_company[0].text

            a_length = len(own_company) if count == 0 else a_length
            count += 1
            print(company)

        self.click_own()

    def click_own(self):
        time.sleep(3)
        element_by = "//*[contains(text(),"+"'"+self.company_name+"'"+")]"
        print(element_by)
        own = self.driver.find_elements_by_xpath(element_by)
        print(own[0].text)

        time.sleep(3)
        own[0].click()

        self.edit_own()

    def edit_own(self):

        self.driver.find_elements_by_css_selector("*[pr-test='EditCompanyProfile']")[0].click()

        email = self.driver.find_element_by_name("company_email")
        email.clear()
        time.sleep(3)
        email.send_keys(self.re_mail)
        time.sleep(3)
        self.driver.find_elements_by_css_selector("*[pr-test='SaveCompanyProfile']")[0].click()

        company_email = self.driver.find_elements_by_css_selector("*[pr-test='CompanyEmail']")[0].text
        print(company_email)
        assert self.re_mail in company_email, "Can't edit company {comp_name} profile"\
            .format(comp_name=self.company_name)





        # self.driver.get(self.company_list)

        # company = self.driver.find_elements_by_css_selector("*[pr-test='CompanyThumbnail']")
        # print(company[1].text)
        # company[0].click()

        # company = self.driver.find_elements_by_css_selector("*[pr-test='JoinedCompany']")
        # own_or_joined = company[0].text
        # print(own_or_joined)

        # for i in company:
        #     # print(i)
        #     own_company = i.text
        #     print(own_company)
        #     own = 'Type: OWN COMPANY'
            # if own_company == own:
            #     return company[own].click()
        # company[0].click()

        # company = self.driver.find_elements_by_css_selector("*[pr-test='JoinedCompany']")
        # print(company)
        # company[0].click()

        # nxt = self.driver.find_elements_by_xpath("//p[text()='Type: OWN COMPANY']")
        # nxt = self.driver.find_elements_by_css_selector("*[text()='Type: OWN COMPANY']")
        #
        # print(nxt)
        # nxt[0].click()

        # list_company = []
        # for i in company:
        #     own = i.text
        #     list_company.append(own)
        #     print(list_company.append(own))
        #     # print(own)
        #     if own == 'Type: OWN COMPANY':
        #         list_company.append(own)[0].click()
        #         company(len(own)).click()

        # company[0].click()

        # re = set()
        # for item in company:
        #     item.get_attribute("text")
        # print(item.get_attribute("text"))
