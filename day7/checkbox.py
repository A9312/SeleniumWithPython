import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

driver.find_element(By.XPATH,"//input[@id='sunday']").click()

weekdays = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains (@id,'day')]")

print(len(weekdays))

for i in weekdays:
    print(i.get_attribute("id"))

for i in weekdays:
    i.click()

time.sleep(3)

for i in weekdays:
    if i.is_selected():
        i.click()


# for i in range(len(weekdays)-2,len(weekdays)):
#     print(weekdays[i].get_attribute("id"))


time.sleep(3)


