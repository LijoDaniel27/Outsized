import time
import sys
sys.path.append("D:/POM//")
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import warnings
import json
import HtmlTestRunner
from Locators.locators import Locators

x = open("firm_Tests//data.json", "r")
a = (x.read())
z = json.loads(a)
testvalue = z["Staging"]

class LoginTest(unittest.TestCase):
    # --------------Set Up----------------
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    # -------------Login-------------------
    def test_1_login(self):
        driver = self.driver
        for num in range(1,4):
            driver.get(testvalue[0]["login_url"])
            username = testvalue[num]["username"]
            password = testvalue[num]["password"]
            driver.find_element(by=By.ID, value="email").send_keys(username)
            driver.find_element(by=By.ID, value="password").send_keys(password)
            driver.find_element(by=By.XPATH, value="//*[@type='submit']").click()
            time.sleep(2)
            try:
                error = driver.find_element(by=By.XPATH, value='//*[@role="alert"]').text
                if error == testvalue[num]["error"]:
                    print(testvalue[num]["error"])
                else:
                    assert False
            except:
                print("Logged")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='firm_Tests//Reports'))
