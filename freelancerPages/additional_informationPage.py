from selenium.webdriver.common.keys import Keys
from Locators.locators import Locators
import time
from selenium.common.exceptions import NoSuchElementException

class Additional_information():

    def __init__(self, driver):
        self.driver = driver

    #------------------------- Resume upload file -----------------------
    def add_resume(self):
        driver = self.driver
        driver.get('https://outsized.site/create-profile/experience')

        def resumeFileUpload():
            driver.find_element_by_xpath(Locators.resume_file_upload).send_keys(Locators.resumeUploadFile)
        time.sleep(2)
        additional_information_header = driver.find_element_by_xpath(Locators.additional_information_header).text
        if additional_information_header == "Additional Information":
            resume_text = driver.find_element_by_xpath(Locators.resume_text).text
            if resume_text == 'We’d like to get to know you better. Please supply us with the following information.':
                try:
                    l = driver.find_element_by_class_name('uploaded-file-name')
                except NoSuchElementException:
                    l = "Element does not exist"
                if l == "Element does not exist":
                    resumeFileUpload()
                else:
                    uploaded_content = driver.find_element_by_xpath(Locators.uploaded_content).text
                    if uploaded_content == 'Attached Files':
                        uploaded_file_name = driver.find_element_by_class_name(Locators.uploaded_file_name).text
                        if uploaded_file_name != "":
                            driver.find_element_by_xpath(Locators.remove_uploaded_file).click()
                            time.sleep(2)
                            resumeFileUpload()
                        else:
                            assert False
                    else:
                        assert False
            else:
                assert False
        else:
            assert False

    # ------------------------- Video upload file -----------------------
    def add_video(self):
        driver = self.driver

        def resumeVideoUpload():
            time.sleep(2)
            driver.find_element_by_class_name('ba-videorecorder-chooser-button-0').click()
            time.sleep(1)
            error_message = driver.find_element_by_class_name('ba-videorecorder-message-message').text
            if error_message == 'Access to the media was forbidden. Click to retry.':
                driver.find_element_by_xpath("//*[text()='Cancel']").click()
                time.sleep(2)
                upload_video = driver.find_element_by_class_name(Locators.upload_video_text).text
                if upload_video == 'Upload Video':
                    driver.implicitly_wait(20)
                    driver.find_element_by_xpath(Locators.resume_video).send_keys(Locators.resume_video_path)
                    #time.sleep(20)
                else:
                    assert False
            else:
                assert False

        resume_video = driver.find_element_by_xpath(Locators.resume_video_text).text
        if resume_video == 'Record two-minute videos about yourself to help us get to get know you better':
            try:
                l = driver.find_element_by_class_name('delete-btn')
            except NoSuchElementException:
                l = "Element does not exist"
            if l == "Element does not exist":
                resumeVideoUpload()
            else:
                driver.find_element_by_class_name(Locators.remove_video_uploaded_file).click()
                time.sleep(2)
                confirm_delete_modal = driver.find_element_by_id(Locators.modal_title).text
                if confirm_delete_modal == 'Confirm Delete':
                    driver.find_element_by_xpath(Locators.modal_delete_button).click()
                else:
                    assert False
                resumeVideoUpload()
        else:
            assert False

    # ------------------------- Education-------------------------------------------------------
    def education(self):
        driver = self.driver
        driver.get('https://outsized.site/create-profile/experience')
        def add_education(a):
            date = Locators.issueDate[a]["issueDate"]
            passout_year_select = '(//*[@class="ant-picker-content"])//*[@title="' + str(date) + '"]'

            education_modal = driver.find_element_by_class_name('ant-modal-title').text
            degree_label = driver.find_element_by_xpath('//*[@for="degree"]').text

            if degree_label == 'Degree or Qualification':
                degree_value = '//*[@title="' + Locators.degreeOrQualification[a]["degreeOrQualification"] + '"]'
                driver.find_element_by_xpath(Locators.degree).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.degree).send_keys(Keys.DELETE)
                driver.find_element_by_xpath(Locators.degree).send_keys(Locators.degreeOrQualification[a]["degreeOrQualification"])
                time.sleep(2)
                driver.find_element_by_xpath(degree_value).click()

                institute_label = driver.find_element_by_xpath('//*[@for="institute"]').text
                if institute_label == 'Institute or Issuing Authority':
                    institute_select = "//*[@title='" + Locators.institute[a]["institute"] + "']"
                    time.sleep(2)
                    driver.find_element_by_xpath(Locators.university).send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_xpath(Locators.university).send_keys(Keys.DELETE)
                    driver.find_element_by_xpath(Locators.university).send_keys(Locators.institute[a]["institute"])
                    time.sleep(2)
                    driver.find_element_by_xpath(institute_select).click()

                    location_label = driver.find_element_by_xpath('//*[@for="location"]').text
                    if location_label == 'Location':
                        driver.find_element_by_xpath(Locators.university_location).send_keys(Keys.CONTROL + "a")
                        driver.find_element_by_xpath(Locators.university_location).send_keys(Keys.DELETE)
                        driver.find_element_by_xpath(Locators.university_location).send_keys(Locators.location[a]["location"])
                        time.sleep(2)
                        driver.find_element_by_xpath(Locators.university_location_select).click()

                        pass_year = driver.find_element_by_xpath('//*[@for="passOutYear"]').text
                        if pass_year == 'Issue Date':
                            if education_modal == 'Edit Education':
                                driver.find_element_by_class_name('ant-picker-clear').click()
                                driver.find_element_by_id(Locators.passout_year).click()
                                time.sleep(2)
                                year = driver.find_element_by_class_name('ant-picker-header-view').text
                                time.sleep(2)
                                if year == "2020-2029":
                                    driver.find_element_by_class_name('ant-picker-header-super-prev-btn').click()
                                    time.sleep(3)
                                    year = driver.find_element_by_class_name('ant-picker-decade-btn').text
                                    if year == "2010-2019":
                                        driver.find_element_by_xpath(passout_year_select).click()
                                    else:
                                        assert False
                                    time.sleep(1)
                                else:
                                    assert False
                            else:
                                driver.find_element_by_id(Locators.passout_year).click()
                                time.sleep(2)
                                year = driver.find_element_by_class_name('ant-picker-header-view').text
                                time.sleep(2)
                                if year == "2020-2029":
                                    driver.find_element_by_class_name('ant-picker-header-super-prev-btn').click()
                                    time.sleep(3)
                                    year = driver.find_element_by_class_name('ant-picker-decade-btn').text
                                    if year == "2010-2019":
                                        driver.find_element_by_xpath(passout_year_select).click()
                                    else:
                                        assert False
                                    time.sleep(1)
                                else:
                                    assert False

                            description_label = driver.find_element_by_xpath('//*[@for="description"]').text
                            if description_label == "Description":
                                driver.find_element_by_id(Locators.education_description).send_keys(Keys.CONTROL + "a")
                                driver.find_element_by_id(Locators.education_description).send_keys(Keys.DELETE)
                                driver.find_element_by_id(Locators.education_description).send_keys(Locators.description[a]["description"])

                                if education_modal == 'Add Education':
                                    submit_button = driver.find_element_by_xpath('(//*[text()="Submit"])').text
                                    if submit_button == 'Submit':
                                        driver.find_element_by_xpath(Locators.submit_button).click()
                                else:
                                    update_button = driver.find_element_by_xpath('(//*[text()="Update"])').text
                                    if update_button == 'Update':
                                        driver.find_element_by_xpath(Locators.update_button).click()
                            else:
                                assert False
                        else:
                            assert False
                    else:
                        assert False
                else:
                    assert False
            else:
                assert False

        # -------------------------------Delete Education------------------------
        def delete_education():
            time.sleep(2)
            count_education = len(driver.find_elements_by_xpath('(//*[@class="additional-into-item qualification"])//*[@aria-label="delete"]'))
            for x in range(count_education):
                driver.find_element_by_xpath('(//*[@class="additional-into-item qualification"])[1]//*[@aria-label="delete"]').click()
                confirm_delete_modal = driver.find_element_by_id('alert-dialog-title').text
                if confirm_delete_modal == 'Confirm Delete':
                    driver.find_element_by_xpath('//*[text()="Delete"]').click()
                    time.sleep(2)
                else:
                    assert False

        delete_education()
        #-------------------------------------Add Education----------------------------------------------------
        time.sleep(2)
        section_title_1 = driver.find_element_by_xpath('(//*[@class="section-title"])[1]').text
        if section_title_1 == 'Education':
            n = len(Locators.education)
            for x in range(n):
                try:
                    add_education_button = driver.find_element_by_xpath('//*[text()="Add Education"]').text
                    if add_education_button == 'Add Education':
                        driver.find_element_by_xpath('//*[text()="Add Education"]').click()
                        add_education(a=x)
                    else:
                        assert False
                except:
                    add_more_1 = driver.find_element_by_xpath('(//*[text()="Add more"])[1]').text
                    if add_more_1 == "Add more":
                        driver.find_element_by_xpath('(//*[text()="Add more"])[1]').click()
                        time.sleep(2)
                        add_education(a=x)
                    else:
                        assert False
        else:
            assert False

        # ------------------------------Edit Education---------------------------
        time.sleep(2)
        driver.find_element_by_xpath('(//*[@class="additional-into-item qualification"]//*[@class="action-btn-container"])[1]//*[@aria-label="edit"][1]').click()
        modal_title = driver.find_element_by_xpath('(//*[@class="ant-modal-title"])[1]').text
        time.sleep(2)
        print(modal_title)
        if modal_title == 'Edit Education':
            add_education(a=0)
        else:
            assert False

    # -------------------------Certificate-------------------------------------------------------
    def certificate(self):
        driver = self.driver
        def add_certificate(a):
            time.sleep(2)
            certificate_modal = driver.find_element_by_class_name('ant-modal-title').text
            certificate_name_label = driver.find_element_by_xpath('//*[@for="certificateName"]').text
            if certificate_name_label == "Certification Name":
                driver.find_element_by_id(Locators.certificate_name).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_id(Locators.certificate_name).send_keys(Keys.DELETE)
                driver.find_element_by_id(Locators.certificate_name).send_keys(Locators.certificateName[a]["certificateName"])
                issuing_label = driver.find_element_by_xpath('//*[@for="authority"]').text

                if issuing_label == "Issuing Organization":
                    driver.find_element_by_id(Locators.authority).send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_id(Locators.authority).send_keys(Keys.DELETE)
                    driver.find_element_by_id(Locators.authority).send_keys(Locators.issuingOrganization[a]["issuingOrganization"])
                    fromdate = driver.find_element_by_xpath('//*[@for="fromDate"]').text

                    if fromdate == "Issue Date":
                        driver.find_element_by_id(Locators.certificate_from_date).click()
                        driver.find_element_by_class_name(
                            Locators.certificate_from_date_super_previous_icon).click()
                        driver.find_element_by_class_name(
                            Locators.certificate_from_date_previous_icon).click()
                        time.sleep(2)
                        driver.find_element_by_xpath(Locators.certificate_from_date_select).click()
                        todate = driver.find_element_by_xpath('//*[@for="toDate"]').text

                        if todate == "Expiration Date":
                            driver.find_element_by_id(Locators.certificate_to_date).click()
                            time.sleep(2)
                            driver.find_element_by_xpath(Locators.certificate_to_date_previous_icon).click()
                            time.sleep(2)
                            driver.find_element_by_xpath(Locators.certificate_to_date_select).click()

                            if certificate_modal == 'Add Certification':
                                submit_button = driver.find_element_by_xpath('(//*[text()="Submit"])').text
                                if submit_button == 'Submit':
                                    driver.find_element_by_xpath(Locators.submit_button).click()
                                    time.sleep(2)
                                else:
                                    assert False
                            else:
                                update_button = driver.find_element_by_xpath('(//*[text()="Update"])').text
                                if update_button == 'Update':
                                    driver.find_element_by_xpath(Locators.update_button).click()
                                    time.sleep(2)
                                else:
                                    assert False
                        else:
                            assert False
                    else:
                        assert False
                else:
                    assert False
            else:
                assert False

        # ------------------------------Delete Certificate------------------------------------------------------
        def delete_certificate():
            time.sleep(2)
            count_certificate = len(driver.find_elements_by_xpath('(//*[@class="additional-into-item certificate"])//*[@aria-label="delete"]'))
            for x in range(count_certificate):
                driver.find_element_by_xpath('(//*[@class="info-card certificate"])[1]//*[@aria-label="delete"]').click()
                confirm_delete_modal = driver.find_element_by_id('alert-dialog-title').text
                if confirm_delete_modal == 'Confirm Delete':
                    driver.find_element_by_xpath('//*[text()="Delete"]').click()
                    time.sleep(2)
                else:
                    assert False

        delete_certificate()

        #---------------------------Add Certficate-------------------------------------------------
        section_title_2 = driver.find_element_by_xpath('(//*[@class="section-title"])[2]').text
        if section_title_2 == 'Certificate':
            n = len(Locators.certificate)
            for x in range(n):
                try:
                    add_qualification_button = driver.find_element_by_xpath('//*[text()="Add Certificate"]')
                    if add_qualification_button == 'Add Certificate':
                        driver.find_element_by_xpath('//*[text()="Add Certificate"]').click()
                        add_certificate(a=x)
                    else:
                        assert False
                except:
                    button_click_2 = driver.find_element_by_xpath('(//*[text()="Add more"])[2]').text
                    if button_click_2 == "Add more":
                        driver.find_element_by_xpath('(//*[text()="Add more"])[2]').click()
                        time.sleep(2)
                        add_certificate(a=x)
                    else:
                        assert False
        else:
            assert False

        #--------------------------------Edit Certificate------------------------------------------------------
        time.sleep(2)
        driver.find_element_by_xpath('(//*[@class="additional-into-item certificate"]//*[@class="action-btn-container"])[1]//*[@aria-label="edit"][1]').click()
        time.sleep(2)
        certificate_modal = driver.find_element_by_class_name('ant-modal-title').text
        if certificate_modal == 'Edit Certification':
            add_certificate(a=0)
        else:
            assert False

    #-------------------------Work Experience----------------------------------
    def work_experience(self):
        driver = self.driver
        #driver.get('https://outsized.site/create-profile/experience')

        def add_work_experience(a):
            position_name_label = driver.find_element_by_xpath('//*[@for="designation"]').text
            if position_name_label == "Position":
                driver.find_element_by_xpath(Locators.position).send_keys(Keys.CONTROL + "a")
                driver.find_element_by_xpath(Locators.position).send_keys(Keys.DELETE)
                driver.find_element_by_xpath(Locators.position).send_keys(Locators.workExperience_position[a]["position"])

                company_label = driver.find_element_by_xpath('//*[@for="companyName"]').text
                if company_label == "Company":
                    driver.find_element_by_xpath(Locators.company).send_keys(Keys.CONTROL + "a")
                    driver.find_element_by_xpath(Locators.company).send_keys(Keys.DELETE)
                    driver.find_element_by_xpath(Locators.company).send_keys(Locators.company_experience[a]["company"])

                    location_label = driver.find_element_by_xpath('//*[@for="location"]').text
                    if location_label == 'Location':
                        driver.find_element_by_xpath(Locators.expereince_location).send_keys(Keys.CONTROL + "a")
                        driver.find_element_by_xpath(Locators.expereince_location).send_keys(Keys.DELETE)
                        driver.find_element_by_xpath(Locators.expereince_location).send_keys(Locators.location_experience[a]["location"])
                        time.sleep(2)
                        driver.find_element_by_xpath('((//*[@class="rc-virtual-list"])[1]//*[@class="ant-select-item-option-content"])[1]').click()

                        fromdate = driver.find_element_by_xpath('//*[@for="fromDate"]').text
                        if fromdate == "Start Date":
                            driver.find_element_by_id(Locators.experience_from_date).click()
                            driver.find_element_by_class_name(Locators.experience_from_date_super_prev_icon).click()
                            driver.find_element_by_class_name(Locators.experience_from_date_prev_icon).click()
                            time.sleep(2)
                            driver.find_element_by_xpath(Locators.experience_from_date_select).click()
                            todate = driver.find_element_by_xpath('//*[@for="toDate"]').text
                            if todate == "End Date":
                                driver.find_element_by_id(Locators.experience_to_date).click()
                                time.sleep(2)
                                driver.find_element_by_xpath(Locators.experience_to_date_prev_icon).click()
                                time.sleep(2)
                                driver.find_element_by_xpath(Locators.experience_to_date_select).click()
                                description = driver.find_element_by_xpath('//*[@for="description"]').text
                                if description == 'Description':
                                    driver.find_element_by_id(Locators.experience_descripton).send_keys(
                                        Keys.CONTROL + "a")
                                    driver.find_element_by_id(Locators.experience_descripton).send_keys(Keys.DELETE)
                                    driver.find_element_by_id(Locators.experience_descripton).send_keys(Locators.description_experience[a]["description"])

                                    experience_modal = driver.find_element_by_class_name('ant-modal-title').text
                                    if experience_modal == 'Add Experience':
                                        submit_button = driver.find_element_by_xpath('(//*[text()="Submit"])').text
                                        if submit_button == 'Submit':
                                            driver.find_element_by_xpath(Locators.submit_button).click()
                                            time.sleep(3)
                                        else:
                                            assert False
                                    else:
                                        update_button = driver.find_element_by_xpath('(//*[text()="Update"])').text
                                        if update_button == 'Update':
                                            driver.find_element_by_xpath(Locators.update_button).click()
                                        else:
                                            assert False
                                else:
                                    assert False
                            else:
                                assert False
                        else:
                            assert False
                    else:
                        assert False
                else:
                    assert False
            else:
                assert False

        # --------------------------------------Delete Work Experience---------------------------------------------------
        def delete_experience():
            time.sleep(2)
            count_experience = len(driver.find_elements_by_xpath('(//*[@class="additional-into-item experience"])//*[@aria-label="delete"]'))
            for x in range(count_experience):
                driver.find_element_by_xpath('(//*[@class="additional-into-item experience"])[1]//*[@aria-label="delete"]').click()
                confirm_delete_modal = driver.find_element_by_id('alert-dialog-title').text
                if confirm_delete_modal == 'Confirm Delete':
                    driver.find_element_by_xpath('//*[text()="Delete"]').click()
                    time.sleep(2)
                else:
                    assert False

        delete_experience()
        #----------------------------------Add Work Experience----------------------------------------------------------
        section_title_3 = driver.find_element_by_xpath('(//*[@class="section-title"])[3]').text
        if section_title_3 == 'Work Experience':
            n = len(Locators.workExperience_additional)
            for x in range(n):
                try:
                    add_qualification_button = driver.find_element_by_xpath('//*[text()="Add experience"]')
                    if add_qualification_button == 'Add experience':
                        driver.find_element_by_xpath('//*[text()="Add experience"]').click()
                        add_work_experience(a=x)
                    else:
                        assert False
                except:
                    button_click_1 = driver.find_element_by_xpath('(//*[text()="Add more"])[3]').text
                    if button_click_1 == "Add more":
                        driver.find_element_by_xpath('(//*[text()="Add more"])[3]').click()
                        time.sleep(2)
                        add_work_experience(a=x)
                    else:
                        assert False
        else:
            assert False

        #--------------------------------------Edit Work Experience-----------------------------------------------------
        time.sleep(2)
        driver.find_element_by_xpath('(//*[@class="additional-into-item experience"]//*[@class="action-btn-container"])[1]//*[@aria-label="edit"][1]').click()
        time.sleep(2)
        experience_modal = driver.find_element_by_class_name('ant-modal-title').text
        if experience_modal == 'Edit Experience':
            add_work_experience(a=1)
            time.sleep(2)
        else:
            assert False

     #-------------------------------------------Submit button-------------------------------------------------------
    def save_button(self):
        def save_additional_information():
            driver = self.driver
            submit_additional_information = driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard).text
            print(submit_additional_information)
            if submit_additional_information == 'Save':
                driver.find_element_by_class_name(Locators.submit_save_and_goto_dashboard).click()
            else:
                assert False
            time.sleep(5)
        save_additional_information()
