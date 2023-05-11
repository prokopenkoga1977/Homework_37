# Install venv  : 
# py -m venv env
# Activate vent : 
# .\env\Scripts\activate
# Install Selenium + Drivers 

# 4) https://medium.com/

# 	- Search panel 
# 	- Click on the first element into nav-panel
# 	- Click on third article there


from Driver import Driver
from tools.Data import Data
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class App:
    def __init__(self, driver):
        self.driver = driver

def main():
    chrome_test = Driver("chrome")
    driver = App(chrome_test.__dict__["driver"])
    driver=driver.__dict__['driver']   
    # loading website Medium   
    driver.get("https://medium.com/")
    time.sleep(5)
    # search the button "Get started" and press Enter
    input = Data(driver, "single", "xpath", value='//*[@id="root"]/div/div[3]/div[1]/div/div/div/div[3]/div/span/a').get_data()
    time.sleep(5)
    input.send_keys(Keys.ENTER)
    time.sleep(5)
    # search the button "Sign up with Google" and press Enter
    input = Data(driver, "single", "xpath", value='/html/body/div[2]/div/div/div/div/div/div[2]/div[2]/button').get_data()
    time.sleep(5)
    input.send_keys(Keys.ENTER)
    time.sleep(5)
    # search the field "Your email", input email: prokopenkoga1977@gmail.com
    input = Data(driver, "single", "xpath", value= '/html/body/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/div[2]/div/p/input').get_data()
    time.sleep(5)
    input.send_keys("prokopenkoga1977@gmail.com")
    time.sleep(5)
    # search the button "Continue" and press Enter
    input = Data(driver, "single", "xpath", value= '/html/body/div[2]/div/div/div/div/div/div[2]/div/div[3]/button').get_data()
    time.sleep(5)
    input.send_keys(Keys.ENTER)
    # search the link "Following" and press Enter   
    input = Data(driver, "single", "xpath", value= '//*[@id="scroller-items"]/div[3]/a/p/span/button').get_data()
    time.sleep(5)
    input.send_keys(Keys.ENTER)
    time.sleep(5)
    # search the third article and press Enter
    input = Data(driver, "single", "xpath", value= '//*[@id="root"]/div/div[3]/div[3]/div/main/div/div[3]/div/div/div[1]/article[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2').get_data()
    time.sleep(5)
    input.send_keys(Keys.ENTER)
    time.sleep(5)
       
if __name__ == "__main__":
    main() 



    



