import logging

from pageObjects.LoginPage import Loginpage
import time
from utilites.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Testaction3:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_ui(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        time.sleep(3)
        self.lp=Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()

        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/button").click()
        self.driver.find_element(By.XPATH, "//*[@id='rTest-nav-bar-settings-menu-dropdown']").click()
        self.driver.find_element(By.XPATH, "//*[@id='rTest-nav-bar-settings-user-personal-information']").click()

        #check validate user
        first_name = self.driver.find_element(By.XPATH, "//*[@id='user_first_name']").get_attribute("value")
        last_name = self.driver.find_element(By.XPATH ,"//*[@id='user_last_name']").get_attribute("value")
        email = self.driver.find_element(By.XPATH, "//*[@id='user_email']").get_attribute("value")
        from_share_link = first_name + '' + last_name + '' + email

        self.driver.find_element(By.XPATH, "//*[@id='edit_user_form']/div[2]/div/button[2]").click()

        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()
        time.sleep(3)
        check_user_from_share_link = self.driver.find_element(By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div.modal-body > form > div:nth-child(1) > p").text

        #get element text from
        get_from = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[1]/label").text
        assert check_user_from_share_link, from_share_link
        print(get_from + " " + check_user_from_share_link)

        #get text box
        to_box = self.driver.find_element(By.XPATH, "//*[@id='rtest-to']")
        testInsideTobox = to_box.get_attribute("value")
        #get text subject
        subject_box = self.driver.find_element(By.XPATH, "//*[@id='rtest-subject']")
        testInsidesubject_box = subject_box.get_attribute("value")
        #get text note
        note_box = self.driver.find_element(By.XPATH, "//*[@id='rtest-note']")
        testInsideNotebox = note_box.get_attribute("value")

        #check verify
        if testInsideNotebox == "":
            assert True
            txt_to = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[2]/label")
            txt_to_text = txt_to.text
            print(txt_to_text +
                 " "
                  +
                  "no data default")
        else:
            assert False

        if testInsideTobox == "":
            assert True
            txt_to_box = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[4]/label")
            txt_to_text_box = txt_to_box.text
            print(txt_to_text_box +
                  " "
                  +
                  "no data default")
        else:
            assert False

        if testInsidesubject_box == "":
            assert True
            txt_to_subject = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[5]/label")
            txt_to_text_subject = txt_to_subject.text
            print(txt_to_text_subject +
                  " "
                  +
                  "no data default")
        else:
            assert False

        msg = self.driver.find_element(By.XPATH, "//*[@id='gfb-cc']").is_selected()
        # copy_myself = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[3]/div/span")
        # copy_myself_text = copy_myself.text
        if msg == False :
            assert True
            print("unselect by default")
        else:
            assert False

        link = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div[6]/p/a").is_displayed()
        if link == True:
            assert True
            print("link success")
        else:
            print("not success")
            assert False

        link_priva = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/a").is_displayed()
        if link_priva == True:
            assert True
            print("privacy policy link")
        else:
            assert False

        send_submit = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/button")
        if(send_submit.is_displayed()):
            send_submit.click()
            assert True
            print("submit form pass")
        else:
            assert False
            print("submit form fail")

        x_cancal = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/button")
        if(x_cancal.is_displayed()):
            x_cancal.click()
            assert True
            print("cancel is pass")
        else:
            assert False
            print("cancel is fail")

        self.driver.close()
        self.driver.quit()