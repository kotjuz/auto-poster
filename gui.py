from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from validator import Validator
from database import Database
from user import User
import datetime
import os

LABELS_FONT = ("Arial", 15)
BUTTONS_FONT = ("Arial", 10)
MAIN_MENU_BUTTONS_FONT = ("Arial", 18)

validator = Validator()
db = Database()


def show_add_car_page(user):
    car_data = {}
    def show_page1():
        clear_screen()
        home_button = Button(window, width=30, height=30, bg="white",  image=home_image, command=lambda: show_main_menu_page(user))
        home_button.grid(row=0, column=0, sticky="n")

        empty_frame = Frame(window, width=590, height=100, bg="white")
        empty_frame.grid(row=0, column=1)

        title_entry = Entry(window, width=50, font=BUTTONS_FONT)
        title_entry.grid(row=1, column=1, pady=10)

        title_label = Label(window, font=LABELS_FONT, text="Tytul: ", bg="white")
        title_label.grid(row=1, column=1, sticky='w', columnspan=2)

        description_entry = Text(window, width=50, height=20, font=BUTTONS_FONT)
        description_entry.grid(row=2, column=1, pady=10)

        description_label = Label(window, font=LABELS_FONT, text="Opis: ", bg="white")
        description_label.grid(row=2, column=1, sticky='w', columnspan=2)

        brand_entry = Entry(window, width=50, font=BUTTONS_FONT)
        brand_entry.grid(row=3, column=1, pady=10)

        brand_label = Label(window, font=LABELS_FONT, text="Marka: ", bg="white")
        brand_label.grid(row=3, column=1, sticky='w', columnspan=2)

        body_entry = Entry(window, width=50, font=BUTTONS_FONT)
        body_entry.grid(row=4, column=1, pady=10)

        body_label = Label(window, font=LABELS_FONT, text="Nadwozie: ", bg="white")
        body_label.grid(row=4, column=1, sticky='w', columnspan=2)

        fuel_entry = Entry(window, width=50, font=BUTTONS_FONT)
        fuel_entry.grid(row=5, column=1, pady=10)

        fuel_label = Label(window, font=LABELS_FONT, text="Paliwo: ", bg="white")
        fuel_label.grid(row=5, column=1, sticky='w', columnspan=2)

        def validate_data():
            errors = 0

            title = title_entry.get()
            if validator.validate_title(title):
                car_data['title'] = title
            elif len(title) < 2:
                messagebox.showwarning("Bląd.", "Dodaj tytul.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.","Bląd w tytule. Tytul nie może zawierać polskich znaków oraz znaków specjalnych."
                                       " Dlugość nie może przekraczać 60 znaków.")
                errors += 1

            description = description_entry.get("1.0", "end-1c")
            if validator.validate_description(description):
                car_data['description'] = description
            elif len(description) < 10:
                messagebox.showwarning("Bląd.", "Dodaj opis.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.", "Bląd w opisie. Dlugość nie może przekraczać 2000 znaków.")
                errors += 1

            brand = brand_entry.get()
            if validator.validate_brand(brand):
                car_data['brand'] = brand
            elif len(brand) < 2:
                messagebox.showwarning("Bląd.", "Dodaj markę.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.","Bląd w marce. Dlugość nie może przekraczać 15 znaków.")
                errors += 1

            body = body_entry.get()
            if validator.validate_body(body):
                car_data['body'] = body
            elif len(body) < 3:
                messagebox.showwarning("Bląd.", "Dodaj nadwozie.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.","Bląd w nadwoziu. Dostępne opcje: \n"
                                               "kombi, sedan, hatchback, coupe, cabrio, suv, inne")
                errors += 1

            fuel = fuel_entry.get()
            if validator.validate_fuel(fuel):
                car_data['fuel'] = fuel
            elif len(fuel) < 3:
                messagebox.showwarning("Bląd.", "Dodaj paliwo.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.","Bląd w paliwie. Dostępne opcje: \n"
                                               "diesel, benzyna, hybryda, elektryczny")
                errors += 1

            if errors > 0:
                return
            else:
                print(car_data)
                show_page2()


        next_page_button = Button(window, text="Dalej", width=20, height=1, font=LABELS_FONT, command=validate_data)
        next_page_button.grid(row=6, column=1)




    def show_page2():
        clear_screen()
        home_button = Button(window, width=30, height=30, bg="white",  image=home_image, command=show_main_menu_page)
        home_button.grid(row=0, column=0, sticky="n")

        empty_frame = Frame(window, width=590, height=100, bg="white")
        empty_frame.grid(row=0, column=1)

        year_entry = Entry(window, width=50, font=BUTTONS_FONT)
        year_entry.grid(row=1, column=1, pady=10)

        year_label = Label(window, font=LABELS_FONT, text="Rok prod.: ", bg="white")
        year_label.grid(row=1, column=1, sticky='w', columnspan=2)

        mileage_entry = Entry(window, width=50, font=BUTTONS_FONT)
        mileage_entry.grid(row=2, column=1, pady=10)

        mileage_label = Label(window, font=LABELS_FONT, text="Przebieg: ", bg="white")
        mileage_label.grid(row=2, column=1, sticky='w', columnspan=2)

        km_label = Label(window, font=BUTTONS_FONT, text="km", bg="white")
        km_label.place(x=510, y=150)

        engine_entry = Entry(window, width=50, font=BUTTONS_FONT)
        engine_entry.grid(row=3, column=1, pady=10)

        engine_label = Label(window, font=LABELS_FONT, text="Pojemnosc: ", bg="white")
        engine_label.grid(row=3, column=1, sticky='w', columnspan=2)

        cm_label = Label(window, font=BUTTONS_FONT, text="cm", bg="white")
        cm_label.place(x=510, y=190)

        price_entry = Entry(window, width=50, font=BUTTONS_FONT)
        price_entry.grid(row=4, column=1, pady=10)

        price_label = Label(window, font=LABELS_FONT, text="Cena: ", bg="white")
        price_label.grid(row=4, column=1, sticky='w', columnspan=2)

        pln_label = Label(window, font=BUTTONS_FONT, text="zl", bg="white")
        pln_label.place(x=510, y=230)

        author_entry = Entry(window, width=50, font=BUTTONS_FONT)
        author_entry.grid(row=5, column=1, pady=10)

        author_label = Label(window, font=LABELS_FONT, text="Autor: ", bg="white")
        author_label.grid(row=5, column=1, sticky='w', columnspan=2)

        email_entry = Entry(window, width=50, font=BUTTONS_FONT)
        email_entry.grid(row=6, column=1, pady=10)

        email_label = Label(window, font=LABELS_FONT, text="Email: ", bg="white")
        email_label.grid(row=6, column=1, sticky='w', columnspan=2)

        phone_entry = Entry(window, width=50, font=BUTTONS_FONT)
        phone_entry.grid(row=7, column=1, pady=10)

        phone_label = Label(window, font=LABELS_FONT, text="Nr telefonu: ", bg="white")
        phone_label.grid(row=7, column=1, sticky='w', columnspan=2)

        city_entry = Entry(window, width=50, font=BUTTONS_FONT)
        city_entry.grid(row=8, column=1, pady=10)

        city_label = Label(window, font=LABELS_FONT, text="Miasto: ", bg="white")
        city_label.grid(row=8, column=1, sticky='w', columnspan=2)

        vin_entry = Entry(window, width=50, font=BUTTONS_FONT)
        vin_entry.grid(row=9, column=1, pady=10)

        vin_label = Label(window, font=LABELS_FONT, text="VIN: ", bg="white")
        vin_label.grid(row=9, column=1, sticky='w', columnspan=2)

        def validate_data():
            errors = 0

            year = year_entry.get()
            if validator.validate_year(year):
                car_data['year'] = year
            elif len(year) < 2:
                messagebox.showwarning("Bląd.", "Dodaj rok produkcji.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w roku produkcji. Rok musi być z przedzialu 1900 - {datetime.datetime.now().year}")
                errors += 1

            mileage = mileage_entry.get()
            if validator.validate_mileage(year):
                car_data['mileage'] = mileage
            elif len(mileage) == 0:
                messagebox.showwarning("Bląd.", "Dodaj przebieg.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w przebiegu. Ma być to liczba, bez np. 'km' oraz bez spacji.")
                errors += 1

            engine = engine_entry.get()
            if validator.validate_engine(engine):
                car_data['engine'] = engine
            elif len(engine) == 0:
                messagebox.showwarning("Bląd.", "Dodaj pojemność silnika.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w pojemności silnika. Ma to być w formacie np '1600' zamiast '1.6'.")
                errors += 1

            price = price_entry.get()
            if validator.validate_price(price):
                car_data['price'] = price
            elif len(price) == 0:
                messagebox.showwarning("Bląd.", "Dodaj cenę.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w cenie. Ma to być liczba, bez np. waluty")
                errors += 1

            author = author_entry.get()
            if validator.validate_author(author):
                car_data['author'] = author
            elif len(author) < 2:
                messagebox.showwarning("Bląd.", "Dodaj autora.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w polu 'Autor'. Ma to być tekst o  maksymalnej dlugości 25 znaków.")
                errors += 1

            email = email_entry.get()
            if validator.validate_email(email):
                car_data['email'] = email
            elif len(email) < 2:
                messagebox.showwarning("Bląd.", "Dodaj email.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w polu 'Email'.")
                errors += 1

            phone = phone_entry.get()
            if validator.validate_phone_number(phone):
                car_data['phone_number'] = phone
            elif len(phone) < 9:
                messagebox.showwarning("Bląd.", "Dodaj numer telefonu.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w polu 'Nr telefonu'. \n"
                                               f" Ma być w postaci np. '532543872', oraz bez numeru kierunkowego.")
                errors += 1

            city = city_entry.get()
            if validator.validate_city(city):
                car_data['city'] = city
            elif len(city) < 2:
                messagebox.showwarning("Bląd.", "Dodaj miasto.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w polu 'Miasto'. Nazwa miasta może mieć maksymalnei 25 znaków.")
                errors += 1

            vin = vin_entry.get()
            if validator.validate_vin(vin):
                car_data['VIN'] = vin
            elif len(vin) == 0:
                messagebox.showwarning("Bląd.", "Dodaj numer VIN.")
                errors += 1
            else:
                messagebox.showwarning("Bląd.",f"Bląd w polu 'VIN'. Nieprawidlowy VIN.")
                errors += 1

            if errors > 0:
                return
            else:
                print(car_data)
                show_page3()

        next_page_button = Button(window, text="Dalej", width=20, height=1, font=LABELS_FONT, command=validate_data)
        next_page_button.grid(row=10, column=1)

    def show_page3():
        clear_screen()
        home_button = Button(window, width=30, height=30, bg="white",  image=home_image, command=show_main_menu_page)
        home_button.place(x=0, y=0)
        def upload_images():
            file_paths = filedialog.askopenfilenames(
                title="Select Images",
                filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")]
            )

            if not file_paths:
                messagebox.showinfo("Brak wyboru", "Nie wybrano żadnych zdjęć.")
                return

            for file_path in file_paths:
                try:
                    if len(images) >= 12:
                        messagebox.showwarning("Limit zdjęć", "Możesz dodać maksymalnie 12 zdjęć.")
                        break

                    img = Image.open(file_path)
                    img.thumbnail((150, 150))
                    photo = ImageTk.PhotoImage(img)

                    img_label = Label(image_frame, image=photo)
                    img_label.image = photo
                    img_label.grid(row=len(images) // 4, column=len(images) % 4, padx=5, pady=5)

                    images.append(file_path)
                except Exception as e:
                    print(f"Error loading image {file_path}: {e}")

        def confirm_images():
            if not images:
                messagebox.showwarning("Brak zdjęć", "Dodaj zdjęcia.")
            else:
                # target_folder = os.path.join(os.getcwd(), "uploaded_images")
                target_folder = os.path.join(os.getcwd(), f"uploaded_images/{car_data['VIN']}")
                os.makedirs(target_folder, exist_ok=True)

                for image_path in images:
                    try:
                        file_name = os.path.basename(image_path)
                        target_path = os.path.join(target_folder, file_name)
                        with open(image_path, "rb") as src_file:
                            with open(target_path, "wb") as dest_file:
                                dest_file.write(src_file.read())
                    except Exception as e:
                        print(f"Error saving image {image_path}: {e}")

                messagebox.showinfo("Zdjęcia zatwierdzone", f"Zapisano zdjęcia")
                #TYMCZASOWO
                car_data['user_id'] = user.ID
                car_data['images_directory_path'] = target_folder
                db.add_new_car(car_data, user.login)
                #TYMCZASOWO
                show_main_menu_page(user)


        upload_button = Button(window, text="Załącz zdjęcia", command=upload_images, font=("Arial", 12))
        upload_button.pack(pady=10)

        image_frame = Frame(window)
        image_frame.pack(pady=10)

        confirm_button = Button(window, text="Zatwierdź zdjęcia", command=confirm_images, font=("Arial", 12))
        confirm_button.pack(pady=10)

        images = []

    show_page1()


def show_main_menu_page(user):
    def toggle_menu():
        if menu_frame.winfo_ismapped():
            menu_frame.place_forget()
        else:
            menu_frame.place(x=530, y=0)
            menu_frame.lift()


    clear_screen()

    # Przycisk powrotu do main menu
    home_button = Button(window, width=30, height=30, bg="white",  image=home_image)
    home_button.place(x=0, y=0)


    # Rozwijane menu
    hamburger_button = Button(window, width=30, height=30,bg="white" ,image=hamburger_menu_image ,command=toggle_menu)
    hamburger_button.place(x=625, y=0)


    # Ramka dla rozwiniętego menu
    menu_frame = Frame(window, bg="lightgray", width=50, height=100)

    # Elementy rozwijanego menu
    menu_label = Label(menu_frame, text=user.login, font=BUTTONS_FONT, bg="lightgray")
    menu_label.grid(row=0, column=0, padx=10, pady=10)

    menu_button1 = Button(menu_frame, text="Wyloguj", font=BUTTONS_FONT)
    menu_button1.grid(row=1, column=0, pady=10, padx=10)

    # Logo aplikacji
    empty_label = Frame(window, width=700, height=320, bg="white", padx=0, pady=0)
    empty_label.place(x=0, y=40)

    logo_label_label = Label(empty_label, image=logo_image)
    logo_label_label.place(relx=0.5, rely=0.5, anchor="center")


    # Ramka dla glownego menu
    main_menu_frame = Frame(window, bg="white", width=350, height=450, bd=1, relief="solid")
    main_menu_frame.place(x=120, y=450)

    # Elementy menu glownego
    add_car_button = Button(main_menu_frame, text="Dodaj auto", font=MAIN_MENU_BUTTONS_FONT, width=30, command=lambda: show_add_car_page(user))
    add_car_button.grid(row=0, column=0, padx=10, pady=4)

    post_car_button = Button(main_menu_frame, text="Ogloś auto", font=MAIN_MENU_BUTTONS_FONT, width=30)
    post_car_button.grid(row=1, column=0, padx=10, pady=4)

    my_cars_button = Button(main_menu_frame, text="Moje auta", font=MAIN_MENU_BUTTONS_FONT, width=30)
    my_cars_button.grid(row=2, column=0, padx=10, pady=4)



def show_login_page():
    clear_screen()
    empty_label = Frame(window, width=700, height=400, bg="white", padx=0, pady=0)
    empty_label.grid(row=0, column=0, columnspan=3)


    logo_label_label = Label(empty_label, image=logo_image)
    logo_label_label.place(relx=0.5, rely=0.5, anchor="center")

    login_label = Label(window, text="login:", bg="white", pady=5, font=LABELS_FONT)
    login_label.grid(row=1, column=0, sticky="e")

    login_entry = Entry(window, width=30, font=LABELS_FONT)
    login_entry.grid(row=1, column=1, ipady=3)
    login_entry.focus_set()

    password_label = Label(window, text="hasło:", bg="white", pady=5, font=LABELS_FONT)
    password_label.grid(row=2, column=0, sticky="e")

    password_entry = Entry(window, width=30, font=LABELS_FONT, show="*")
    password_entry.grid(row=2, column=1, ipady=3)

    def log_in():
        login = login_entry.get()
        password = password_entry.get()
        if db.check_if_user_exists(login, password):
            messagebox.showinfo("Sukces", "Pomyślnie zalogowano.")
            user = User(login, db)
            show_main_menu_page(user)
        else:
            messagebox.showwarning("Bląd.", "Nieprawidlowy login lub haslo.")
            return

    sign_in_button = Button(window, text="Zaloguj się", width=30, height=1, font=BUTTONS_FONT, command=log_in)
    sign_in_button.grid(row=3, column=1)

    sign_up_button = Button(window, text="Zarejestruj się", width=30, height=1, font=BUTTONS_FONT, command=show_sign_up_page)
    sign_up_button.grid(row=4, column=1)

def show_sign_up_page():
    clear_screen()

    empty_label = Frame(window, width=700, height=400, bg="white", padx=0, pady=0)
    empty_label.grid(row=0, column=0, columnspan=3)

    logo_label_label = Label(empty_label, image=logo_image)
    logo_label_label.place(relx=0.5, rely=0.5, anchor="center")

    login_label = Label(window, text="login:", bg="white", pady=5, font=LABELS_FONT)
    login_label.grid(row=1, column=0, sticky="e")

    login_entry = Entry(window, width=30, font=LABELS_FONT)
    login_entry.grid(row=1, column=1, ipady=3)
    login_entry.focus_set()

    password_label = Label(window, text="hasło:", bg="white", pady=5, font=LABELS_FONT)
    password_label.grid(row=2, column=0, sticky="e")

    password_entry = Entry(window, width=30, font=LABELS_FONT, show="*")
    password_entry.grid(row=2, column=1, ipady=3)

    email_label = Label(window, text="email:", bg="white", pady=5, font=LABELS_FONT)
    email_label.grid(row=3, column=0, sticky="e")

    email_entry = Entry(window, width=30, font=LABELS_FONT)
    email_entry.grid(row=3, column=1, ipady=3)

    def validate_data():
        login = login_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        errors = 0

        if len(login) == 0:
            messagebox.showwarning("Bląd.", "Podaj login.")
            errors += 1
        elif not validator.validate_login(login):
            messagebox.showwarning("Bląd.", "Bląd w polu 'login'. Login może zawierać tylko male, duże litery (bez polskich znaków) \n "
                                            "oraz cyfry. Dlugość musi mieścić się w przedziale 4-20 znaków.")
            errors += 1
        elif db.check_if_username_taken(login):
            messagebox.showwarning("Bląd.", "Użytkownik z takim loginem już istnieje. Wybierz innny.")
            errors += 1


        if len(password) == 0:
            messagebox.showwarning("Bląd.", "Podaj haslo.")
            errors += 1
        elif not validator.validate_password(password):
            messagebox.showwarning("Bląd.",
                                   "Bląd w polu 'haslo'. Haslo musi zawierać min. 1 malą, 1 dużą literę oraz 1 cyrę. \n "
                                   "Dlugość musi mieścić się w przedziale 6-20 znaków.")
            errors += 1

        if len(email) == 0:
            messagebox.showwarning("Bląd.", "Podaj email.")
            errors += 1
        elif not validator.validate_password(password):
            messagebox.showwarning("Bląd.",
                                   "Bląd w polu 'email'. Niepoprawny adres email.")
            errors += 1

        if errors == 0:
            db.add_new_user(login, password, email)
            messagebox.showinfo("Sukces", "Pomyślnie utworzono konto. Teraz możesz się zalogować.")
            show_login_page()
        else:
            return


    sign_up_button = Button(window, text="Utwórz konto", width=30, height=1, font=BUTTONS_FONT, command=validate_data)
    sign_up_button.grid(row=4, column=1)

    go_back_button = Button(window, width=30, height=30, bg="white",  image=back_arrow_image, command=show_login_page)
    go_back_button.place(x=0, y=0)


def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()


window = Tk()
window.title("Auto wystawiacz")
window.config(bg="white", padx=20, pady=20, width=700, height=750)
window.minsize(700, 750)
window.maxsize(700, 750)

logo_image = PhotoImage(file="icons/login_img.png")
logo_image = logo_image.subsample(3, 3)

home_image = PhotoImage(file="icons/home_img.png")
home_image = home_image.subsample(20, 20)

hamburger_menu_image = PhotoImage(file="icons/hamburger_menu_img.png")
hamburger_menu_image = hamburger_menu_image.subsample(35, 35)

back_arrow_image = PhotoImage(file="icons/back_arrow.png")
back_arrow_image = back_arrow_image.subsample(25, 25)

# show_login_page()
# window.after(5000, show_main_menu_page)

show_login_page()


window.mainloop()