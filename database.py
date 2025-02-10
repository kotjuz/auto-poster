import sqlite3


class Database():
    def __init__(self):
        self.conn = sqlite3.connect('auto-poster.db')
        self.c = self.conn.cursor()
        self.c.execute("PRAGMA foreign_keys = ON")


    def add_new_user(self, user_data):
        data_tuple = (user_data["username"], user_data["password"], user_data["email_address"])
        self.c.execute("INSERT INTO Users (username, password, email_address) VALUES (?,?,?)", data_tuple)
        self.conn.commit()

    def delete_user(self, username):
        self.c.execute("DELETE from Users WHERE username = ?", (username,))
        self.conn.commit()

    def add_new_car(self, car_data, username):
        car_data["username"] = username
        self.c.execute("""
        INSERT INTO Cars (
            VIN, images_directory_path, description, car_brand, car_body, fuel_type,
            year, miles, engine, price, author, email, phone_number, city, user_id
        ) VALUES (
            :VIN, :images_directory_path, :description, :brand, :body, :fuel,
            :year, :mileage, :engine, :price, :author, :email, :phone_number, :city, :user_id
                    )
        """, car_data)
        self.conn.commit()

    def delete_car(self, car_data):
        self.c.execute("DELETE from Cars WHERE VIN = ?", (car_data["VIN"],))
        self.conn.commit()

    def create_empty_database(self):
        self.c.execute("""CREATE TABLE Users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email_address TEXT NOT NULL)
        """)


        self.c.execute("""CREATE TABLE Cars(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
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

    def close_connection(self):
        self.conn.close()

