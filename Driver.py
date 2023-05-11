from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

class Driver:
    driver = None
    def __init__(self, webdriver_type):
        match (webdriver_type):
            case "chrome":
                time.sleep(5)
                self.driver = webdriver.Chrome('C:\\Program Files\\chromedriver.exe')
            case "firefox":
                time.sleep(5)
                self.driver = webdriver.Firefox()