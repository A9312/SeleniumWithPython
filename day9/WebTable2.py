
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element(By.NAME,"username").send_keys("Admin")

driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.NAME,"//button[@type='submit']").click()

driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']//span[1]").click()

driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()

driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li").click()

