from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


class TurekAutomater:
    def __init__(self, all_cars_data):
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.minimize_window()
        self.all_cars_data = all_cars_data

    def upload_images(self):
        folder_path = os.path.join(self.all_cars_data[3])
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]

        if not image_files:
            return

        for image in image_files:
            file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")

            image_path = os.path.join(folder_path, image)

            self.driver.execute_script("arguments[0].value = '';", file_input)
            file_input.send_keys(image_path)

            time.sleep(1)


    def post_all_cars(self):
        self.driver.get('https://www.turek.net.pl/ogloszenia#form_ogloszenia')

        wait = WebDriverWait(self.driver, 10)

        close_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.fc-close')))
        close_button.click()

        title = wait.until(EC.visibility_of_element_located((By.ID, 'ogtytul')))
        title.send_keys(self.all_cars_data[1])

        category = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.selectogloszenia')))
        category.send_keys('motoryzacja')

        phone_number = wait.until(EC.presence_of_element_located((By.ID, 'ogkontakt')))
        phone_number.send_keys(self.all_cars_data[14])

        author = wait.until(EC.presence_of_element_located((By.ID, 'oguser')))
        author.send_keys(self.all_cars_data[12])

        email = wait.until(EC.presence_of_element_located((By.ID, 'ogemail')))
        email.send_keys(self.all_cars_data[13])

        price = wait.until(EC.presence_of_element_located((By.ID, 'ogcena')))
        price.send_keys(self.all_cars_data[11])

        descripiton = wait.until(EC.presence_of_element_located((By.ID, 'cke_ogtext')))
        actions = ActionChains(self.driver)
        actions.move_to_element(descripiton).click().send_keys(self.all_cars_data[4]).perform()

        self.upload_images()

        post_button = wait.until(EC.presence_of_element_located((By.NAME, 'dodaj')))
        post_button.send_keys(Keys.ENTER)

        self.driver.quit()




t = TurekAutomater((1, 'Peugeot', 'VF111111111111111', 'C:\\Users\\rkota\\Desktop\\pythonprojekty\\auto-wystawiacz\\uploaded_images/VF111111111111111', 'Descri', 'Peugeot', 'kombi', 'diesel', 2017, 176500, 1690, 39500, 'Rss', 'admin@gmail.com', '123456789', 'Warszawa', 1))
t.post_all_cars()
