from .general_part import GeneralPart
import random as rand
import config
import time


class Search_and_Subscribe(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page

    def __call__(self, *args, **kwargs):
        self.test_search_and_subscribe()
        self.to_subscribe()

    @classmethod
    def __repr__(cls):
        return 'search_and_subscribe'

    def test_search_and_subscribe(self):

        self.driver.get(self.testing_page)
        self.driver.find_elements_by_css_selector("*[pr-test='PortalList']")[0].click()
        title = self.driver.find_elements_by_css_selector("*[pr-test='SearchAndSubscribeTitle']")[0].text
        # print(title)

        assert 'Please, search and subscribe to any portal' == title, "Can't search and subscribe to portals, " \
                                                                      "page {page}".format(page=self.driver.current_url)

        search_text = ['portal', 'фірми', 'по']
        rand_search_text = rand.choice(search_text)
        # print(rand_search_text)

        search_field = self.driver.find_element_by_css_selector("*[pr-test='SearchForPortals']")
        search_field.send_keys(rand_search_text)
        time.sleep(3)

        # searching_results = self.driver.find_elements_by_css_selector("*[pr-test='PortalSearchingResults']")[0].text
        # print(searching_results)
        #
        # assert 'Searching results' == searching_results, "Can't find 'Searching results' row"

        mached_lighted_text = self.driver.find_elements_by_css_selector("*[pr-test='MachedLightedText']")[0].text
        print(mached_lighted_text)

        assert mached_lighted_text == rand_search_text, "Can't light search text {search_text}"\
            .format(search_text=rand_search_text)

    def to_subscribe(self):

        subs_buttons = self.driver.find_elements_by_css_selector("*[pr-test='SearchAndSubscribeBtn']")

        # Random Button Click
        random_subs_btn_id = (rand.choice(subs_buttons)).get_attribute("pr-test-portal-id")
        print(random_subs_btn_id)
        random_subs_btn = rand.choice(subs_buttons)
        random_subs_btn.click()
        time.sleep(3)

        # UserMustLogIN
        user = self.driver.find_element_by_name('email')
        user.send_keys('qwe@profi.ntaxa.com')
        time.sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys('1')
        time.sleep(2)
        form = self.driver.find_element_by_class_name('submit-form')
        form.submit()

        # assert 'You have successfully subscribed to this portal' in self.driver.page_source

        # Get Article Id
        self.driver.find_elements_by_css_selector(self.get_division_xpath_subscriptions)[0].click()
        self.get_portal_id(random_subs_btn_id)

    def get_portal_id(self, random_subs_btn_id, **kwarg):
        get_ids = set()
        for item in self.driver.find_elements_by_css_selector("*[pr-test='Grid-portal_name']"):
            get_ids.update({item.get_attribute("pr-id")})
        print(get_ids)

        # article_portal = self.driver.find_elements_by_css_selector("*[pr-test='ArticlePortal']")
        # article_portal_id = article_portal[0].get_attribute("pr-portal-id")
        # print(article_portal_id)

        assert random_subs_btn_id in get_ids, "Subscribed {subscribed} Portal not in Subscriptions {subscriptions} " \
                                              "Portal".format(subscribed=random_subs_btn_id, subscriptions=get_ids)
