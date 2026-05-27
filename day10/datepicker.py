import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://jqueryui.com/datepicker/")

time.sleep(2)

frames_date_picker = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")

driver.switch_to.frame(frames_date_picker)

date_picker = driver.find_element(By.XPATH,"//input[@id='datepicker']")

date_picker.click()

time.sleep(2)

# driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").send_keys("January")
#
# driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").send_keys("2025")
#
# driver.find_element(By.XPATH,"//span[@class='ui-datepicker-day']").send_keys("1")

year="2029"

month="July"

day="23"

time.sleep(2)

# date_picker.send_keys("01/24/2025")

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month   and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()


time.sleep(2)

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for i in dates:
    if i.text==day:
        i.click()
        break


time.sleep(4)

