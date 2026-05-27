import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2)

items = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")

print(len(items))

for i in range(1,len(items)):
    print(items[i].text)