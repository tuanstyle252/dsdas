import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
import time
from utilites.readProperties import ReadConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Testprivacy:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_privacy(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        time.sleep(4)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        share = self.driver.find_element(By.XPATH, "//*[@id='gfb_app']/main/div/div/div[1]/div[2]/button/i")
        share.click()
        time.sleep(2)
        privacy = self.driver.find_element(By.LINK_TEXT, "Privacy Policy")
        privacy.click()
        p = self.driver.current_window_handle
        table0 = self.driver.window_handles[0]
        table1 = self.driver.window_handles[1]
        self.driver.switch_to_window(table0)
        time.sleep(3)
        self.driver.close()
        # switch to parent window
        self.driver.switch_to.window(table1)
        # print("Page title for table 2 window:")
        # print(self.driver.title)
        act_title = self.driver.title
        if act_title == "Privacy Policy - Revinate":
            assert True
        else:
            assert False

        # close browser parent window
        time.sleep(3)
        self.driver.close()
        self.driver.quit()