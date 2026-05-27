import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

time.sleep(5)

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

time.sleep(2)

alertwindow = driver.switch_to.alert

print(alertwindow.text)

time.sleep(2)

alertwindow.send_keys("welcome")

time.sleep(2)

# alertwindow.accept()
alertwindow.dismiss()
time.sleep(2)