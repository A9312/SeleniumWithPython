import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.maximize_window()

time.sleep(3)

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

time.sleep(3)

driver.close()

time.sleep(3)

# driver.quit()