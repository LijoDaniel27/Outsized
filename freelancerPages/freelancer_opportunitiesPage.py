import time
class Opportunities_tab():

    def __init__(self, driver):
        self.driver = driver

    def opportunities(self):
        driver = self.driver
        driver.get('https://home.outsized.site/live-opportunities/submit-proposal?project=1069')

        #--------------------------sample--------------------------------

        no_of_questionnaire = driver.find_elements_by_xpath('//*[@class="questionnaire"]')
        a = len(no_of_questionnaire)
        for i in range(1, a + 1):
            range_i =str(i)
            if driver.find_element_by_xpath('(//*[@class="questionnaire"])['+range_i+']'):
                try:
                    if driver.find_element_by_xpath('((//*[@class="questionnaire"])[' + range_i + ']//*[@class="ant-checkbox-input"])'):
                        driver.find_element_by_xpath('((//*[@class="questionnaire"])[' + range_i + ']//*[@class="ant-checkbox-input"])').click()
                    elif driver.find_element_by_xpath('((//*[@class="questionnaire"])[' + range_i + ']//*[@type="file"])'):
                        driver.find_element_by_xpath('((//*[@class="questionnaire"])[' + range_i + ']//*[@type="file"])').send_keys('C:/Users/Administrator/PythonProject/POM/file/418558.pdf')
                except:
                    driver.find_element_by_xpath('((//*[@class="questionnaire"])[' + range_i + ']//*[@placeholder="Answer"])').send_keys('TESTING ')

            else:
                assert False
        time.sleep(3)


        # label = driver.find_element_by_xpath(Locators.opportunities_label).text
        # if label == 'Interesting projects on the platform':
        #    project_name = driver.find_element_by_xpath(Locators.project_name_label).text
        #    driver.find_element_by_xpath(Locators.opportunities_apply_button).click()
        #    website_project_name = driver.find_element_by_class_name(Locators.website_project_name).text
        #    if project_name == website_project_name:
        #        driver.find_element_by_xpath(Locators.website_apply_button).click()
        #        submit_proposal = driver.find_element_by_class_name('title').text
        #        if submit_proposal == 'Submit Proposal':
        #            test = driver.find_elements_by_xpath('//*[@class="questionnaire"]')
        #            a = len(test)
        #            for x in range(1, a + 1):
        #                print(x)
        #
        #            time.sleep(5)
        #        else:
        #            assert False
        #
        #        # time.sleep(2)
        #        # url_check = driver.current_url
        #        # print(url_check)
        #    else:
        #        assert False
        # else:
        #     assert False