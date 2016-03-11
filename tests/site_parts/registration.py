from .general_part import GeneralPart
from selenium.webdriver.common.keys import Keys
import config
import time
from utils.db_init import profi_db_con, pro_cur
import pathlib
import os
from os import path



class Registration(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, user_name=config.USER['name']):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        # cur.execute("SELECT data FROM test_data WHERE test_name='Registration'; ")


        # print(elem.get('user_pass'))
        # print(elem.get('user_mail'))
        # self.user_email = elem.get('user_mail')
        # self.user_password = elem.get('user_pass')


    def __call__(self, *args, **kwargs):
        self.test_registration()
        self.checkUser()
        self.tearDown()

    @classmethod
    def __repr__(cls):
        return 'registration'


    def test_registration(self, elem=0):

        login_tag = self.driver.find_elements_by_css_selector(self.get_division_xpath_log_in)
        login_tag[0].click()
        reg_tag = self.driver.find_elements_by_css_selector(self.get_division_select_registration)
        reg_tag[0].click()

        reg_title = self.driver.find_elements_by_css_selector("*[pr-test='TabSignUp']")
        title = reg_title[elem].get_attribute("text")
        # print(title)
        registration = 'Реєстрація'

        assert registration == title, 'Can"t find registration page {page}'.format(page=self.driver.current_url)

        # email = self.driver.find_elements_by_css_selector("*[pr-test='RegEmail']")
        email = self.driver.find_element_by_name('email')
        email.send_keys('1@1.com')
        time.sleep(1)

        # display_name = self.driver.find_elements_by_css_selector("*[pr-test='RegName']")
        display_name = self.driver.find_element_by_name('display_name')
        display_name.send_keys(self.user_name)
        time.sleep(1)

        # password = self.driver.find_elements_by_css_selector("*[pr-test='RegPass']")
        password = self.driver.find_element_by_name('password')
        password.send_keys('1')
        time.sleep(1)

        # repeat_password = self.driver.find_elements_by_css_selector("*[pr-test='RegRepeatPass']")
        verify_password = self.driver.find_element_by_name('password1')
        verify_password.send_keys('1')
        time.sleep(1)

        # reg_btn = self.driver.find_elements_by_css_selector("*[pr-test='RegSubmit']")
        reg_btn = self.driver.find_element_by_class_name('sabmit-form')
        reg_btn.submit()

        # assert ''

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


        # # We need to kick John out of the database, otherwise the test will fail
        # # in the future
        # path_to_database = path.join(path.curdir, "databases")
        # db = DAL('sqlite://storage.sqlite', folder=path_to_database)
        # db.import_table_definitions(path_to_database)
        #
        # #This gives us the users with the email address john@tukker.me
        # db_query = db(db.auth_user.email == 'john@tukker.me').select()
        # if len(db_query) > 0:
        #     db_query[0].delete_record() # delete John
        #     db.commit()

