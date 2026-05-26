import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

country = driver.find_element(By.ID, "country")

dropdown = Select(country)

# dropdown.select_by_visible_text("India")

time.sleep(2)

# dropdown.select_by_value("australia")

# time.sleep(2)

# dropdown.select_by_index(5)

# time.sleep(2)

dropdown_options = dropdown.options

for option in dropdown_options:
    print(option.text)

for option in dropdown_options:
    if option.text == "India":
        option.click()

time.sleep(2)

