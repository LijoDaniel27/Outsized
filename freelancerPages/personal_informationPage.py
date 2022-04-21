from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators
import time
import random

class Personal_information():

    def __init__(self, driver):
        self.driver = driver

    def personal_information_screen(self):
        driver = self.driver
        #driver.get('https://outsized.site/create-profile/personal-information')
        #driver.get('https://outsized.site/create-profile/personal-information?email=lijo420%40mailinator.com')

        def personal_information():
            # ----------------profile photo-------------------
            photo_url = Locators.profile_upload_path
            photo_name = "profile"
            photo_extension = ".jpg"
            select_random = random.randrange(1, 9)
            item = (str(select_random))
            if item != " ":
                photo_add = photo_url + photo_name + item + photo_extension
            else:
                assert False
            driver.find_element_by_xpath(Locators.profile_upload).send_keys(photo_add)
            time.sleep(2)
            ok_button = driver.find_element_by_xpath(Locators.ok_button).is_enabled()
            if ok_button == True:
                driver.find_element_by_xpath(Locators.ok_button).click()
            else:
                assert False
            # ------------------------------------------------------

            time.sleep(2)
            first_name_label = driver.find_element_by_xpath(Locators.label_firstname).text
            if first_name_label == 'First Name':
                driver.find_element_by_xpath(Locators.text_first_name).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.text_first_name).send_keys(Keys.DELETE)
                if Locators.firstname == None:
                    assert True
                else:
                    driver.find_element_by_xpath(Locators.text_first_name).send_keys(Locators.enterManually_firstName+Locators.randomname)
            else:
                assert False

            last_name_label = driver.find_element_by_xpath(Locators.label_last_name).text
            if last_name_label == 'Last Name':
                driver.find_element_by_xpath(Locators.text_last_name).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.text_last_name).send_keys(Keys.DELETE)
                if Locators.lastname == None:
                    assert True
                else:
                    driver.find_element_by_xpath(Locators.text_last_name).send_keys(Locators.lastname)
            else:
                assert False

            headline_label = driver.find_element_by_xpath(Locators.label_headline).text
            if headline_label == 'Headline *':
                driver.find_element_by_id(Locators.headline_textbox).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_id(Locators.headline_textbox).send_keys(Keys.DELETE)
                if Locators.headline == None:
                    assert True
                else:
                    driver.find_element_by_id(Locators.headline_textbox).send_keys(Locators.headline)
            else:
                assert False

            linkedinlabel = driver.find_element_by_xpath(Locators.label_linkedin).text
            if linkedinlabel == 'LinkedIn Profile *':
                time.sleep(2)
                driver.find_element_by_id(Locators.linkedin_textbox).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_id(Locators.linkedin_textbox).send_keys(Keys.DELETE)
                if Locators.linkedinProfile == None:
                    assert True
                else:
                    driver.find_element_by_id(Locators.linkedin_textbox).send_keys(Locators.linkedinProfile)
            else:
                assert False

            city_label = driver.find_element_by_xpath(Locators.label_location).text
            if city_label == 'City':
                driver.find_element_by_xpath(Locators.city_textbox).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.city_textbox).send_keys(Keys.DELETE)
                if Locators.city == None:
                    assert True
                else:
                    driver.find_element_by_xpath(Locators.city_textbox).send_keys(Locators.city)
                    time.sleep(2)
                    driver.find_element_by_xpath(Locators.city_select).click()
                time.sleep(2)
            else:
                assert False

            driver.find_element_by_xpath(Locators.select_country_code).click()
            time.sleep(1)
            driver.find_element_by_xpath(Locators.select_indian_code).click()
            mobile_label = driver.find_element_by_xpath(Locators.label_mobile).text
            if mobile_label == 'Mobile Number':
                driver.find_element_by_xpath(Locators.mobile_textbox).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.mobile_textbox).send_keys(Keys.DELETE)
                if Locators.mobile == None:
                    assert True
                else:
                    driver.find_element_by_xpath(Locators.mobile_textbox).send_keys(str(Locators.mobile))
            else:
                assert False

            about_you_label = driver.find_element_by_xpath(Locators.label_about).text
            if about_you_label == 'About you':
                driver.find_element_by_id(Locators.about_textbox).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_id(Locators.about_textbox).send_keys(Keys.DELETE)
                if Locators.aboutYou == None:
                    assert True
                else:
                    driver.find_element_by_id(Locators.about_textbox).send_keys(Locators.aboutYou)
                    time.sleep(2)
            else:
                assert False

            savenext_button = driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard).text
            savenext_css = driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard)
            check_url = driver.current_url
            css_color1 = savenext_css.value_of_css_property('background-color')
            if check_url == Locators.about_us_url:
                # if save_and_goto_dashboard == 'Save and Go to dashboard':
                driver.find_element_by_xpath('(//*[@class="css-wk2kap-commonButtonStyle"])[2]').click()
                time.sleep(2)
            else:
                if css_color1 == 'rgba(149, 204, 73, 1)':
                    if savenext_button == 'Submit':
                        driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard).click()
                    elif savenext_button == 'Save & Next':
                        driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard).click()
                else:
                    assert False

        personal_information()

