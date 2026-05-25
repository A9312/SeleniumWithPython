
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# mywait = WebDriverWait(driver,10)

mywait = WebDriverWait(driver, 10,ignored_exceptions=[NoSuchElementException,Exception])

driver.get("https://www.google.com/")

driver.maximize_window()

# time.sleep(2)

search_box=driver.find_element(By.NAME,"q")

search_box.send_keys("Selenium")

search_box.submit()

search_link = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))

search_link.click()