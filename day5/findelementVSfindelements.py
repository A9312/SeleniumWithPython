import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(3)

username=driver.find_element(By.XPATH,"//input[@placeholder='Username']")

username.send_keys("Admin")

time.sleep(2)

driver.get("https://www.amazon.in/")

time.sleep(3)

elements = driver.find_elements(By.XPATH,"//div[@id='navFooter']//a")

print(len(elements))

print(elements[0].text)

for i in elements:
    print(i.text)