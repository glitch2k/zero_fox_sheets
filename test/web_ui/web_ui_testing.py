import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# create class to find and use elements on the DOM
class FindElement():
    def byID(self, url=None, id=None, text=None):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get(url)
        driver.find_element(By.ID, id).send_keys(text)
        time.sleep(5)
# create an object from the class above
interact_with_element = FindElement()

# use the obj method to find and interact with the DOM element by Name
url = f'http://127.0.0.1:8081/'
interact_with_element.byID(url=url, id='what', text='glitch')
interact_with_element.byID(url=url, id='how', text='bitch')