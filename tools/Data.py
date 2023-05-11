from selenium.webdriver.common.by import By
import time

class Data:
    def __init__(self, driver, is_single, identifier, value):
        self.driver = driver
        self.is_single = is_single
        self.identifier = identifier
        self.value = value
    
    def find_element_ (self):
        match (self.identifier):
            case "id":
              return self.driver.find_element(By.ID, self.value) 
            case "class_name":
              return self.driver.find_element(By.CLASS_NAME, self.value) 
            case "xpath":
              return self.driver.find_element(By.XPATH, self.value)
            case "css_selector":
              return self.driver.find_element(By.CSS_SELECTOR, self.value)
    
    def find_elements_ (self):
        match (self.identifier):
            case "id":
              return self.driver.find_elements(By.ID, self.value) 
            case "class_name":
              return self.driver.find_elements(By.CLASS_NAME, self.value) 
            case "xpath":
              return self.driver.find_elements(By.XPATH, self.value)  
            case "css_selector":
              return self.driver.find_elements(By.CSS_SELECTOR, self.value)   
        
    def get_data(self):
        match(self.is_single):
            case "single":
                return self.find_element_()
            case "some":
                return self.find_elements_()