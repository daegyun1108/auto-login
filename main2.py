import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10) 

driver.get("https://www.github.com/login")

from selenium.webdriver.common.by import By

user = {'id':'id','pw':'pw'}

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

driver.find_element(By.ID,'login_field').click()
pyperclip.copy(user['id'])
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

driver.find_element(By.ID,'password').click()
pyperclip.copy(user['pw'])
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

driver.find_element(By.NAME,'commit').click()

while True:
    time.sleep(1)
