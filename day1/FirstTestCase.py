from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# service = Service("/Users/shreygupta/Downloads/Self/Akshit/drivers/chromedriver-mac-arm64/chromedriver")
#
# driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome()

driver.maximize_window()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)

driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(3)

act_title = driver.title
exp_title = "OrangeHRM"

if exp_title == act_title:
    print("login test passed")
else:
    print("login test failed")