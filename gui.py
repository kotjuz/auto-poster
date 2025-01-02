from tkinter import *

LABELS_FONT = ("Arial", 15)
BUTTONS_FONT = ("Arial", 10)

window = Tk()
window.title("Auto wystawiacz")
window.config(bg="white", padx=20, pady=20, width=700, height=750)
window.minsize(700, 750)
window.maxsize(700, 750)


empty_label = Frame(window, width=700, height=400, bg="white", padx=0, pady=0)
empty_label.grid(row=0, column=0, columnspan=3)

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

window.mainloop()
