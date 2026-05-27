import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice")

time.sleep(2)

driver.switch_to.frame("courses-iframe")

time.sleep(2)

driver.find_element(By.XPATH,"//span[@class='fa fa-linkedin']").click()

time.sleep(2)

driver.switch_to.default_content()

time.sleep(2)

driver.find_element(By.XPATH,"//input[@value='radio1']").click()

time.sleep(2)
