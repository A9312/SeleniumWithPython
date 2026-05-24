import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(5)

driver.find_element(By.XPATH,"/html[1]/body[1]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("abcd")

time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc@gmail.com")

time.sleep(5)

