from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators
import time
import random
from selenium.common.exceptions import NoSuchElementException

class Professional_information():
    
    def __init__(self, driver):
        self.driver = driver

    def professional_information_screen(self):
        driver = self.driver
        #driver.get("https://outsized.site/create-profile/professional-information")

#-----------------------Professional Information-----------------------------------
        def professional_information():
            time.sleep(2)
            year_of_experience = driver.find_element_by_xpath(Locators.label_no_of_experience).text
            if year_of_experience == 'I have * years of professional experience.':
                driver.find_element_by_xpath(Locators.no_of_experience).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.no_of_experience).send_keys(Keys.DELETE)
                driver.find_element_by_xpath(Locators.no_of_experience).send_keys(Locators.experience)
            else:
                assert False

            # -------------------------------------------Skills------------------------------------------------------

            # ----------------Delete Skills---------------
            count_skill_len = driver.find_elements_by_xpath(Locators.count_skill_len)
            skill_length = len(count_skill_len)
            for x in range(skill_length):
                delete_str = str(x)
                delete_btn = Locators.count_skill_len+"['" + delete_str + "']"
                driver.find_element_by_xpath(delete_btn).click()
                time.sleep(1)

            # ----------------Add Skills------------------
            skill_length = len(Locators.areaOfExpertise)
            skills_label = driver.find_element_by_xpath(Locators.label_skills).text
            for x in range(0, skill_length):
                if skills_label == 'Area of expertise (skills) *':
                    skill_value = Locators.areaOfExpertise[x]["skill"]
                    driver.find_element_by_xpath(Locators.area_of_expertise_1).send_keys(skill_value.strip())
                    time.sleep(2)
                    try:
                        driver.find_element_by_class_name(Locators.skilll_added_container)
                        driver.find_element_by_xpath(Locators.add_new_skill).click()
                        time.sleep(2)
                        driver.find_element_by_xpath(Locators.add_new_skill_button).click()
                    except:
                        skill_select = '//*[@title="' + skill_value.strip() + '"]'
                        driver.find_element_by_xpath(skill_select).click()
                else:
                    assert False
            # -------------------------------------------Industeries------------------------------------------------

            # ----------------Delete Industeries---------------

            count_industeries_len = driver.find_elements_by_xpath(Locators.count_industries_len)
            industeries_len = len(count_industeries_len)
            for y in range(1, industeries_len + 1):
                delete_industeries_str = str(y)
                delete_btn2 = Locators.count_industries_len+"['" + delete_industeries_str + "']"
                driver.find_element_by_xpath(delete_btn2).click()
                time.sleep(1)
            time.sleep(2)

            # ----------------Add Industeries-------------------
            industeries_worked_length = len(Locators.industriesWorked)
            industeries = driver.find_element_by_xpath(Locators.label_industries).text
            for x in range(1, industeries_worked_length):
                if industeries == "Industries worked in *":
                    organisationname_value = Locators.industriesWorked[x]["industries"]
                    driver.find_element_by_xpath(Locators.industeries_1).send_keys(organisationname_value.strip())
                    time.sleep(2)
                    try:
                        driver.find_element_by_class_name(Locators.industries_added_container)
                        driver.find_element_by_xpath(Locators.add_new_industry).click()
                        time.sleep(2)
                        driver.find_element_by_xpath(Locators.add_new_industry_button).click()
                    except:
                        industeries_select = '//*[@title="' + organisationname_value.strip() + '"]'
                        driver.find_element_by_xpath(industeries_select).click()
                else:
                    assert False
        professional_information()

#----------------------------Add Project---------------------------------------------------
    def add_project(self):
        driver = self.driver
        #driver.get("https://outsized.site/create-profile/professional-information")

        def addproject(a):
            time.sleep(2)
            client_name = driver.find_element_by_xpath(Locators.label_clientname).text
            if client_name == 'Client name *':
                driver.find_element_by_xpath(Locators.project_client_name).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.project_client_name).send_keys(Keys.DELETE)
                if Locators.clientName[a]["clientName"] == None:
                    assert True
                else:
                    driver.find_element_by_xpath(Locators.project_client_name).send_keys(Locators.clientName[a]["clientName"])
            else: assert True

            company_logo = driver.find_element_by_xpath(Locators.label_company_logo).text
            if company_logo == 'Company Logo':
                logo_url = Locators.project_logo_path
                logo_name = "logo"
                logo_extension = ".jpg"
                select_random = random.randrange(1, 5)
                logo_item = (str(select_random))
                item = logo_item
                logo_add = logo_url + logo_name + item + logo_extension
                driver.find_element_by_xpath(Locators.project_logo).send_keys(logo_add)
                driver.implicitly_wait(5)
                time.sleep(2)
                driver.find_element_by_xpath(Locators.company_logo_ok_button).click()
                time.sleep(1)
            else:
                assert False

            project_location = driver.find_element_by_xpath(Locators.label_city).text
            if project_location == 'Project location':
                time.sleep(2)
                driver.find_element_by_xpath(Locators.project_city).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.project_city).send_keys(Keys.DELETE)
                if Locators.projectLocation[a]["projectLocation"] == None:
                    assert True
                else:
                    driver.find_element_by_xpath(Locators.project_city).send_keys(Locators.projectLocation[a]["projectLocation"])
                try:
                    dropdown_element = driver.find_element_by_xpath(Locators.project_city_select)
                except NoSuchElementException:
                    dropdown_element = "No dropdown element found"
                if dropdown_element == "No dropdown element found":
                    assert True
                else:
                    driver.find_element_by_xpath(Locators.project_city_select).click()
                time.sleep(2)
            else:
                assert False

            project_title_name = driver.find_element_by_xpath(Locators.label_project).text
            if project_title_name == 'Project title *':
                time.sleep(2)
                driver.find_element_by_xpath(Locators.project_title).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.project_title).send_keys(Keys.DELETE)
                if Locators.projectTitle[a]["projectLocation"] == None:
                    assert True
                else:
                    driver.find_element_by_xpath(Locators.project_title).send_keys(Locators.projectTitle[a]["projectTitle"])
                time.sleep(2)
            else:
                assert False

            start_date = driver.find_element_by_xpath(Locators.label_startdate).text
            if start_date == 'Start Date':
                time.sleep(1)
                driver.find_element_by_xpath(Locators.project_select_from_date).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.project_select_from_date).send_keys(Keys.DELETE)
                driver.find_element_by_xpath(Locators.project_select_from_date).click()
                time.sleep(1)
                startdate = driver.find_element_by_class_name(Locators.date_prev_icon_click)
                for x in range(6):
                    startdate.click()
                driver.find_element_by_xpath(Locators.from_date_click).click()
                end_date = driver.find_element_by_xpath(Locators.label_enddate).text
                if end_date == 'End Date':
                    time.sleep(1)
                    driver.find_element_by_xpath(Locators.project_select_to_date).send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_xpath(Locators.project_select_to_date).send_keys(Keys.DELETE)
                    driver.find_element_by_xpath(Locators.project_select_to_date).click()
                    time.sleep(2)
                    driver.find_element_by_link_text(Locators.date_click).click()
                    time.sleep(1)
            else:
                assert False

            skill_demonstrated = driver.find_element_by_xpath(Locators.label_skill_demostrated).text
            skill_length = len(Locators.skilldemonstrated_count)
            if skill_demonstrated == 'Skills demonstrated *':
                try:
                    skill_added = driver.find_element_by_xpath(Locators.project_skill_added_container)
                except NoSuchElementException:
                    skill_added = "Element does not exist"
                if skill_added == "Element does not exist":
                    for x in range(skill_length):
                        driver.find_element_by_xpath(Locators.skills_demonstrated).send_keys(Locators.skilldemonstrated[a]["skilldemonstrated"][x]["skill"])
                        time.sleep(3)
                        driver.find_element_by_xpath('(//*[@title="' + Locators.skilldemonstrated[a]["skilldemonstrated"][x]["skill"] + '"])').click()
                        time.sleep(1)
                else:
                    chk = driver.find_elements_by_xpath(Locators.count_project_skill_len)
                    length_value = len(chk)
                    for x in range(length_value):
                        driver.find_element_by_xpath(Locators.count_project_skill_len + '[1]').click()
                    time.sleep(2)

                    for x in range(skill_length):
                        driver.find_element_by_xpath(Locators.skills_demonstrated).send_keys(Locators.skilldemonstrated[a]["skilldemonstrated"][x]["skill"])
                        time.sleep(1)
                        try:
                            dropdown_element = driver.find_element_by_xpath( '(//*[@title="' + Locators.skilldemonstrated[a]["skilldemonstrated"][x]["skill"] + '"])')
                        except NoSuchElementException:
                            dropdown_element = "No dropdown element found"
                        if dropdown_element == "No dropdown element found":
                            assert True
                        else:
                            driver.find_element_by_xpath('(//*[@title="' + Locators.skilldemonstrated[a]["skilldemonstrated"][x]["skill"] + '"])').click()
            else:
                assert False

            time.sleep(1)
            project_brief = driver.find_element_by_xpath(Locators.label_brief).text
            if project_brief == 'Project brief':
                driver.find_element_by_xpath(Locators.about_project).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.about_project).send_keys(Keys.DELETE)
                driver.find_element_by_xpath(Locators.about_project).send_keys(Locators.projectBrief[a]["projectBrief"])
            else:
                assert False

            modal_title = driver.find_element_by_xpath(Locators.project_modal_title).text
            if modal_title == 'Edit Project':
                update_a_project = driver.find_element_by_xpath(Locators.update_project_button).text
                if update_a_project == 'Update':
                    driver.find_element_by_xpath(Locators.update_project_button).click()
                else:
                    assert False
            else:
                submit_a_project = driver.find_element_by_xpath(Locators.save_project_button).text
                if submit_a_project == 'Add':
                    driver.find_element_by_xpath(Locators.save_project_button).click()
                else:
                    assert False

        # -------------------------------------Add Projects------------------------------------------------------
        project_data = len(Locators.projectData)
        for x in range(project_data):
            try:
                add_more = driver.find_element_by_xpath(Locators.project_add_more_button).text
                if add_more == 'Add more':
                    time.sleep(3)
                    driver.find_element_by_xpath(Locators.project_add_more_button).click()
                    time.sleep(1)
                    try:
                        modal_title = driver.find_element_by_xpath(Locators.project_modal_title).text
                        if modal_title == 'Add a new project':
                            driver.find_element_by_id(Locators.project_select).click()
                            time.sleep(1)
                            driver.find_element_by_xpath(Locators.project_add_manually).click()
                            addproject(a=x)
                        else:
                            assert False
                    except:
                        modal_title = driver.find_element_by_xpath(Locators.project_modal_title).text
                        if modal_title == 'Add a new project':
                            addproject(a=x)
                        else:
                            assert False
                else:
                    assert False
            except:
                add_project = driver.find_element_by_xpath(Locators.add_project_button).text
                if add_project == 'Add Project':
                    driver.find_element_by_xpath(Locators.add_project_button).click()
                    time.sleep(2)
                    try:
                        modal_title = driver.find_element_by_xpath(Locators.project_modal_title).text
                        if modal_title == 'Add a new project':
                            driver.find_element_by_id(Locators.project_select).click()
                            time.sleep(1)
                            driver.find_element_by_xpath(Locators.project_add_manually).click()
                            addproject(a=x)
                        else:
                            assert False
                    except:
                        addproject(a=x)
                else:
                    assert False

        # ----------------------------------Edit Project---------------------------------------------------------
        time.sleep(2)
        driver.find_element_by_xpath(Locators.project_edit_icon).click()
        time.sleep(2)
        modal_title = driver.find_element_by_xpath(Locators.project_modal_title).text
        if modal_title == 'Edit Project':
            addproject(a=1)
        else:
            assert False

         # --------------------------------Delete Project---------------------------------------------------------
        time.sleep(2)
        driver.find_element_by_xpath(Locators.project_delete_icon).click()
        confirm_delete_modal = driver.find_element_by_id(Locators.confirm_delete_modal).text
        if confirm_delete_modal == 'Confirm Delete':
            driver.find_element_by_xpath(Locators.modal_delete_button).click()
            time.sleep(2)
        else:
            assert False

#---------------------Submit button-------------------------------------------------------------------------
    def submit_button(self):
        def submit_next_button():
            driver = self.driver
            savenext_button = driver.find_element_by_xpath(Locators.save_and_next_button)
            css_color1 = savenext_button.value_of_css_property('background-color')
            if css_color1 == 'rgba(149, 204, 73, 1)':
                driver.find_element_by_xpath(Locators.save_next_button).click()
                time.sleep(2)
            else:
                assert False
        submit_next_button()
