import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('auto-poster2.db')
        self.c = self.conn.cursor()
        self.c.execute("PRAGMA foreign_keys = ON")

    def create_empty_database(self):
        self.c.execute("""CREATE TABLE Users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email_address TEXT NOT NULL)
        """)


        self.c.execute("""CREATE TABLE Cars(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            VIN TEXT,
            images_directory_path TEXT,
            description TEXT,
            car_brand TEXT,
            car_body TEXT,
            fuel_type TEXT,
            year INTEGER,
            miles INTEGER,
            engine INTEGER,
            price INTEGER,
            author TEXT,
            email TEXT,
            phone_number TEXT,
            city TEXT,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES Users(ID)
        )""")

    def delete_car(self, vin):
        self.c.execute("DELETE from Cars WHERE VIN = ?", (vin,))
        self.conn.commit()

    def delete_user(self, username):
        self.c.execute("DELETE from Users WHERE username = ?", (username,))
        self.conn.commit()

    def add_new_user(self, username, password, email_address):
        data_tuple = (username, password, email_address)
        self.c.execute("INSERT INTO Users (username, password, email_address) VALUES (?,?,?)", data_tuple)
        self.conn.commit()

    def add_new_car(self, car_data, username):
        car_data["username"] = username
        self.c.execute("""
        INSERT INTO Cars (
            title, VIN, images_directory_path, description, car_brand, car_body, fuel_type,
            year, miles, engine, price, author, email, phone_number, city, user_id
        ) VALUES (
            :title, :VIN, :images_directory_path, :description, :brand, :body, :fuel,
            :year, :mileage, :engine, :price, :author, :email, :phone_number, :city, :user_id
                    )
        """, car_data)
        self.conn.commit()


    def check_if_username_taken(self, username):
        self.c.execute("SELECT username FROM Users WHERE username = ?", (username,))
        reslut = self.c.fetchone()

        if reslut:
            return True
        return False

    def check_if_user_exists(self, username, password):
        self.c.execute("SELECT password FROM Users WHERE username = ?", (username,))
        result = self.c.fetchone()

        if result:
            stored_password = result[0]
            if stored_password == password:
                return True
            return False

    def get_user_password(self, username):
        self.c.execute("SELECT password FROM Users WHERE username = ?", (username,))
        return self.c.fetchone()[0]

    def get_user_email(self, username):
        self.c.execute("SELECT email_address FROM Users WHERE username = ?", (username,))
        return self.c.fetchone()[0]

    def get_user_id(self, username):
        self.c.execute("SELECT ID FROM Users WHERE username = ?", (username,))
        return self.c.fetchone()[0]

    def get_user_cars(self, username):
        self.c.execute("""SELECT Cars.* FROM Cars
         JOIN Users ON Cars.user_id = Users.ID
         WHERE username = ?""", (username,))
        return self.c.fetchall()

    def close_connection(self):
        self.conn.close()

