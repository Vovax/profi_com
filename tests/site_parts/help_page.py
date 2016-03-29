from .general_part import GeneralPart
from utils.db_init import cur
import random as rand
import config
import time


class Help_page(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, login_link=config.MAIL_LOGIN,
                 user_email=config.MAIL_GMAIL, user_password=config.MAIL_PWD, mail_inbox=config.MAIL_INBOX):
        super().__init__(driver=driver)
        self.driver = driver
        self.testing_page = testing_page
        self.login_link = login_link
        self.mail_inbox = mail_inbox
        self.user_email = user_email
        self.user_password = user_password
        cur.execute("SELECT data FROM test_data WHERE test_name='Logination'; ")
        elem = cur.fetchone()[0]
        self.profi_email = elem.get('user_mail')
        cur.execute("SELECT data FROM test_data WHERE test_name='LogedIn'; ")
        el = cur.fetchone()[0]
        self.email = el.get('user_mail')

    def __call__(self, *args, **kwargs):
        self.test_help_page()
        self.contact_us()

    @classmethod
    def __repr__(cls):
        return 'help_page'

    def test_help_page(self, elem=0):

        self.driver.find_elements_by_css_selector(self.get_division_xpath_help_page)[0].click()
        under_title_txt = self.driver.find_elements_by_css_selector("*[pr-test='WillContactTitle']")[0].text
        # print(under_title_txt)

        assert 'Help page' or 'Contact Us' in self.driver.page_source, 'Can"t find Help page, in page {page}'\
            .format(page=self.driver.current_url)
        assert under_title_txt == 'Site Administrator will contact you', "Can't find under title text {txt}"\
            .format(txt=under_title_txt)

    def contact_us(self):

        msg_text = ['Яка година?', 'Питання чи побажання?', 'Доброго дня!', 'Hi, Profireader!']
        rand_msg_text = rand.choice(msg_text)
        # print(rand_msg_text)
        time.sleep(3)

        send_btn = self.driver.find_element_by_css_selector("*[pr-test='SendMessage']")
        # email = self.driver.find_element_by_css_selector("*[pr-test='EmailInput']")
        # email.send_keys(email_text)
        message = self.driver.find_element_by_css_selector("*[pr-test='TextInput']")
        message.send_keys(rand_msg_text)
        time.sleep(2)
        send_btn.click()
        time.sleep(10)
        # print(message)

        # assert 'Your message has been sent!' in self.driver.page_source, "Message {msg} hasn't been sent"\
        #     .format(msg=rand_msg_text)

        self.message_in_mail(rand_msg_text)

    def message_in_mail(self, rand_msg_text):

        # G-Mail_link
        self.driver.get(self.login_link)

        usr_email = self.driver.find_element_by_name('Email')
        usr_email.send_keys(self.profi_email)
        time.sleep(2)
        form = self.driver.find_element_by_id('signIn')
        form.submit()
        time.sleep(2)
        passwd = self.driver.find_element_by_name('Passwd')
        passwd.send_keys(self.user_password)
        time.sleep(2)
        form = self.driver.find_element_by_id('signIn')
        form.submit()

        # G-Mail_inbox
        self.driver.get(self.mail_inbox)

        self.driver.find_elements_by_xpath("//*[@id=':3g']")[0].click()

        mail_assert = self.driver.find_elements_by_xpath("//*[@class='a3s']/a")[0].text
        print(mail_assert)

        text_assert = self.driver.find_elements_by_xpath("//*[@class='a3s']")[0].text
        print(text_assert)

        assert rand_msg_text in text_assert, "Can't find Contact Us Message {msg}".format(msg=rand_msg_text)

        # print(self.email)
        # print(mail_assert)
        assert self.email == mail_assert, "Profile_email {pr_email} not equal to Inbox_email {in_email}"\
            .format(pr_email=self.user_email, in_email=mail_assert)
        time.sleep(5)

        self.driver.get(self.testing_page)
