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

        assert 'Please, search and subscribe to any portal' == title, "Can't search and subscribe to portals, " \
                                                                      "page {page}".format(page=self.driver.current_url)

        # search_text = ['portal', 'a', 'фірми', 'по']
        search_text = ['a', 'б']
        rand_search_text = rand.choice(search_text)

        search_field = self.driver.find_element_by_css_selector("*[pr-test='SearchForPortals']")
        search_field.send_keys(rand_search_text)
        time.sleep(3)

        mached_lighted_text = self.driver.find_elements_by_css_selector("*[pr-test='MachedLightedText']")[0].text
        print(mached_lighted_text)

        assert mached_lighted_text == rand_search_text, "Can't light search text {search_text}"\
            .format(search_text=rand_search_text)

    def to_subscribe(self):

        # RandomButtonClick
        subs_buttons = self.driver.find_elements_by_css_selector("*[pr-test='SearchAndSubscribeBtn']")
        random_subs_btn = rand.choice(subs_buttons)
        portal_id = random_subs_btn.get_attribute("pr-test-portal-id")
        random_subs_btn.click()
        print(portal_id)
        time.sleep(3)

        # UserMustLogIN
        user = self.driver.find_element_by_name('email')
        user.send_keys('abc@profi.ntaxa.com')
        time.sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys('1')
        time.sleep(2)
        form = self.driver.find_element_by_class_name('submit-form')
        form.submit()

        # assert 'You have successfully subscribed to this portal' in self.driver.page_source

        self.get_portal_id(portal_id)

    def get_portal_id(self, portal_id, **kwarg):

        self.click_news_or_favo_or_subs(news_or_favo_or_subs='UserSubscriptions')
        get_ids = set()
        for item in self.driver.find_elements_by_css_selector("*[pr-test='Grid-portal_name']"):
            get_ids.update({item.get_attribute("pr-id")})
        print(get_ids)

        assert portal_id in get_ids, "Subscribed {subscribed} Portal not in Subscriptions {subscriptions} Portal"\
            .format(subscribed=portal_id, subscriptions=get_ids)
