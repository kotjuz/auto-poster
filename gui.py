from tkinter import *

window = Tk()
window.title("Auto wystawiacz")
window.config(bg="white", padx=20, pady=20, width=700, height=750)
window.minsize(700, 750)

shadow_label = Frame(window, width=700, height=400, bg="white", padx=0, pady=0).grid(row=0, column=0, columnspan=3)
login_label = Label(window, text="login:", bg="white", pady=5).grid(row=1, column=0, sticky="e")
login_entry = Entry(window, width=30).grid(row=1, column=1)

password_label = Label(window, text="haslo:", bg="white", pady=5).grid(row=2, column=0, sticky="e")
password_entry = Entry(window, width=30).grid(row=2, column=1)

sign_in_button = Button(window, text="Zaloguj się", width=20, height=1).grid(row=3, column=1)

sign_up_button = Button(window, text="Zarejestruj się", width=20, height=1).grid(row=4, column=1)

window.mainloop()