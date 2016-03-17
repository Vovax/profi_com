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

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, email_confirm=config.CONFIRM['email'],
                 keypass_confirm=config.CONFIRM['pass'], name_confirm=config.CONFIRM['name'],
                 user_name=('myname'), registration='Реєстрація', user_pass=('1'),
                 user_email=('t1@profi.ntaxa.com'), new_frame=config.SQUIRREL_FRAME):
        super().__init__(driver)
        self.driver = driver
        self.testing_page = testing_page
        self.user_name = user_name
        self.user_email = user_email
        self.user_pass = user_pass
        self.registration = registration
        self.confirm = email_confirm
        self.keypass_confirm = keypass_confirm
        self.name_confirm = name_confirm
        self.frame = new_frame

    def __call__(self, *args, **kwargs):
        self.test_registration()
        # self.checkUser()
        # self.tearDown()
        # self.checkUserConfirm()
        self.getMessageLink()
        self.new_user_login()

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

        assert self.registration == title, 'Can"t find registration page {page}'.format(page=self.driver.current_url)

        # email = self.driver.find_elements_by_css_selector("*[pr-test='RegEmail']")
        email = self.driver.find_element_by_name('email')
        email.send_keys(self.user_email)
        time.sleep(1)

        # display_name = self.driver.find_elements_by_css_selector("*[pr-test='RegName']")
        display_name = self.driver.find_element_by_name('display_name')
        display_name.send_keys(self.user_name)
        time.sleep(1)

        # password = self.driver.find_elements_by_css_selector("*[pr-test='RegPass']")
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.user_pass)
        time.sleep(1)

        # repeat_password = self.driver.find_elements_by_css_selector("*[pr-test='RegRepeatPass']")
        verify_password = self.driver.find_element_by_name('password1')
        verify_password.send_keys(self.user_pass)
        time.sleep(1)

        # reg_btn = self.driver.find_elements_by_css_selector("*[pr-test='RegSubmit']")
        reg_btn = self.driver.find_element_by_class_name('sabmit-form')
        reg_btn.submit()

        assert 'A confirmation email has been sent to you by email.' in self.driver.page_source, \
            "Can't register user {user}".format(user=self.user_name)
        print(self.user_name)

        time.sleep(5)

        # SquirrelMail Confirmation
        self.driver.get(self.confirm)

        name = self.driver.find_element_by_name('login_username')
        name.send_keys(self.name_confirm)
        time.sleep(2)
        keypass = self.driver.find_element_by_name('secretkey')
        keypass.send_keys(self.keypass_confirm)
        time.sleep(2)
        login = self.driver.find_element_by_xpath("//input[@value='Login']")
        login.submit()
        time.sleep(2)

    def getMessageLink(self):

        self.driver.get(self.frame)
        link = self.driver.find_elements_by_xpath("/html/body/form/table/tbody/tr[5]/td/table/tbody/tr/td/table/tbody/"
                                                  "tr[2]/td[5]/b/a")
        text = link[0].text
        print(text)
        message = link[0].get_attribute('href')
        print(message)

        assert text == 'Confirm Your Account', "Can't find confirmation message {message}".format(message=message)

        time.sleep(2)
        link[0].click()

        confirm_link = self.driver.find_elements_by_xpath("/html/body/table[4]/tbody/tr[1]/td/table/tbody/tr/td/table/"
                                                          "tbody/tr/td/table/tbody/tr/td/pre/a")
        confirm_link[0].click()

        # assert 'Please log in to access this page.' in self.driver.page_source, "Not Confirmed User {user}"\
        #     .format(user=self.user_email)

        print('ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ')

    def new_user_login(self):

        self.driver.get(self.testing_page)
        login_tag = self.driver.find_elements_by_css_selector(self.get_division_xpath_log_in)
        login_tag[0].click()

        user = self.driver.find_element_by_name('email')
        user.send_keys(self.user_email)
        time.sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys(self.user_pass)
        time.sleep(2)
        form = self.driver.find_element_by_class_name('submit-form')
        form.submit()

        print('≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈')






    #     self.checkUserConfirm(user_email=self.user_email)
    #
    #
    #
    # def checkUserConfirm(self, user_email):
    #     pro_cur.execute("""SELECT "confirmed" FROM "user" WHERE "profireader_email"='%s';""" % user_email)
    #     elem = pro_cur.fetchone()[0]
    #     print(elem)
    #     if elem == True:
    #         assert elem == True, "User confirmed email {email}".format(email=user_email)
    #         return elem
    #     if elem == False:
    #         assert elem == False, "User doesn't confirmed email {email}".format(email=user_email)
    #         return elem


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


        # server = poplib.POP3("pop.gmail.com")
        # server.user("mail")
        # server.pass_("pass")
        # numMessages = len(server.list()[1])
        # print('wwwww')
        # for i in range(numMessages):
        #     for j in server.retr(i+1)[1]:
        #         print(j)
        #     break


