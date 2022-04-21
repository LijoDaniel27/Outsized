from Locators.locators import Locators
import time
import json
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
class HomePage():

    def __init__(self, driver):
        self.driver = driver

    #-------Check url ---------------------------------
    def check_profile_url(self):
        current_page = self.driver.current_url
        if current_page == 'https://outsized.site/profile':
            time.sleep(2)
            assert True
        else:
            assert False

    #-------Logout button-------------------------------
    def click_logout_link(self):
        self.driver.find_element_by_class_name(Locators.logout_link).click()

    # -------Update your profile button-------------------
    def click_update_your_profile(self):
        self.driver.find_element_by_xpath(Locators.update_a_profile).click()

    def click_fill_it_manually(self):
        self.driver.find_element_by_xpath(Locators.fill_it_manually).click()

    #-----------------------------------------------------
    def click_opportunties_tab(self):
        driver = self.driver

        def store_project_details(project_name,client_name):
            with open(Locators.json_path, 'r+') as f:
                data = json.load(f)
                testvalue = data["Staging"][0]
                testvalue["opporunitiesTab"][0]["projectName"] = project_name
                testvalue["opporunitiesTab"][0]["clientName"] = client_name
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

        opportunities_tab_text = driver.find_element(by=By.ID, value='rc-tabs-0-tab-2').text
        click_opportunities = driver.find_element(by=By.XPATH, value='(//*[@class="tab-content"])[2]').click()
        driver.assertEqual(opportunities_tab_text, ' Opportunities', click_opportunities)
        time.sleep(2)

        opportunities_projectName = driver.find_element(by=By.XPATH,value='(//*[@class="live-ops-title-subtitle"]//*[@class="ant-row"]//h3)[1]').text
        opportunities_client_name = driver.find_element(by=By.XPATH, value='(//*[@class="live-ops-title-subtitle"]//*[@class ="ant-row"]//*[@class="secondary-text"])[1]').text
        store_project_details(project_name = opportunities_projectName,client_name=opportunities_client_name)

        check_button_label = driver.find_element(by=By.XPATH, value='(//*[text()="Apply"])[1]').text
        click_apply_button = driver.find_element(by=By.XPATH, value='(//*[text()="Apply"])[1]').click()
        driver.assertEqual(check_button_label, 'Apply', click_apply_button)

        driver.switch_to.window(self.driver.window_handles[1])
        check_button_applyForProject_label = driver.find_element(by=By.XPATH,value='(//*[text()="Apply for project"])[1]').text
        click_button_applyForProject = driver.find_element(by=By.XPATH,value='(//*[text()="Apply for project"])[1]').click()
        driver.assertEqual(check_button_applyForProject_label, 'Apply for project', click_button_applyForProject)

    def submit_proposal(self):
        driver = self.driver

        check_submitProposal_text = driver.find_element(by=By.XPATH, value='//*[@class="title"]').text
        driver.assertEqual(check_submitProposal_text, 'Submit Proposal', 'Not matched the page')

        try:
            fileupload_status = driver.find_elements(by=By.XPATH,value='(//*[@class="questionnaire"]//*[@class="uploader-link-antd"]//*[@role="img"])')
            if len(fileupload_status) > 0:
                for a in range(1, len(fileupload_status) + 1):
                    driver.find_element(by=By.XPATH,value='(//*[@class="questionnaire"]//*[@class="uploader-link-antd"]//*[@role="img"])').click()
                    time.sleep(2)
                    driver.find_element(by=By.XPATH, value='(//*[@type="file"])[' + str(a) + ']').send_keys('D:/Testing/file/NewResume.pdf')
            else:
                assert False

            checkbox = len(driver.find_elements(by=By.CLASS_NAME, value="ant-checkbox-input"))
            for i in range(1, checkbox + 1):
                driver.find_element(by=By.XPATH,value='(//*[@class="questionnaire"]//*[@class="checkbox-question"]//*[@type="checkbox"])[' + str(i) + ']').click()
                time.sleep(1)
                driver.find_element(by=By.XPATH,value='(//*[@class="questionnaire"]//*[@class="checkbox-question"]//*[@type="checkbox"])[' + str(i) + ']').click()

            textarea = len(driver.find_elements(by=By.XPATH, value='//textarea[@class="ant-input"]'))
            for i in range(1, textarea + 1):
                driver.find_element(by=By.XPATH, value='(//*[@class="questionnaire"]//*[@class="ant-input"])[' + str(i) + ']').send_keys(Keys.CONTROL + "a")
                driver.find_element(by=By.XPATH, value='(//*[@class="questionnaire"]//*[@class="ant-input"])[' + str( i) + ']').send_keys(Keys.DELETE)
                driver.find_element(by=By.XPATH, value='(//*[@class="questionnaire"]//*[@class="ant-input"])[' + str(i) + ']').send_keys('Updated ' + Locators.about_project_value)
                time.sleep(2)

        except:
            uploadFile = len(driver.find_elements(by=By.XPATH, value="//*[text()=' Upload file ']"))
            for i in range(1, uploadFile + 1):
                driver.find_element(by=By.XPATH, value='(//*[@type="file"])[' + str(i) + ']').send_keys('D:/Testing/file/418558.pdf')
                time.sleep(2)

            checkbox = len(driver.find_elements(by=By.CLASS_NAME, value="ant-checkbox-input"))
            for i in range(1, checkbox + 1):
                driver.find_element(by=By.XPATH,value='(//*[@class="questionnaire"]//*[@class="checkbox-question"]//*[@type="checkbox"])[' + str(i) + ']').click()
                time.sleep(2)
                # driver.find_element(by=By.XPATH,value='(//*[@class="questionnaire"]//*[@class="checkbox-question"]//*[@type="checkbox"])[' + str(i) + ']').click()

            textarea = len(driver.find_elements(by=By.XPATH, value='//textarea[@class="ant-input"]'))
            for i in range(1, textarea + 1):
                driver.find_element(by=By.XPATH, value='(//*[@class="questionnaire"]//*[@class="ant-input"])[' + str(i) + ']').send_keys(Keys.CONTROL + "a")
                driver.find_element(by=By.XPATH, value='(//*[@class="questionnaire"]//*[@class="ant-input"])[' + str(i) + ']').send_keys(Keys.DELETE)
                driver.find_element(by=By.XPATH, value='(//*[@class="questionnaire"]//*[@class="ant-input"])[' + str(i) + ']').send_keys('New feed ' + Locators.about_project_value)
                time.sleep(2)

        element = driver.find_element(by=By.XPATH, value='//*[text()="Day"]')
        element_color = element.value_of_css_property('color')
        if element_color == 'rgba(72, 182, 203, 1)':
            driver.find_element(by=By.XPATH, value='//*[text()="Month"]').click()
        else:
            driver.find_element(by=By.XPATH, value='//*[text()="Day"]').click()

        try:
            driver.find_element_by_class_name("ant-select-selection-search").click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@title="INR (₹)"]').click()
            time.sleep(1)
        except:
            driver.find_element_by_class_name("ant-select-selector").click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@title="ZAR (R)"]').click()
            time.sleep(1)

        amount_value = driver.find_element_by_class_name('rate-input').text
        if amount_value != '':
            driver.find_element_by_id('//*[@placeholder="Rate"]').send_keys(Keys.CONTROL + "a")
            driver.find_element_by_id('//*[@placeholder="Rate"]').send_keys(Keys.DELETE)
            driver.find_element_by_id('//*[@placeholder="Rate"]').send_keys("20000")
            assert True
        else:
            driver.find_element_by_xpath('//*[@placeholder="Rate"]').send_keys(Keys.CONTROL + "a")
            driver.find_element_by_xpath('//*[@placeholder="Rate"]').send_keys(Keys.DELETE)
            driver.find_element_by_xpath('//*[@placeholder="Rate"]').send_keys("10000")
        time.sleep(3)

        submit_preference = driver.find_element_by_xpath('//button[@type="submit"]').is_enabled()
        if submit_preference == True:
            driver.find_element_by_xpath('//button[@type="submit"]').click()
            time.sleep(2)
        else:
            assert False

    def explore_more_opportunities(self):
        driver = self.driver
        time.sleep(2)
        modal_more_explore = driver.find_element_by_class_name('success-wrapper').is_displayed()
        if modal_more_explore == True:
            modal_confirm_text = driver.find_element_by_class_name('header').text
            if modal_confirm_text == 'Proposal Submitted Successfully':
                explore_more_button = driver.find_element_by_xpath('//*[text()="Explore More Opportunities"]').text
                if explore_more_button == 'Explore More Opportunities':
                    driver.find_element_by_xpath('//*[text()="Explore More Opportunities"]').click()
                    time.sleep(2)
                    driver.switch_to.window(self.driver.window_handles[1])
                else:
                    assert False
            else:
                assert False
        else:
            assert False

    def click_proposal_tab(self):
        driver = self.driver
        proposal_tab_text = driver.find_element(by=By.ID, value='rc-tabs-0-tab-3').text
        click_proposal_tab = driver.find_element(by=By.XPATH, value='(//*[@class="tab-content"])[3]')
        driver.assertEqual(proposal_tab_text, ' Proposal', click_proposal_tab.click())

        time.sleep(5)
        proposal_projectName = driver.find_element(by=By.XPATH,value='(//*[@class="live-ops-title-subtitle"]//*[@class="ant-row"]//h3)[1]').text
        proposal_clientName = driver.find_element(by=By.XPATH,value='(//*[@class="live-ops-title-subtitle"]//*[@class ="ant-row"]//*[@class="secondary-text"])[1]').text
        x = open(Locators.json_path, "r")
        a = (x.read())
        data = json.loads(a)
        testvalue = data["Staging"][0]
        project_name = testvalue["opporunitiesTab"][0]["projectName"]
        client_name = testvalue["opporunitiesTab"][0]["clientName"]

        print(proposal_projectName+"="+ project_name)
        print(proposal_clientName+"="+ client_name)

        if proposal_projectName == project_name and proposal_clientName == client_name:
            driver.find_element(by=By.XPATH, value='(//*[@class="ant-row"]//span[@role="img"])[1]').click()
        else:
            assert False

        submit_proposal = HomePage(driver)
        submit_proposal.submit_proposal()
        submit_proposal.explore_more_opportunities()