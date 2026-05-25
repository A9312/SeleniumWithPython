import time

from  selenium import  webdriver

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

time.sleep(3)

driver.get("https://www.snapdeal.com/")

time.sleep(3)

driver.back()

time.sleep(3)

driver.forward()

time.sleep(3)

driver.refresh()

time.sleep(3)


