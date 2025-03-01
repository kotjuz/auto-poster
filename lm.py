from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


def upload_images(driver, folder_name="images"):
    folder_path = os.path.join(os.getcwd(), folder_name)
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]

    if not image_files:
        print("Brak zdjęć w folderze.")
        return

    for image in image_files:

        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")

        image_path = os.path.join(folder_path, image)

        driver.execute_script("arguments[0].value = '';", file_input)

        file_input.send_keys(image_path)
        print(f"Przesyłanie zdjęcia: {image_path}")

        time.sleep(1)

    print("Wszystkie zdjęcia zostały przesłane.")


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
        find_and_click_option(driver, ul_selector, car_name)
    except Exception as e:
        print(f"Błąd podczas wyszukiwania opcji: {e}")


def go_to_next_page(driver, next_page_button):
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_page_button)
        next_page_button.click()
    except:
        go_to_next_page(driver, next_page_button)


def change_year_table_page(year):
    if tds[0].text > year:
        previous_year_button.click()
        return True
    elif tds[9].text < year:
        next_year_button.click()
        return True
    return False


def click_year_form(driver, year_form):
    driver.execute_script("window.scrollBy(0, -200);")
    try:
        year_form.click()
        time.sleep(1)
        # driver.execute_script("arguments[0].scrollIntoView({block: 'end'});", year_form)
        driver.execute_script("window.scrollBy(0, -100);")
        driver.execute_script("arguments[0].click();", year_form)
    except:
        click_year_form(driver, year_form)

title = "Peugeot 308"
imie = 'Mark'
email = 'test@gmail.com'
telefon = '123456789'
ulica = 'Konin'
miasto = 'Konin'
mileage = '176500'
pojemnosc = '1600'
price = '39500'
year = '2017'
descripiton = """Witam,
Mam na sprzedaż pięknego Peugeota 308 w wersji po lifcie. Samochód jest w całości w oryginalnym lakierze i prezentuje się naprawdę świetnie. Ma nowe opony letnie Michelin i ładne alufelgi, które doskonale komponują się z jego wyglądem.

Peugeot posiada bogate wyposażenie, w tym:

czujniki parkowania przód i tył,
elektryczne szyby,
półskórzane fotele,
dotykowy wyświetlacz,
system Start-Stop,
szklany dach,
składane lusterka,
CarPlay i Android Auto.
Auto posiada dynamiczny i niezawodny silnik diesla 1.6 o mocy 120 KM oraz 6-biegową skrzynie biegów.
Spalanie jest bardzo niskie – około 5 l/100 km w trasie i 6 l/100 km w mieście.

Zapraszam do kontaktu oraz na jazdę próbną. Kontakt:"""

desc = "Ladny"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.lm.pl/ogloszenia/dodaj")

time.sleep(1)


button = driver.find_element(By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")
button.click()


time.sleep(1)
category = driver.find_element(By.CLASS_NAME, 'el-input__inner')
driver.execute_script("arguments[0].click();", category)

category.send_keys("samochody")

car_category = driver.find_element(By.XPATH, '/html/body/div[15]/div[1]/div[1]/ul/ul[2]/li[2]/ul/li[1]')
driver.execute_script("arguments[0].click();", car_category)


title_input = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[3]/div/div/input')
title_input.send_keys(title)

description_input = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[4]/div/div/textarea')
description_input.send_keys(descripiton)

time.sleep(0.5)
type_of_ad = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[7]/div/div/div/input')
driver.execute_script("arguments[0].click();", type_of_ad)


sell = driver.find_element(By.XPATH, '/html/body/div[16]/div[1]/div[1]/ul/li[1]')
driver.execute_script("arguments[0].click();", sell)

time.sleep(0.5)


items = driver.find_elements(By.CLASS_NAME, "el-form-item")


inputs = ["Peugeot", "kombi", "diesel"]
ul_selectors = ['/html/body/div[17]/div[1]/div[1]/ul','/html/body/div[18]/div[1]/div[1]/ul', '/html/body/div[19]/div[1]/div[1]/ul']
for i in range(3):
    time.sleep(0.5)
    type_of_form = items[i + 5]
    driver.execute_script("arguments[0].click();", type_of_form.find_element(By.TAG_NAME, "input"))
    find_and_click_option(driver, ul_selectors[i], inputs[i])

time.sleep(0.5)

year_form = items[8].find_element(By.TAG_NAME, "input")



click_year_form(driver, year_form)
time.sleep(0.5)
previous_year_button = driver.find_element(By.XPATH, "//button[@aria-label='Poprzedni rok']")
next_year_button = driver.find_element(By.XPATH, "//button[@aria-label='Następny rok']")

year_table = driver.find_element(By.CSS_SELECTOR, "table.el-year-table")

tds = year_table.find_elements(By.TAG_NAME, "td")



time.sleep(1)
while change_year_table_page(year):
    time.sleep(1)
    change_year_table_page(year)

for td in tds:
    if td.text == year:
        td.click()
        driver.execute_script("arguments[0].click();", td)



inputs = [mileage, pojemnosc, price]
for i in range(3):
    input_element = items[i+10].find_element(By.TAG_NAME, "input")
    input_element.send_keys(inputs[i])




next_page_button = driver.find_element(By.XPATH, "//button[contains(@class, 'el-button--primary')]")
# time.sleep(2)
go_to_next_page(driver, next_page_button)
time.sleep(1)

other_divs = driver.find_elements(By.XPATH, "//div[div[contains(@class, 'form__small_info')]]/div[position()>1]")




inputs = [imie, email, telefon, ulica, miasto]
for i in range(5):
    input_element = other_divs[i].find_element(By.TAG_NAME, "input")
    input_element.send_keys(inputs[i])

time.sleep(0.5)
type_of_form = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[3]/div/div[7]/div/div/div/input')
driver.execute_script("arguments[0].click();", type_of_form)
find_and_click_option(driver, '/html/body/div[21]/div[1]/div[1]/ul', 'Konin')

next_page_button = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[7]/div[2]/button')
time.sleep(0.5)
go_to_next_page(driver, next_page_button)
time.sleep(0.5)

upload_images(driver)
time.sleep(0.5)
checkbox = driver.find_element(By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[4]/div/div[4]/label[1]/span[1]/input')

driver.execute_script("arguments[0].click();", checkbox)


time.sleep(60)
driver.quit()

