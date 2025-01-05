from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.lm.pl/ogloszenia/dodaj")

time.sleep(2)


button = driver.find_element(By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")
button.click()



time.sleep(1)
category = driver.find_element(By.CLASS_NAME, 'el-input__inner')
driver.execute_script("arguments[0].click();", category)

category.send_keys("samochody")


car_category = driver.find_element(By.XPATH, '/html/body/div[15]/div[1]/div[1]/ul/ul[2]/li[2]/ul/li[1]')
driver.execute_script("arguments[0].click();", car_category)




time.sleep(60)
driver.quit()

