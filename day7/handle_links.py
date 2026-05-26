import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.instagram.com/")

time.sleep(3)

driver.find_element(By.LINK_TEXT,"Meta").click()

time.sleep(10)

links = driver.find_elements(By.TAG_NAME,"a")

for i in links:
    print(i.text)

