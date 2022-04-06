import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
import time
from utilites.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Testaction9:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_input_invalid(self, setup):
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
        self.driver.find_element(By.XPATH, "//*[@id='rtest-to']").send_keys("automation")
        time.sleep(3)

        #get element send
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button").click()

        #get element value input email
        get_email = self.driver.find_element(By.XPATH, "//*[@id='rtest-to']")
        act = get_email.get_attribute("value")
        error = act + "is not a valid email"

        #get message error
        message = self.driver.find_element(By.CLASS_NAME, "invalid-feedback")
        act_message = message.text
        print("Error message is " + act_message)

        #check error
        assert act_message, error
        self.driver.close()