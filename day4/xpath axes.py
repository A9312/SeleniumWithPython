import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

time.sleep(2)

# text_msg = driver.find_element(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/self::a").text

# print(text_msg)

# text_msg = driver.find_element(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/parent::td").text

# print(text_msg)


# childs = driver.find_elements(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/ancestor::tr/child::td")

# print(len(childs))

text_msg = driver.find_element(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/ancestor::tr").text

print(text_msg)


childs = driver.find_elements(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/ancestor::tr/descendant::*")

print(len(childs))


childs = driver.find_elements(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/ancestor::tr/following::*")

print(len(childs))

childs = driver.find_elements(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/ancestor::tr/following-sibling::*")

print(len(childs))

childs = driver.find_elements(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/ancestor::tr/preceding::*")

print(len(childs))

childs = driver.find_elements(By.XPATH,"//a[normalize-space()='Sterlite Technologie']/ancestor::tr/preceding-sibling::*")

print(len(childs))

