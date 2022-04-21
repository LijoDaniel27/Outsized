from Locators.locators import Locators
from freelancerTest import Xlutils

class Call_url():

    def __init__(self, driver):
        self.driver = driver

    def call_url(self):
        path = "Excel//Outsized.xlsx"
        sheet = 'url'
        driver = self.driver
        staging = 1
        production = 2
        url = 1
        if staging == url:
            Xlutils.writeData(path, sheet, 2, 1, Locators.staging_login_url)
            Xlutils.writeData(path, sheet, 2, 2, Locators.staging_sign_up_url)
            Xlutils.writeData(path, sheet, 2, 3, Locators.staging_about_us_url)
            Xlutils.writeData(path, sheet, 2, 4, Locators.staging_forgot_password_url)
            Xlutils.writeData(path, sheet, 2, 5, Locators.staging_profile_url)
        elif production == url:
            Xlutils.writeData(path, sheet, 2, 1, Locators.login_url_prod)
            # driver.get(Locators.login_url_prod)
        else:
            assert False

        # time.sleep(3)
        # login_url_data = Xlutils.readData(path, sheet, 2, 1)
        # sign_up_url_data = Xlutils.readData(path, sheet, 2, 2)
        # about_us_url_data = Xlutils.readData(path, sheet, 2, 3)
        # forgot_password_url_data = Xlutils.readData(path, sheet, 2, 4)
        # profile_url_data = Xlutils.readData(path, sheet, 2, 5)
        # print(login_url_data)
        # print(sign_up_url_data)
        # print(about_us_url_data)
        # print(forgot_password_url_data)
        # print(profile_url_data)