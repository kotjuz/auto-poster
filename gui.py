import time
from tkinter import *

LABELS_FONT = ("Arial", 15)
BUTTONS_FONT = ("Arial", 10)
MAIN_MENU_BUTTONS_FONT = ("Arial", 18)

def show_main_menu_screen():
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
    add_car_button = Button(main_menu_frame, text="Dodaj auto", font=MAIN_MENU_BUTTONS_FONT, width=30)
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

logo_image = PhotoImage(file="login_img.png")
logo_image = logo_image.subsample(3, 3)

home_image = PhotoImage(file="home_img.png")
home_image = home_image.subsample(20, 20)

hamburger_menu_image = PhotoImage(file="hamburger_menu_img.png")
hamburger_menu_image = hamburger_menu_image.subsample(35, 35)

show_login_page()
window.after(5000, show_main_menu_screen)


window.mainloop()