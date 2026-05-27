import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='dob']").click()

year = "2025"
month = "Jan"
day = "1"

# Select month
months = driver.find_element(By.XPATH, "//select[@aria-label='Select month']")
drp_month = Select(months)
drp_month.select_by_visible_text(month)

# Re-locate year dropdown again
years = driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
drp_year = Select(years)
drp_year.select_by_visible_text(year)

# Select day
days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for i in days:
    if i.text == day:
        i.click()
        break

time.sleep(5)