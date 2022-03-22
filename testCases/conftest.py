import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup():
    option = Options()
    driver = webdriver.Chrome(chrome_options=option, executable_path="/home/traninc/PycharmProjects/Case_1/drivers/chromedriver")
    return driver