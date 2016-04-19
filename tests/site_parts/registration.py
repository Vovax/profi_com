from .general_part import GeneralPart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import config
import time


class Registration(GeneralPart):

    def __init__(self, driver=None, testing_page=config.PROFIREADER_URL, new_frame=config.SQUIRREL_FRAME,
                 email_confirm=config.CONFIRM['email'], keypass_confirm=config.CONFIRM['pass'],
                 name_confirm=config.CONFIRM['name'], registration='Sign up',
                 user_email=('iam@profi.ntaxa.com'), user_name=('how'), user_pass=('1')):
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
        self.squirell_mail_login()
        self.get_message_link()
        self.accept_licence()
        self.log_out()

    @classmethod
    def __repr__(cls):
        return 'registration'

    def test_registration(self, elem=0):

        self.click_login_or_logout(login_or_logout='LogIn')
        reg_tag = self.driver.find_elements_by_css_selector(self.get_division_select_registration)
        reg_tag[0].click()

        reg_title = self.driver.find_elements_by_css_selector("*[pr-test='TabSignUp']")
        title = reg_title[elem].get_attribute("text")

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

    def squirell_mail_login(self):
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

    def get_message_link(self):

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

        confirm_link = self.driver.find_elements_by_xpath(self.get_division_select_confirm_link)[0].get_attribute("href")
        print(confirm_link)

        # hello_user = self.driver.find_elements_by_css_selector("*[pr-test='HelloUser']").get_attribute("text")
        # print(hello_user)

        self.driver.get(confirm_link)

    def accept_licence(self):

        print('Hello,' + ' ' + self.user_name + '!')

        assert 'Hello,' + ' ' + self.user_name + '!' in self.driver.page_source, \
            "Can't find new user name {name} on page source {page}".format(name=self.user_name,
                                                                           page=self.driver.page_source)

        confirmed = self.driver.find_elements_by_css_selector("*[pr-test='Confirmed']")[0].text
        print(confirmed)
        conf_text = 'You have confirmed your account successfully!'

        assert conf_text == confirmed or conf_text in self.driver.page_source, "Not Confirmed User {user}"\
            .format(user=self.user_email)

        #Почніть звідси!
        self.driver.find_elements_by_css_selector("*[pr-test='ConfirmEmail']")[0].click()
        time.sleep(3)

        self.driver.find_elements_by_css_selector("*[pr-test='HeaderAcceptLicence']")[0].click()
        time.sleep(3)

        licence_text = self.driver.find_elements_by_css_selector("*[pr-test='LicenceText']")[0].text

        assert 'Licence text' in licence_text, "Can't find Licence Text {licence}".format(licence=licence_text)

        self.driver.find_elements_by_css_selector("*[pr-test='AcceptLicence']")[0].click()
        time.sleep(3)

        user_header_name = self.driver.find_elements_by_css_selector("*[pr_test='UserProfile']")[0].text

        assert user_header_name == self.user_name, "User header name {header_name} isn't equal to user profile name " \
                                                   "{profile_name}, page {page}"\
            .format(page=self.driver.current_url, header_name=user_header_name, profile_name=self.user_name)

    def log_out(self):

        time.sleep(7)
        self.click_login_or_logout(login_or_logout='LogOut')

        # action = ActionChains(self.driver)
        # log_out_btn = self.driver.find_element_by_css_selector("*[pr_test='LogOut']")
        # action.move_to_element(log_out_btn).perform()
        # time.sleep(5)
        # log_out_btn.click()

        login_btn_visibility = self.driver.find_elements_by_css_selector("*[pr_test='LogIn']")[0].get_attribute('href')

        print(login_btn_visibility)
        assert 'login_signup' in login_btn_visibility, "User {user} can't finally Log out".format(user=self.user_name)













        # el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "*[pr_test='LogOut']")))
        # el.click()

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

        # server = poplib.POP3("pop.gmail.com")
        # server.user("mail")
        # server.pass_("pass")
        # numMessages = len(server.list()[1])
        # print('wwwww')
        # for i in range(numMessages):
        #     for j in server.retr(i+1)[1]:
        #         print(j)
        #     break

    # def scroll_to_and_click(xpath):
    #     btn = TestUtil.driver.find_element_by_xpath(xpath)
    #     TestUtil.driver.execute_script('window.scrollTo(0, ' + str(btn.location['y'])
# + ');')
#         btn.click()

