from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


CHROME_DRIVER_PATH = "chromedriver.exe"
TITLE = "Peugeot 308"
USER_DATA = {
    "name": "Name",
    "email": "email",
    "phone": "phone_nr",
    "street": "Street",
    "city": "City"
}
CAR_DETAILS = {
    "mileage": "176500",
    "engine": "1600",
    "price": "40000",
    "year": "2017",
    "description": "Nice"
}




def setup_driver():

    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    return driver


def wait_and_click(driver, by, value, timeout=10):

    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()
    return element


def fill_input_field(driver, by, value, text, timeout=10):

    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    element.clear()
    element.send_keys(text)


def select_category(driver, category_input_selector, category_name, category_option_xpath):

    wait_and_click(driver, By.CSS_SELECTOR, category_input_selector)
    fill_input_field(driver, By.CSS_SELECTOR, category_input_selector, category_name)
    wait_and_click(driver, By.XPATH, category_option_xpath)


def select_option_from_dropdown(driver, ul_xpath, option_text):

    ul_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ul_xpath)))
    options = ul_element.find_elements(By.CSS_SELECTOR, "li.el-select-dropdown__item")
    for option in options:
        if option_text in option.text:
            driver.execute_script("arguments[0].scrollIntoView(true);", option)
            driver.execute_script("arguments[0].click();", option)
            return
    raise ValueError(f"Opcja '{option_text}' nie została znaleziona.")


def upload_images(driver, folder_name="images"):

    folder_path = os.path.join(os.getcwd(), folder_name)
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]

    if not image_files:
        print("Brak zdjęć w folderze.")
        return

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    for image in image_files:
        file_path = os.path.join(folder_path, image)
        file_input.send_keys(file_path)
        time.sleep(1)
        print(f"Przesłano zdjęcie: {file_path}")


def fill_form(driver):

    select_category(
        driver,
        category_input_selector=".el-input__inner",
        category_name="samochody",
        category_option_xpath='/html/body/div[15]/div[1]/div[1]/ul/ul[2]/li[2]/ul/li[1]'
    )


    fill_input_field(driver, By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[3]/div/div/input', TITLE)
    fill_input_field(driver, By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[4]/div/div/textarea', CAR_DETAILS["description"])

    wait_and_click(driver, By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[7]/div/div/div/input')
    wait_and_click(driver, By.XPATH, '/html/body/div[16]/div[1]/div[1]/ul/li[1]')


    details = ["Peugeot", "kombi", "diesel"]
    dropdowns = ['/html/body/div[17]/div[1]/div[1]/ul', '/html/body/div[18]/div[1]/div[1]/ul', '/html/body/div[19]/div[1]/div[1]/ul']
    for i, detail in enumerate(details):
        form_item = driver.find_elements(By.CLASS_NAME, "el-form-item")[i + 5]
        form_item.find_element(By.TAG_NAME, "input").click()
        select_option_from_dropdown(driver, dropdowns[i], detail)


    fill_input_field(driver, By.CLASS_NAME, "el-input__inner", CAR_DETAILS["year"])


    details_input = [CAR_DETAILS["mileage"], CAR_DETAILS["engine"], CAR_DETAILS["price"]]
    for i, detail in enumerate(details_input):
        input_element = driver.find_elements(By.CLASS_NAME, "el-form-item")[i + 10].find_element(By.TAG_NAME, "input")
        input_element.send_keys(detail)




driver = setup_driver()
driver.get("https://www.lm.pl/ogloszenia/dodaj")
time.sleep(1)


wait_and_click(driver, By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")

try:

    fill_form(driver)


    upload_images(driver)


    time.sleep(5)
    print("Ogłoszenie zostało opublikowane.")
finally:
    driver.quit()



