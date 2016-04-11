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
        # self.test_create_new_company()
        self.companies_scroll()
        self.get_own_company()
        # self.own_company_edit()

    @classmethod
    def __repr__(cls):
        return 'create_new_company'

    # def test_create_new_company(self):
    #
    #     self.driver.get(self.company_list)
    #     self.driver.find_elements_by_css_selector("*[pr-test='CreateNewCompany']")[0].click()
    #
    #     text = 'Fest'
    #     e_mail = 'we@1.com'
    #     # name = self.driver.find_elements_by_css_selector("*[pr-test='InputCompanyName']")
    #     name = self.driver.find_element_by_name('company_name')
    #     name.send_keys(text)
    #     # country = self.driver.find_elements_by_css_selector("*[pr-test='InputCompanyCountry']")
    #     country = self.driver.find_element_by_name('company_country')
    #     country.send_keys(text)
    #     region = self.driver.find_element_by_name("company_region")
    #     region.send_keys(text)
    #     city = self.driver.find_element_by_name("company_city")
    #     city.send_keys(text)
    #     email = self.driver.find_element_by_name("company_email")
    #     email.send_keys(e_mail)
    #     time.sleep(5)
    #
    #     # upload_image = self.driver.find_elements_by_css_selector("*[pr-test='UploadImageBtn']")
    #     upload_image = self.driver.find_element_by_name('file')
    #     print(upload_image)
    #     upload_image.send_keys("/Users/apple/Desktop/test.jpg")
    #     time.sleep(5)
    #
    #     create_company = self.driver.find_elements_by_css_selector("*[pr-test='CreateCompanyBtn']")
    #     create_company[0].click()
    #     time.sleep(10)

    def companies_scroll(self, old_pos=0):
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

    def get_own_company(self, elem=0):

        a_length = 1
        count = 0

        while count < a_length:
            company = self.driver.find_elements_by_css_selector("*[pr-test='JoinedCompany']")[count:]
            a_length = len(company) if count == 0 else a_length
            own_or_joined = company[elem].text
            print(own_or_joined, '2222222')
            count += 1
            # if own_or_joined == 'OWN COMPANY':
            #         company[0].click()
            self.click_own_company(company, own_or_joined)

    def click_own_company(self, company, own_or_joined):
        if own_or_joined == 'OWN COMPANY':
                    company[0].click()


    def own_company_edit(self, elem=0):
        # company_edit = self.driver.find_elements_by_css_selector("*[pr-test='CompanyEdit']")
        # company_edit[0].click()
        #
        # upload_image = self.driver.find_element_by_name('file')
        # print(upload_image)
        # upload_image.send_keys("/Users/apple/Desktop/PROJECTS/business.jpg")
        # time.sleep(5)

        a_length = 1
        count = 0

        while count < a_length:
            company = self.driver.find_elements_by_css_selector("*[pr-test='JoinedCompany']")[count:]
            a_length = len(company) if count == 0 else a_length
            own_or_joined = company[elem].text
            print(own_or_joined, '2222222')
            count += 1
            if own_or_joined == 'OWN COMPANY':
                    company[0].click()

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
