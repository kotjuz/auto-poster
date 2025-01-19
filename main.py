from database import Database

db = Database()

data = {
    "username": "Marti",
    "password": "<PASSWORD>",
    "email_address": "<EMAIL>",
}
db.delete_user("Rafal")