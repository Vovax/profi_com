from .general_part import GeneralPart
import random as rand
import config
import time


class Companies(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, company_list=config.COMPANY_LIST):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page
        self.company_list = company_list

    def __call__(self, *args, **kwargs):
        # self.test_companies()
        self.companies_click()
        self.companies_scroll()
        self.get_own_company()

    @classmethod
    def __repr__(cls):
        return 'companies'

    # def test_companies(self, random=None):

        # self.driver.find_elements_by_css_selector(self.get_division_select_companies_list)[0].click()
        # time.sleep(2)
        #
        # assert 'Your company list:' in self.driver.page_source, "Can't find company list"
        #
        # company = self.driver.find_elements_by_css_selector("*[pr-test='CompanyThumbnail']")
        # if random:
        #     company = rand.choice(company)
        #     assert type(company) is str, "Can't find company"
        #     company.click()
        #     assert 'Not Found' not in self.driver.page_source, \
        #         'Page {page} Not Found'.format(page=self.driver.current_url)
        #     assert self.driver.current_url != self.testing_page, "Can't move to {url}".format(url=company)
        # else:
        #     a_length = 1
        #     count = 0
        #
        #     while count < a_length:
        #         company = self.driver.find_elements_by_css_selector("*[pr-test='CompanyThumbnail']")[count:]
        #         a_length = len(company) if count == 0 else a_length
        #         count += 1
        #         if count > 5:
        #             print('ewrrwerwer')
        #             self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #             time.sleep(2)
        #             print(company)
        #         company[0].click()
        #         time.sleep(5)

                # self.driver.get(self.company_list)

    def companies_click(self):

        self.driver.find_elements_by_css_selector(self.get_division_select_companies_list)[0].click()

        a_length = 1
        count = 0

        while count < a_length:
            company = self.driver.find_elements_by_css_selector("*[pr-test='CompanyThumbnail']")[count:]
            a_length = len(company) if count == 0 else a_length
            # count += 1

            if count > 2:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            count += 1
            company[0].click()
            time.sleep(2)

            self.driver.get(self.company_list)

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
            print(own_or_joined, '00000')
            count += 1
            if own_or_joined == 'OWN COMPANY':
                company[0].click()
            # self.click_own_company(company, own_or_joined)
    #
    # def click_own_company(self, company, own_or_joined):
    #     if own_or_joined == 'OWN COMPANY':
    #         company[0].click()

