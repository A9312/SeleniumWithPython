import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(3)

username_box = driver.find_element(By.XPATH,"//input[@placeholder='Username']")
#
print(username_box.is_displayed())
#
print(username_box.is_enabled())

driver.get("https://demoqa.com/radio-button")

radio1 = driver.find_element(By.XPATH,"//input[@id='yesRadio']")

print(radio1.is_selected())

time.sleep(3)

radio1.click()

time.sleep(3)

print(radio1.is_selected())



