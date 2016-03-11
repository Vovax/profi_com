from .general_part import GeneralPart
from selenium.webdriver.common.keys import Keys
import config
import time
from ..site_parts.log_in import Log_in
from utils.db_init import profi_db_con, pro_cur
import pathlib
import os
from os import path
import poplib



class Registration(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_pass=('1'), user_email=('saq@me.com'),
                 user_name=config.USER['name']):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        self.user_email = user_email
        self.user_pass = user_pass
        # cur.execute("SELECT data FROM test_data WHERE test_name='Registration'; ")


        # print(elem.get('user_pass'))
        # print(elem.get('user_mail'))
        # self.user_email = elem.get('user_mail')
        # self.user_password = elem.get('user_pass')


    def __call__(self, *args, **kwargs):
        self.test_registration()
        # self.checkUser()
        # self.tearDown()
        self.new_user()

    @classmethod
    def __repr__(cls):
        return 'registration'


    def test_registration(self, elem=0):

        login_tag = self.driver.find_elements_by_css_selector(self.get_division_xpath_log_in)
        login_tag[0].click()
        reg_tag = self.driver.find_elements_by_css_selector(self.get_division_select_registration)
        reg_tag[0].click()

        # reg_title = self.driver.find_elements_by_css_selector("*[pr-test='TabSignUp']")
        # title = reg_title[elem].get_attribute("text")
        # # print(title)
        # registration = 'Реєстрація'
        #
        # assert registration == title, 'Can"t find registration page {page}'.format(page=self.driver.current_url)
        #
        # # email = self.driver.find_elements_by_css_selector("*[pr-test='RegEmail']")
        # email = self.driver.find_element_by_name('email')
        # email.send_keys(self.user_email)
        # time.sleep(1)
        #
        # # display_name = self.driver.find_elements_by_css_selector("*[pr-test='RegName']")
        # display_name = self.driver.find_element_by_name('display_name')
        # display_name.send_keys(self.user_name)
        # time.sleep(1)
        #
        # # password = self.driver.find_elements_by_css_selector("*[pr-test='RegPass']")
        # password = self.driver.find_element_by_name('password')
        # password.send_keys(self.user_pass)
        # time.sleep(1)
        #
        # # repeat_password = self.driver.find_elements_by_css_selector("*[pr-test='RegRepeatPass']")
        # verify_password = self.driver.find_element_by_name('password1')
        # verify_password.send_keys(self.user_pass)
        # time.sleep(1)
        #
        # # reg_btn = self.driver.find_elements_by_css_selector("*[pr-test='RegSubmit']")
        # reg_btn = self.driver.find_element_by_class_name('sabmit-form')
        # reg_btn.submit()
        #
        # assert 'A confirmation email has been sent to you by email.' in self.driver.page_source, \
        #     "Can't register user {user}".format(user=self.user_name)
        # print(self.user_name)

    


        server = poplib.POP3("pop.gmail.com")
        server.user("volodymyr.khvesyk@gmail.com")
        server.pass_("pass")
        numMessages = len(M.list()[1])
        for i in range(numMessages):
            for j in M.retr(i+1)[1]:
                print(j)
            break




    def new_user(self):
        login_tag = self.driver.find_elements_by_css_selector(self.get_division_xpath_log_in)
        login_tag[0].click()

        # Log_in.login(self)
        # print('ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ')

        user = self.driver.find_element_by_name('email')
        user.send_keys(self.user_email)
        time.sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.user_pass)
        time.sleep(2)
        form = self.driver.find_element_by_class_name('submit-form')
        form.submit()


    # def checkUser(self):
    #     pro_cur.execute("""SELECT "profireader_name" FROM "user" WHERE "profireader_email"='1@1.com';""")
    #     elem = pro_cur.fetchone()[0]
    #     print(elem)
    #
    # def tearDown(self):
    #
    #     pro_cur.execute("""DELETE FROM "user" WHERE "profireader_email"='1@1.com';""")
    #     profi_db_con.commit()
    #
    #
    #     print('dadqwdqwdwefadfadfsdfasdfasdasdfafsdaf')




