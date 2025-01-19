from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

LABELS_FONT = ("Arial", 15)
BUTTONS_FONT = ("Arial", 10)
MAIN_MENU_BUTTONS_FONT = ("Arial", 18)

def show_add_car_page():
    def show_page1():
        clear_screen()
        home_button = Button(window, width=30, height=30, bg="white",  image=home_image, command=show_main_menu_page)
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

        next_page_button = Button(window, text="Dalej", width=20, height=1, font=LABELS_FONT, command=show_page2)
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

        engine_entry = Entry(window, width=50, font=BUTTONS_FONT)
        engine_entry.grid(row=3, column=1, pady=10)

        engine_label = Label(window, font=LABELS_FONT, text="Pojemnosc: ", bg="white")
        engine_label.grid(row=3, column=1, sticky='w', columnspan=2)

        price_entry = Entry(window, width=50, font=BUTTONS_FONT)
        price_entry.grid(row=4, column=1, pady=10)

        price_label = Label(window, font=LABELS_FONT, text="Cena: ", bg="white")
        price_label.grid(row=4, column=1, sticky='w', columnspan=2)

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

        next_page_button = Button(window, text="Dalej", width=20, height=1, font=LABELS_FONT, command=show_page3)
        next_page_button.grid(row=9, column=1)

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
                target_folder = os.path.join(os.getcwd(), "uploaded_images")
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
                show_main_menu_page()


        upload_button = Button(window, text="Załącz zdjęcia", command=upload_images, font=("Arial", 12))
        upload_button.pack(pady=10)

        image_frame = Frame(window)
        image_frame.pack(pady=10)

        confirm_button = Button(window, text="Zatwierdź zdjęcia", command=confirm_images, font=("Arial", 12))
        confirm_button.pack(pady=10)

        images = []

    show_page1()


def show_main_menu_page():
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
    menu_label = Label(menu_frame, text="Uzytkownik", font=BUTTONS_FONT, bg="lightgray")
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
    add_car_button = Button(main_menu_frame, text="Dodaj auto", font=MAIN_MENU_BUTTONS_FONT, width=30, command=show_add_car_page)
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

    # Etykieta loginu
    login_label = Label(window, text="login:", bg="white", pady=5, font=LABELS_FONT)
    login_label.grid(row=1, column=0, sticky="e")

    # Pole tekstowe dla loginu
    login_entry = Entry(window, width=30, font=LABELS_FONT)
    login_entry.grid(row=1, column=1, ipady=3)
    login_entry.focus_set()  # Ustawienie fokusu na pole loginu

    # Etykieta hasła
    password_label = Label(window, text="hasło:", bg="white", pady=5, font=LABELS_FONT)
    password_label.grid(row=2, column=0, sticky="e")

    # Pole tekstowe dla hasła
    password_entry = Entry(window, width=30, font=LABELS_FONT)
    password_entry.grid(row=2, column=1, ipady=3)

    # Przycisk logowania
    sign_in_button = Button(window, text="Zaloguj się", width=30, height=1, font=BUTTONS_FONT)
    sign_in_button.grid(row=3, column=1)

    # Przycisk rejestracji
    sign_up_button = Button(window, text="Zarejestruj się", width=30, height=1, font=BUTTONS_FONT)
    sign_up_button.grid(row=4, column=1)

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

# show_login_page()
# window.after(5000, show_main_menu_page)

show_main_menu_page()

window.mainloop()