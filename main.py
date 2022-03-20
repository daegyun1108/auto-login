'''
pip install selenium
pip install webdriver_manager.chrome
pip install pyperclip
'''
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10) 

driver.get("https://www.naver.com")

from selenium.webdriver.common.by import By
driver.find_element(By.CLASS_NAME,'link_login').click()

user = {'id':'id','pw':'id'} #id pw 입력

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

driver.find_element(By.ID,'id').click()
pyperclip.copy(user['id'])
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

driver.find_element(By.ID,'pw').click()
pyperclip.copy(user['pw'])
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

driver.find_element(By.ID,'log.login').click()

while True:
    time.sleep(1)
