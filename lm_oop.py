from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import os


class LmAutomater:
    def __init__(self, all_cars_data):
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        # self.driver.minimize_window()
        self.all_cars_data = all_cars_data

    def change_year_table_page(self):
        if self.tds[0].text > str(self.all_cars_data[8]):
            self.previous_year_button.click()
            return True
        elif self.tds[9].text < str(self.all_cars_data[8]):
            self.next_year_button.click()
            return True
        return False

    def click_year_form(self, year_form):
        self.driver.execute_script("window.scrollBy(0, -200);")
        try:
            year_form.click()
            time.sleep(1)
            self.driver.execute_script("window.scrollBy(0, -100);")
            self.driver.execute_script("arguments[0].click();", year_form)
        except:
            self.click_year_form(year_form)


    def find_and_click_option(self, ul_selector, car_name):
        try:
            ul_element = self.driver.find_element(By.XPATH, ul_selector)
            list_items = ul_element.find_elements(By.CSS_SELECTOR, "li.el-select-dropdown__item")
            for item in list_items:
                if car_name in item.text:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", item)
                    self.driver.execute_script("arguments[0].click();", item)
                    return
            self.find_and_click_option(ul_selector, car_name)
        except Exception as e:
            print(f"Błąd podczas wyszukiwania opcji: {e}")

    def go_to_next_page(self):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", self.next_page_button)
            self.next_page_button.click()
        except:
            self.go_to_next_page(self.driver, self.next_page_button)


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
        self.driver.get('https://www.lm.pl/ogloszenia/dodaj')

        wait = WebDriverWait(self.driver, 10)

        button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".fc-button.fc-cta-consent.fc-primary-button")))
        button.click()
        time.sleep(1)

        category = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'el-input__inner')))
        self.driver.execute_script("arguments[0].click();", category)
        category.send_keys("samochody")

        car_category = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[15]/div[1]/div[1]/ul/ul[2]/li[2]/ul/li[1]')))
        self.driver.execute_script("arguments[0].click();", car_category)

        title_input = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[3]/div/div/input')))
        title_input.send_keys(self.all_cars_data[1])

        description_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[4]/div/div/textarea')))
        description_input.send_keys(self.all_cars_data[4])

        type_of_ad = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="multicont_script_477"]/section[2]/form/div[2]/div/div[7]/div/div/div/input')))
        self.driver.execute_script("arguments[0].click();", type_of_ad)

        sell = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[16]/div[1]/div[1]/ul/li[1]')))
        self.driver.execute_script("arguments[0].click();", sell)

        items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "el-form-item")))

        inputs = [self.all_cars_data[5], self.all_cars_data[6], self.all_cars_data[7]]
        ul_selectors = ['/html/body/div[17]/div[1]/div[1]/ul', '/html/body/div[18]/div[1]/div[1]/ul','/html/body/div[19]/div[1]/div[1]/ul']
        for i in range(3):
            time.sleep(0.5)
            type_of_form = items[i + 5]
            self.driver.execute_script("arguments[0].click();", type_of_form.find_element(By.TAG_NAME, "input"))
            self.find_and_click_option(ul_selectors[i], inputs[i])

        year_form = items[8].find_element(By.TAG_NAME, 'input')
        self.click_year_form(year_form)

        time.sleep(0.5)
        self.previous_year_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Poprzedni rok']")
        self.next_year_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Następny rok']")

        year_table = self.driver.find_element(By.CSS_SELECTOR, "table.el-year-table")

        self.tds = year_table.find_elements(By.TAG_NAME, "td")

        time.sleep(1)
        while self.change_year_table_page():
            time.sleep(1)
            self.change_year_table_page()

        for td in self.tds:
            if td.text == str(self.all_cars_data[8]):
                td.click()
                self.driver.execute_script("arguments[0].click();", td)

        inputs = [self.all_cars_data[9], self.all_cars_data[10], self.all_cars_data[11]]
        for i in range(3):
            input_element = items[i + 10].find_element(By.TAG_NAME, "input")
            input_element.send_keys(inputs[i])

        self.next_page_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'el-button--primary')]")


        self.go_to_next_page()
        other_divs = self.driver.find_elements(By.XPATH,
                                          "//div[div[contains(@class, 'form__small_info')]]/div[position()>1]")

        inputs = [self.all_cars_data[12], self.all_cars_data[13], self.all_cars_data[14], self.all_cars_data[15], self.all_cars_data[15]]
        for i in range(5):
            input_element = other_divs[i].find_element(By.TAG_NAME, "input")
            input_element.send_keys(inputs[i])

        type_of_form = self.driver.find_element(By.XPATH,
                                           '//*[@id="multicont_script_477"]/section[2]/form/div[3]/div/div[7]/div/div/div/input')
        self.driver.execute_script("arguments[0].click();", type_of_form)
        self.find_and_click_option('/html/body/div[21]/div[1]/div[1]/ul', 'Konin')

        self.next_page_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="multicont_script_477"]/section[2]/form/div[7]/div[2]/button')

        self.go_to_next_page()


        time.sleep(100)
        self.driver.quit()




l = LmAutomater((1, 'Peugeot', 'VF111111111111111', 'C:\\Users\\rkota\\Desktop\\pythonprojekty\\auto-wystawiacz\\uploaded_images/VF111111111111111', 'Descri', 'Peugeot', 'kombi', 'diesel', 2008, 176500, 1690, 39500, 'Rss', 'admin@gmail.com', '123456789', 'Warszawa', 1))
l.post_all_cars()