from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def find_and_click_option(driver, ul_selector, car_name):
    try:
        ul_element = driver.find_element(By.XPATH, ul_selector)
        list_items = ul_element.find_elements(By.CSS_SELECTOR, "li.el-select-dropdown__item")
        for item in list_items:
            if car_name in item.text:
                driver.execute_script("arguments[0].scrollIntoView(true);", item)
                driver.execute_script("arguments[0].click();", item)
                return
        print(f"Opcja {car_name} nie została znaleziona w liście.")
    except Exception as e:
        print(f"Błąd podczas wyszukiwania opcji: {e}")


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

# '/html/body/div[15]/div[1]/div[1]/ul/ul[2]/li[2]/ul/li[1]'
# '/html/body/div[15]/div[1]/div[1]/ul/ul[2]/li[2]/ul/li[1]'
car_category = driver.find_element(By.XPATH, '/html/body/div[15]/div[1]/div[1]/ul/ul[2]/li[2]/ul/li[1]')
driver.execute_script("arguments[0].click();", car_category)


title_input = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[3]/div/div/input')
title_input.send_keys("Peugeot 308")

description_input = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[4]/div/div/textarea')
description_input.send_keys("Ladny itd")

time.sleep(1)
type_of_ad = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[7]/div/div/div/input')
driver.execute_script("arguments[0].click();", type_of_ad)


sell = driver.find_element(By.XPATH, '/html/body/div[16]/div[1]/div[1]/ul/li[1]')
driver.execute_script("arguments[0].click();", sell)

time.sleep(1)
# car_model = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[8]/div/div/div[1]/input')
# driver.execute_script("arguments[0].click();", type_of_ad)
#
# find_and_click_option(driver, "/html/body/div[15]/div[1]/div[1]/ul", "Peugeot")

items = driver.find_elements(By.CLASS_NAME, "el-form-item")
# marka = items[5]
# driver.execute_script("arguments[0].click();", marka.find_element(By.TAG_NAME, "input"))
# find_and_click_option(driver, '/html/body/div[17]/div[1]/div[1]/ul', "Peugeot")

inputs = ["Peugeot", "kombi", "diesel"]
ul_selectors = ['/html/body/div[17]/div[1]/div[1]/ul','/html/body/div[18]/div[1]/div[1]/ul', '/html/body/div[19]/div[1]/div[1]/ul']
for i in range(3):
    time.sleep(3)
    type_of_form = items[i + 5]
    driver.execute_script("arguments[0].click();", type_of_form.find_element(By.TAG_NAME, "input"))
    find_and_click_option(driver, ul_selectors[i], inputs[i])

time.sleep(20)


time.sleep(60)
driver.quit()

