import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
import time
from utilites.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class Testunselected:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_unselected(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        time.sleep(4)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()
        #get element field input
        self.driver.find_element(By.XPATH, "//*[@id='rtest-to']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='rtest-to']").send_keys("phananhtuan792@gmail.con")
        time.sleep(3)
        # get element field subject
        self.driver.find_element(By.XPATH, "//*[@id='rtest-subject']").send_keys("automation")

        # get element field your note
        self.driver.find_element(By.XPATH, "//*[@id='rtest-note']").send_keys("automation")

        #get element field send
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button").click()

        expectedMessage = "Success! This page has been shared."

        #get text alert noti
        message_success = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#rtest-alert-notifications")))
        act_message_success = message_success.text
        # print(act_message_success)

        #check verify noti
        assert act_message_success, expectedMessage
        self.driver.close()

