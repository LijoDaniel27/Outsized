from Locators.locators import Locators
from freelancerPages.loginPage import LoginPage
import time

class SignUp():

    def __init__(self, driver):
        self.driver = driver

    def click_sign_up_with_email(self):
        self.driver.find_element_by_class_name(Locators.signup_with_email).click()

    def sign_up_email(self):
        f = open("freelancerTest//tempfiles/emailid.txt", "w")
        f.write("pythonqa" + Locators.randomname + "@mailinator.com")
        f.close()
        f = open("freelancerTest//tempfiles//emailid.txt", "r")
        emailid = f.read()
        self.driver.find_element_by_id(Locators.signup_email).send_keys(emailid)

    def click_send_otp_button(self):
        self.driver.find_element_by_xpath(Locators.sendOTPbtn).click()

#-----------------Get OTP-----------------

    def get_otp(self):
        self.driver.execute_script("window.open('https://mailinator.com/','new window')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        f = open("freelancerTest//tempfiles//emailid.txt", "r")
        emailid = f.read()
        self.driver.find_element_by_xpath(Locators.mailinator_searchbx).send_keys(emailid)
        self.driver.find_element_by_xpath(Locators.mailinator_searchbtn).click()
        self.driver.find_element_by_xpath(Locators.mailinator_inbox).click()
        self.driver.switch_to.frame(self.driver.find_element_by_id(Locators.mail_frameset))
        value = self.driver.find_element_by_xpath(Locators.getOTP).text
        f = open("freelancerTest//tempfiles//temp_otp.txt", "w")
        f.write(value)
        f.close()
        time.sleep(4)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.current_url

#---------------Enter OTP-------------------

    def enter_otp(self):
        otp_label = self.driver.find_element_by_xpath(Locators.otp_text).text
        verify_button = self.driver.find_element_by_xpath(Locators.verify_otpbtn).text
        if otp_label == "OTP":
            f = open("freelancerTest//tempfiles//temp_otp.txt", "r")
            otp_value = f.read()
            self.driver.find_element_by_id(Locators.otptxtbox).send_keys(otp_value)
            if verify_button == "Verify OTP":
                self.driver.find_element_by_xpath(Locators.verify_otpbtn).click()
            else:
                assert False
        else:
            assert False

#-----------Welcome to Outsized-----------------

    def welcome_to_outsized(self):
        first_name_label = self.driver.find_element_by_xpath(Locators.firstname_label).text
        if first_name_label == 'First Name':
            self.driver.find_element_by_id(Locators.firstname_field).send_keys(Locators.enterManually_firstName+Locators.randomname)
        else:
            assert False

        last_name_label = self.driver.find_element_by_xpath(Locators.lastname_label).text
        if last_name_label == 'Last Name':
            self.driver.find_element_by_id(Locators.lastname_field).send_keys(Locators.enterManually_lastName)
        else:
            assert False

        set_password_label = self.driver.find_element_by_xpath(Locators.password_label).text
        if set_password_label == 'Set a new password':
            self.driver.find_element_by_id(Locators.password_field).send_keys(Locators.enterManually_password)
        else:
            assert False

        create_account_button = self.driver.find_element_by_xpath(Locators.create_account).text
        if create_account_button == "Create account":
            self.driver.find_element_by_xpath(Locators.create_account).click()
        else:
            assert False

#--------------Fill out your profile modal (Fill it manually button) -------------------------------

    def fill_out_your_profile_modal_use_fill_manually_button(self):
        modal_text = self.driver.find_element_by_class_name(Locators.modal_h1_text).text
        if modal_text == 'Fill out your profile to apply':
            fill_it_manually = self.driver.find_element_by_class_name(Locators.fill_it_manually_button).text
            if fill_it_manually == 'Fill profile manually':
                self.driver.find_element_by_class_name(Locators.fill_it_manually_button).click()
            else:
                assert False
        else:
            assert False

#--------------Fill out your profile modal (Use Linkedin button) -------------------------------

    def fill_out_your_profile_modal_use_linkedin_button(self):
        modal_text = self.driver.find_element_by_class_name(Locators.modal_h1_text).text
        if modal_text == 'Fill out your profile to apply':
            use_linkedin_button = self.driver.find_element_by_class_name(Locators.use_linkedin_profile).text
            if use_linkedin_button == 'Use LinkedIn profile':
                self.driver.find_element_by_class_name(Locators.use_linkedin_profile).click()
            else:
                assert False
        else:
            assert False

#---------------Enter Linkedin URL --------------------------------------------------------------

    def enter_linkedin_url(self):
        modal_text = self.driver.find_element_by_xpath('(//*[@class="linkedin-modal-title"])//h1').text
        if modal_text == 'Enter LinkedIn URL':
            self.driver.find_element_by_xpath('//*[@placeholder="eg. https://www.linkedin.com/in/username"]').send_keys('https://www.linkedin.com/in/lijo-daniel')
            time.sleep(1)
            self.driver.find_element_by_class_name('css-1jltwbs-commonButtonStyle').click()
            time.sleep(10)
        else:
            assert False

        linkedin_modal_open = self.driver.find_element_by_class_name('linkedin-modal').is_enabled()
        if linkedin_modal_open == True:
            linkedin_modal_title = self.driver.find_element_by_class_name('linkedin-modal-loader-title').text
            if linkedin_modal_title == 'Profile Updated':
                self.driver.find_element_by_xpath('//span[text()="Go"]').click()
            else:assert False
        else:assert False


#------------Sign up with linkedin-----------------------------------------------------------
    def sign_up_with_linkedin(self):
        linkedin_button = self.driver.find_element_by_class_name(Locators.linkedin_signup_button).text
        print(linkedin_button)
        if linkedin_button == 'Sign up with LinkedIn':
            self.driver.find_element_by_class_name('css-13qrrhu-commonButtonStyle').click()
        else:
            assert False
        driver = self.driver
        login = LoginPage(driver)
        login.enter_linkedin_username(Locators.linkedin_username_value)
        login.enter_linkedin_password(Locators.linkedin_password_value)
        time.sleep(2)
        login.click_linkedin_sign_in()
        time.sleep(6)

