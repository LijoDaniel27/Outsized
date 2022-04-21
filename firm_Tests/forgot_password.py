from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import sys
sys.path.append("D:/POM//")
import time
import unittest
import HtmlTestRunner
import warnings
from firm_Pages.forgot_passwordPage import ForgotPassword
from Locators.Firm_locators import Locators


class ForgotPasswordTest(unittest.TestCase):
    driver = None
    # --------------Set Up----------------
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

    # -------------Click on link-------------------
    def test_1_Click_link(self):
        driver = self.driver
        driver.get(Locators.loginUrl)
        forgotpassword = ForgotPassword(driver)
        forgotpassword.click_forgot_password()
        time.sleep(1)

    #-------------Reset Password-------------------
    def test_2_Reset_password_screen(self):
        driver = self.driver
        forgotpassword = ForgotPassword(driver)
        forgotpassword.check_url()
        forgotpassword.reset_password()

    #-------------Check Mail----------------------
    def test_3_Check_mail(self):
        driver = self.driver
        forgotpassword = ForgotPassword(driver)
        forgotpassword.check_mail()

    #-------------Enter Password-----------------
    def test_4_Change_Password(self):
        driver = self.driver
        forgotpassword = ForgotPassword(driver)
        forgotpassword.enter_password()

    #-------------Login-------------------------
    def test_5_Login(self):
        driver = self.driver
        forgotpassword = ForgotPassword(driver)
        forgotpassword.login()

    # --------------Tear down----------------
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='firm_Tests//Reports'))
