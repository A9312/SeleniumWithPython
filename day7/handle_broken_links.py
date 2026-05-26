import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

links = driver.find_elements(By.TAG_NAME, "a")

count = 0

for link in links:

    url = link.get_attribute("href")

    if url is None or url == "":
        continue

    try:
        res = requests.head(url)

        if res.status_code >= 400:
            print(url + " invalid link")
            count += 1
        else:
            print(url + " valid link")

    except:
        print(url + " exception occurred")

print("Total invalid links:", count)

driver.quit()