import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demo.automationtesting.in/Frames.html")

time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

frame1 = driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")

driver.switch_to.frame(frame1)

frame2 = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")

driver.switch_to.frame(frame2)

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("admin")

time.sleep(2)

driver.switch_to.parent_frame()

time.sleep(2)