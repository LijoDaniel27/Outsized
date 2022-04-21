from Locators.locators import Locators
from freelancerPages.work_preferencePage import Work_Preference
from freelancerPages.personal_informationPage import Personal_information
from freelancerPages.professional_informationPage import Professional_information
from freelancerPages.additional_informationPage import Additional_information

import time

class Profile_edit_by_icon():

    def __init__(self, driver):
        self.driver = driver

    #-------Work Preference Edit--------------------------------
    def work_preference_edit_icon(self):
        self.driver.find_element_by_xpath(Locators.work_preference_icon).click()
        driver = self.driver
        profile_edit_1 = Work_Preference(driver)
        profile_edit_1.workExperience()
        time.sleep(2)

    #-------Personal Information (About Us) Edit------------------
    def aboutus(self):
        self.driver.find_element_by_xpath(Locators.about_us_icon).click()
        driver = self.driver
        aboutus_edit_2 = Personal_information(driver)
        aboutus_edit_2.personal_information_screen()
        time.sleep(2)

    #-------Professional Information (Expertise)------------------
    def expertise(self):
        self.driver.find_element_by_xpath(Locators.expertise_icon).click()
        driver = self.driver
        expertise_edit_3 = Professional_information(driver)
        expertise_edit_3.professional_information_screen()
        expertise_edit_3.submit_button()
        driver.get("https://outsized.site/profile")
        time.sleep(3)

    #---------------Document and video----------------------------
    def document_and_video(self):
        self.driver.find_element_by_xpath(Locators.document_and_video_icon).click()
        driver = self.driver
        document_and_video_edit_4 = Additional_information(driver)
        document_and_video_edit_4.add_resume()
        document_and_video_edit_4.add_video()
        time.sleep(15)
        document_and_video_edit_4.save_button()

    #-------------Projects---------------------------------------
    def projects(self):
        self.driver.find_element_by_xpath(Locators.project_icon).click()
        time.sleep(3)
        driver = self.driver
        projects_edit_5 = Professional_information(driver)
        projects_edit_5.add_project()
        projects_edit_5.submit_button()
        driver.get("https://outsized.site/profile")
        time.sleep(2)