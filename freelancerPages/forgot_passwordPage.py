import time
from freelancerPages.loginPage import LoginPage
from Locators.locators import Locators

class ForgotPassword():

    def __init__(self, driver):
        self.driver = driver

    #-----------------------------Forgot Password-----------------------------------
    def click_forgot_password(self):
        self.driver.find_element_by_link_text(Locators.forgot_link).click()

    #--------------------------Check Url-------------------------------------------
    def check_url(self):
        check_correct_page = self.driver.current_url
        if check_correct_page == Locators.forgotPasswordUrl:
            assert True
        else:
            assert False
    #-------------------------Reset Password--------------------------------------
    def reset_password(self):
        emailAddress_label = self.driver.find_element_by_xpath(Locators.mail_label).text
        if emailAddress_label == 'Email Address':
            self.driver.find_element_by_id(Locators.username_textbox).send_keys(Locators.username_value)
            time.sleep(2)
            buttoncheck = self.driver.find_element_by_xpath(Locators.reset_password_modal_button).text
            if buttoncheck == 'Reset Password':
                self.driver.find_element_by_xpath(Locators.reset_password_modal_button).click()
                time.sleep(2)
            else:
                assert False
        else:
            assert False

    #--------------------------Check_mail---------------------------------------------
    def check_mail(self):
        self.driver.execute_script("window.open('https://mailinator.com/','new window')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath(Locators.mailinator_searchbx).send_keys(Locators.username_value)
        self.driver.find_element_by_xpath(Locators.mailinator_searchbtn).click()
        self.driver.find_element_by_xpath(Locators.mailinator_inbox).click()
        self.driver.switch_to.frame(self.driver.find_element_by_id(Locators.mail_frameset))
        self.driver.find_element_by_xpath(Locators.reset_password_mail_button).click()
        time.sleep(4)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.current_url

    #--------------------------Enter Password-----------------------------------------------
    def enter_password(self):
        time.sleep(2)
        set_new_password_label = self.driver.find_element_by_class_name(Locators.modal_label_name).text
        if set_new_password_label == 'Set New Password':
            time.sleep(2)
            self.driver.find_element_by_xpath(Locators.create_password).send_keys(Locators.password_value)
            self.driver.find_element_by_xpath(Locators.confirm_password).send_keys(Locators.password_value)
            time.sleep(2)
            self.driver.find_element_by_class_name(Locators.reset_password_button).click()
            time.sleep(5)
        else:
            assert False

    #---------------------------Login after password change-------------------------------
    def login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username(Locators.username_value)
        login.enter_password(Locators.password_value)
        login.click_login()
        time.sleep(4)
        check_profile_url = driver.current_url
        if check_profile_url == Locators.profileUrl:
            print('Successfully Reached')
            assert True
        else:
            assert False