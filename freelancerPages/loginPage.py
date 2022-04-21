from Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    #-----------------------------Login with Email-----------------------------------
    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.username_textbox).clear()
        self.driver.find_element_by_id(Locators.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.password_textbox).clear()
        self.driver.find_element_by_id(Locators.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_button).click()


    #------------------------------Login with Linkedin---------------------------------
    def click_linkedin_button(self):
        button_label = self.driver.find_element_by_class_name('css-8ue2lb-commonButtonStyle').text
        if button_label == 'Sign In with LinkedIn':
            self.driver.find_element_by_class_name('css-8ue2lb-commonButtonStyle').click()
        else:
            assert False

    def enter_linkedin_username(self, username):
        self.driver.find_element_by_id(Locators.linkedin_username_textbox).clear()
        self.driver.find_element_by_id(Locators.linkedin_username_textbox).send_keys(username)

    def enter_linkedin_password(self, password):
        self.driver.find_element_by_id(Locators.linkedin_password_textbox).clear()
        self.driver.find_element_by_id(Locators.linkedin_password_textbox).send_keys(password)

    def click_linkedin_sign_in(self):
        self.driver.find_element_by_xpath(Locators.linkedin_signin_button).click()