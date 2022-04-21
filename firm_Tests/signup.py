import time
import sys
sys.path.append("D:/POM//")
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import warnings
from firm_Pages.Signup_Page import SignUp
from firm_Pages.CompanyInformation import CompanyInformation
from firm_Pages.Expertiseandexperience import ExpertiseandExperience
from firm_Pages.forgot_passwordPage import ForgotPassword
from Locators.Firm_locators import Locators
from firm_Pages.Profile_page import Profile_page
import HtmlTestRunner

class SignupTest(unittest.TestCase):

    # --------------Set Up----------------
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    def setUp(self):
        self.addCleanup(self.screen_shot)

    def screen_shot(self):
        """Take a Screen-shot of the drive homepage, when it Failed."""
        for method, error in self._outcome.errors:
            if error:
                self.driver.get_screenshot_as_file("firm_Tests//Screenshot//screenshot" + self.id() + ".png")

    #--------------------------------
    def test_1_signup(self):
        driver = self.driver
        driver.get(Locators.signup_url)
        # click_on_firm = SignUp(driver)
        # click_on_firm.click_on_firm_button()
        signup_data = SignUp(driver)
        signup_data.sign_up_data()
        click_on_register = SignUp(driver)
        click_on_register.click_on_register_button()

    def test_2_company_information(self):
        driver = self.driver
        check_current_screen = CompanyInformation(driver)
        check_current_screen.check_screen()
        enter_company_profile = CompanyInformation(driver)
        enter_company_profile.enter_company_details()
        enter_company_profile.company_deck()
        enter_company_profile.click_on_save_and_next_button()

    def test_3_expertise_and_experience(self):
        driver = self.driver
        check_current_screen = ExpertiseandExperience(driver)
        check_current_screen.check_screen()
        enter_expertiseandExperience_details = ExpertiseandExperience(driver)
        enter_expertiseandExperience_details.enter_expertise()
        enter_expertiseandExperience_details.enter_sectors()
        enter_expertiseandExperience_details.projects()
        enter_expertiseandExperience_details.click_on_submit_button()

    def test_4_logout(self):
        driver = self.driver
        logout_text = driver.find_element(by=By.CLASS_NAME, value=Locators.logout_link_text).text
        logout_button = driver.find_element(by=By.CLASS_NAME, value=Locators.logout_link_text).click()
        driver.assertEqual(logout_text, "Logout", logout_button)
        time.sleep(5)

    def test_5_forgotPassword_link(self):
        driver = self.driver
        driver.get(Locators.loginUrl)
        forgotpassword = ForgotPassword(driver)
        forgotpassword.click_forgot_password()
        time.sleep(1)

    def test_6_Reset_password_screen(self):
        driver = self.driver
        forgotpassword = ForgotPassword(driver)
        forgotpassword.check_url()
        forgotpassword.reset_password()

    def test_7_Check_mail(self):
        driver = self.driver
        forgotpassword = ForgotPassword(driver)
        forgotpassword.check_mail()

    def test_8_Change_Password(self):
        driver = self.driver
        forgotpassword = ForgotPassword(driver)
        forgotpassword.enter_password()

    #----------------------------------------------------------
    def test_9_login(self):
        driver = self.driver
        driver.get(Locators.loginUrl)
        username = Locators.username
        password = Locators.password
        driver.find_element(by=By.ID, value=Locators.email_textbox).send_keys(username)
        driver.find_element(by=By.ID, value=Locators.password_textbox).send_keys(password)
        sign_in_button_enabled = driver.find_element(by=By.CLASS_NAME, value=Locators.sign_in_button).is_enabled()
        if sign_in_button_enabled == True:
            driver.find_element(by=By.CLASS_NAME, value=Locators.sign_in_button).click()
            try:
                error = driver.find_element(by=By.XPATH, value=Locators.alert_message).text
                driver.assertEqual(error,Locators.error, 'Wrong Creditionals')
            except:
                assert True

    def test_a10_profile_screen(self):
        driver = self.driver
        click_on_profile_edit = Profile_page(driver)
        click_on_profile_edit.click_on_profile_edit_button()

    def test_a11_edit_company_information(self):
        driver = self.driver
        check_current_screen = CompanyInformation(driver)
        check_current_screen.check_screen()
        enter_company_profile = CompanyInformation(driver)
        enter_company_profile.enter_company_details()
        enter_company_profile.company_deck()
        enter_company_profile.click_on_save_and_next_button()

    def test_a12_edit_expertise_and_experience(self):
        driver = self.driver
        check_current_screen = ExpertiseandExperience(driver)
        check_current_screen.check_screen()
        enter_expertiseandExperience_details = ExpertiseandExperience(driver)
        enter_expertiseandExperience_details.enter_expertise()
        enter_expertiseandExperience_details.enter_sectors()
        enter_expertiseandExperience_details.projects()
        enter_expertiseandExperience_details.click_on_submit_button()

    def test_a13_profile_Opportunities_screen(self):
        driver = self.driver
        click_opportunties_tab_click = Profile_page(driver)
        click_opportunties_tab_click.click_opportunties_tab()

        submit_proposal = Profile_page(driver)
        submit_proposal.submit_proposal()

        modal_popup = Profile_page(driver)
        modal_popup.explore_more_opportunities()

    def test_a14_profile_proposal_screen(self):
        driver = self.driver
        proposal_tab = Profile_page(driver)
        proposal_tab.click_proposal_tab()

    def test_a15_logout_profile(self):
        driver = self.driver
        logout_text = driver.find_element(by=By.CLASS_NAME, value=Locators.logout_link_text).text
        logout_button = driver.find_element(by=By.CLASS_NAME, value=Locators.logout_link_text).click()
        driver.assertEqual(logout_text, "Logout", logout_button)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='firm_Tests//Reports'))
