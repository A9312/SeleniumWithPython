import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

time.sleep(2)

# window1 = driver.current_window_handle
#
# driver.switch_to.window(window1)

windowIDS = driver.window_handles

driver.switch_to.window(windowIDS[1])

print(driver.title)

time.sleep(2)

# driver.close()

driver.switch_to.window(windowIDS[0])

print(driver.title)

time.sleep(5)

