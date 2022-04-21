from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators
import time
import random

class Work_Preference():

    def __init__(self, driver):
        self.driver = driver

    def workExperience(self):
        driver = self.driver
        #driver.get('https://outsized.site/create-profile/work-preference')

        currentEmploymentStatus_randomize = random.randrange(0, 2)
        currentEmploymentStatus = Locators.workExperience[0]["currentEmploymentStatus"][currentEmploymentStatus_randomize]["status"]

        howSoonCanYouStart_randomize = random.randrange(0, 3)
        howSoonCanYouStart = Locators.workExperience[0]["howSoonCanYouStart"][howSoonCanYouStart_randomize]["start"]

        capacity_randomize = random.randrange(0, 2)
        capacity_value = Locators.workExperience[0]["capacity"][capacity_randomize]["capacityValue"]

        rate_randomize = random.randrange(0, 2)
        rate_value = Locators.workExperience[0]["rate"][rate_randomize]["rate_value"]

        currency_randomize = random.randrange(0, 2)
        currency_value = Locators.workExperience[0]["currency"][currency_randomize]["curr_value"]

        amount_randomize = random.randrange(10000,25000)

        visibility = "Public"


        current_employment_status = driver.find_element_by_xpath(Locators.current_employment_status).text
        if current_employment_status == 'Current employment status *':
            driver.find_element_by_xpath('//*[text()="' + currentEmploymentStatus + '"]').click()
        else:
            assert False
        time.sleep(1)

        how_soon_you_can_start = driver.find_element_by_xpath(Locators.how_soon_you_can_start).text
        if how_soon_you_can_start == 'How soon can you start? *':
            driver.find_element_by_xpath('//*[text()="' + howSoonCanYouStart + '"]').click()
        else:
            assert False
        time.sleep(1)

        capacity = driver.find_element_by_xpath(Locators.capacity).text
        if capacity == 'Capacity *':
            driver.find_element_by_xpath('//*[text()="' + capacity_value + '"]').click()
        else:
            assert False
        time.sleep(1)

        rate = driver.find_element_by_xpath(Locators.rate).text
        if rate == 'Rate *':
            driver.find_element_by_xpath('//*[text()="' + rate_value + '"]').click()
        else:
            assert False
        time.sleep(1)

        driver.find_element_by_class_name(Locators.currency).click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@title="' + currency_value + '"]').click()
        time.sleep(1)

        amount_value = driver.find_element_by_class_name('rate-input').text
        if amount_value != '':
            driver.find_element_by_xpath(Locators.amount).send_keys(Keys.CONTROL + "a")
            driver.find_element_by_xpath(Locators.amount).send_keys(Keys.DELETE)
            driver.find_element_by_xpath(Locators.amount).send_keys(amount_randomize)
            assert True
        else:
            driver.find_element_by_xpath(Locators.amount).send_keys(Keys.CONTROL + "a")
            driver.find_element_by_xpath(Locators.amount).send_keys(Keys.DELETE)
            driver.find_element_by_xpath(Locators.amount).send_keys(amount_randomize)

        time.sleep(2)
        if visibility == 'Public':
            assert True
        else:
            driver.find_element_by_xpath(Locators.select_private_or_public).click()
        time.sleep(1)

        submit_preference = driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard).text
        if submit_preference == 'Submit':
            driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard).click()
        elif submit_preference == 'Save and Go to dashboard':
            driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard).click()
            time.sleep(1)
        else:
            assert False

    def application_complete_modal(self):
        driver = self.driver
        try:
            modal_name = driver.find_element_by_xpath(Locators.modalname).text
            if modal_name=='Application complete':
                driver.find_element_by_xpath(Locators.Add_additional_info_button).click()
            else:
                assert False
        except:
            assert True
