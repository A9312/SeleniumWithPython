import time

from  selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

time.sleep(2)

search_box = driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")

search_box.send_keys("abcdefgh")

print(search_box.get_attribute('value'))
