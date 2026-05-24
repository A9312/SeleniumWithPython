import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.saucedemo.com/")

time.sleep(5)

driver.find_element(By.ID,"user-name").send_keys("standard_user")

time.sleep(5)

driver.find_element(By.NAME,"password").send_keys("secret_sauce")

time.sleep(5)

driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

time.sleep(5)


