from selenium.webdriver.common.by import By


class Loginpage:
    textbox_username_xpath = "//*[@id='1-email']"
    textbox_password_xpath = "//input[@name = 'password']"
    button_login_xpath = "//button[@type = 'submit']"
    click_print = "//*[@id='gfb_app']/main/div/div/div[1]/div[1]/div/span/button/i"
    # click_print_cancel = "button.cancel-button"
    click_rules_ticket = "//*[@id='gfb_app']/main/div/div/div[1]/a"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickPrint(self):
        self.driver.find_element(By.XPATH, self.click_print).click()

    def clickPrintcancel(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_print_cancel).click()

    def clickrulesticket(self):
        self.driver.find_element(By.XPATH, self.click_rules_ticket).click()
